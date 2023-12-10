import base64
import json

def lambda_handler(event, context):
    if 'body' in event and event['body'] is not None:
        request_body = json.loads(event['body'])

        if 'image' in request_body:
            image_base64 = request_body['image']
            decoded_image = base64.b64decode(image_base64)
            enconded_image = base64.b64decode(decoded_image).decode('utf-8')

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Imagem recebida!'})
            }
        
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Imagem babou!'})
            }
        
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Babou geral.'})
        }