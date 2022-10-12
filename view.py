
from email import message
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
    write_result = os.getenv("write_result")

    if request.method == 'POST':

        if not numero1 or not numero2:
            return {"message": EscribirResultado(write_result, "Indique dos numeros para ser sumados", user_name,None,None)}, 404
        
        numero1, numero2 = request.json["numero_1"], request.json["numero_2"]
        message = f"suma de los dos numeros es: {numero1 + numero2}" 
        message = user_name + " la " + message if user_name else "La " + message  

        return {"message": EscribirResultado(write_result, message, user_name, numero1, numero2)}, 200

def EscribirResultado(write, message, user_name ,a ,b):
    if not write or not a and not b:
        return message
    f = open("resultado.txt", "w")
    f.write(f"Hola {user_name}! Al sumar {a} y {b} se obtiene como resultado {a+b} ")
    f.close()
    return message


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)