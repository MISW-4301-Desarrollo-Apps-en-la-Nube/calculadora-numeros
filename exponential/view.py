from flask import Flask
from flask import request
import os
import requests

app = Flask(__name__)

@app.route('/exponencial',methods = ['POST'])
def Exponencial():
    multiplicacion_url = os.getenv("multiplicacion_ms")
    
    if request.method == 'POST':
        try:
            numero , potencia = request.json["numero"], request.json["potencia"]
        except:
            return {"message": ""}

        resultado = numero
        for _ in range(potencia-1):
            obj = {'num_1': f'{resultado}', 'num_2': f'{numero}'}
            req = requests.post(multiplicacion_url + '/multiplicar', json = obj)
            resultado = req.json()["result"]

        return {"message": f"Elevando {numero} a la {potencia} se obtiene {resultado}" , "result": resultado}, 200
            

""
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)