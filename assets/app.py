from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Lee el archivo Excel en un DataFrame de pandas
df = pd.read_excel('assets/figthers_data.xlsx')

# Convierte el DataFrame a un diccionario
fighters = df.to_dict(orient='index')

@app.route('/fighter/<int:id>', methods=['GET'])
def get_fighter(id):
    fighter = fighters.get(id, {})
    return jsonify(fighter)

if __name__ == '__main__':
    app.run(debug=True)