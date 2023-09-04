from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

CORS(app)
# Utiliza una ruta relativa para leer el archivo Excel
df = pd.read_excel("fighters_data.xlsx")  # Aquí he quitado la ruta completa

# Convierte el DataFrame a un diccionario
fighters = df.to_dict(orient='index')

@app.route('/fighter/<int:id>', methods=['GET'])
def get_fighter(id):
    return jsonify(fighters.get(id, {}))

if __name__ == '__main__':
    app.run(debug=True)