
from email import message
from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/suma',methods = ['POST'])
def Suma():
    message = ""
    user_name = os.getenv("user_name")
    write_result = os.getenv("write_result")
    print(type(write_result))

    if request.method == 'POST':
        try:
            numero1, numero2 = request.json["num_1"], request.json["num_2"]
        except:
            return {"message": EscribirResultado("Indique dos números para ser sumados", user_name,None,None)}, 404
        
        message = f"suma de los dos números es: {numero1 + numero2}" 
        message = user_name + " la " + message if user_name else "La " + message  

        return {"message": EscribirResultado(message, user_name, numero1, numero2)}, 200

def EscribirResultado(message, user_name ,a ,b):
    if os.getenv("write_result") == "not_show" or not a or not b:
        return message
    f = open("resultado.txt", "w")
    f.write(f"Hola {user_name}! Al sumar {a} y {b} se obtiene como resultado {a+b} ")
    f.close()
    return message


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)