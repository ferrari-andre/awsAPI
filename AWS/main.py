from flask import Flask

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def handler():
    return 'Está é a minha API', 200


if __name__ == '__main__':
    app.run(debug=True)