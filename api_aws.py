import base64
import requests
import json


with open('imagem.png','rb') as file:
    encoded_image = base64.b64decode(file.read()).decode('utf-8')

url = " "

data = {
    'image': encoded_image
}

headers = {
    "Content-Type": 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)
if response.status_code == 200:
    response_data = response.json()
    received_image = response_data.get("image")
    decoded_image = base64.b64decode(received_image)

    with open('...', 'wb') as output:
        output.write(decoded_image)
else:
    print("Ai babou!")
    #çlk\sjdhefgçlksjgdçwiuegfçWI
    #\KSDJHFGLSidhgfçlisuYDGFÇLSDI