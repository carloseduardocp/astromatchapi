from flask import Flask, request, jsonify
from openastro import Chart
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["POST"])
def gerar_mapa():
    dados = request.json

    nome = dados.get("nome")
    data = dados.get("data")  # formato: YYYY-MM-DD
    hora = dados.get("hora")  # formato: HH:MM
    latitude = float(dados.get("latitude"))
    longitude = float(dados.get("longitude"))

    dt = datetime.strptime(data + " " + hora, "%Y-%m-%d %H:%M")
    chart = Chart(date=dt, latitude=latitude, longitude=longitude)

    return jsonify({
        "nome": nome,
        "mapa_json": chart.to_json()
    })

if __name__ == "__main__":
    app.run()
