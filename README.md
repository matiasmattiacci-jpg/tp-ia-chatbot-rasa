# tp-ia-chatbot-rasa
Tp2 Inteligencia artificial ChatBot 
Autores
- Cortez, Matias
- Mattiacci, Matias
- Widmer, Sergio

Tuvimos que descargar una verion de python mas antigua, 3.10.8 para ser precisos, para que funcionara rasa y tambien cambiar la carpeta del proyecto a una ubcacion mas simple porque tambien daba problemas ya que la ruta total superaba el "limite" y daba error
Comandos utilizados:
- py -3.10 -m venv venv
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
- .\venv\Scripts\activate
- pip install rasa
- rasa init
- pip install requests

En una terminal ->(modo venv) 
- rasa train (Esto procesará todos los archivos .yml y creará un archivo comprimido en la carpeta models.)
- rasa run actions (para correr el servidor de acciones)

En la otra -> (modo venv) 
- rasa shell (aca ejecutamos el bot)