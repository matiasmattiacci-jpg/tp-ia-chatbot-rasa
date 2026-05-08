# tp-ia-chatbot-rasa
Tp2 Inteligencia artificial ChatBot

Comandos utilizados:
- py -3.10 -m venv venv
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
- .\venv\Scripts\activate
- pip install rasa
- rasa init
- pip install requests

En una terminal ->(modo venv) rasa train (Esto procesará todos los archivos .yml y creará un archivo comprimido en la carpeta models.)
y luego "rasa run actions" para correr el servidor de acciones 
En la otra -> (modo venv) rasa shell (aca ejecutamos el bot)