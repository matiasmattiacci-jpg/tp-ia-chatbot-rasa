#Servidor de Acciones Personalizadas: Su función principal es gestionar la lógica de negocio fuera del flujo 
#conversacional, permitiendo la integración con la API de CoinGecko para 
#obtener cotizaciones de criptomonedas en tiempo real.

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConsultarPrecio(Action):

    def name(self) -> Text:
        # Este nombre debe coincidir exactamente con el del domain.yml
        return "action_consultar_precio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Extraer la entidad 'crypto' que el bot detectó en el NLU
        crypto_item = next(tracker.get_latest_entity_values("crypto"), None)

        if not crypto_item:
            dispatcher.utter_message(text="No entendí qué moneda buscas. ¿Podrías repetirla? (Ej: bitcoin, ethereum)")
            return []

        # 2. Configurar la llamada a la API de CoinGecko
        # Pasamos el nombre de la moneda a minúsculas para la API
        coin_id = crypto_item.lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

        try:
            response = requests.get(url, timeout=10)
            data = response.json()

            # 3. Validar si la API devolvió datos para esa moneda
            if coin_id in data:
                precio = data[coin_id]['usd']
                mensaje = f"El precio actual de {crypto_item.capitalize()} es de ${precio} USD."
            else:
                mensaje = f"Lo siento, no pude encontrar información sobre '{crypto_item}'. Asegúrate de escribir el nombre completo (ej: bitcoin en lugar de btc si falla)."

        except Exception as e:
            mensaje = "Hubo un error al conectar con el servicio financiero. Por favor, intenta más tarde."
        
        # 4. Enviar la respuesta final al usuario
        dispatcher.utter_message(text=mensaje)

        return []