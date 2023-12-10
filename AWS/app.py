from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_data():
    url = "https://9o9upqxms6.execute-api.us-east-2.amazonaws.com/estagioTeste/"
    response = requests.post(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return jsonify(data)

    else:
        return jsonify({"Mensagem": "Erro"})


app.run(debug=True)
