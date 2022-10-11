
from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/suma',methods = ['POST'])
def Suma():
    numero1 = "number_1",
    numero2 =  "number_2"
    message = ""
    user_name = os.getenv("user_name")
    messageWithUserName, messageWithOutUserName = user_name + " la " + message , "La " + message  

    if request.method == 'POST':

        if not numero1 or not numero2:
            return {"message": "Indique dos numeros para ser sumados"}, 404
        
        numero1, numero2 = request.json["numero_1"], request.json["numero_2"]
        message = f"suma de los dos numeros es: {numero1 + numero2}" 
        message = messageWithUserName + " la " + message if user_name else "La " + messageWithOutUserName 

        return {"message": message}, 200


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)