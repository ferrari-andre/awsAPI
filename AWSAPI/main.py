import cv2
import base64


class ProcessImg:
    def decode(encoded_img):
        path_auxiliar = 'teste.jpg'
        with open(path_auxiliar, 'wb') as file:
            file.write(base64.b64decode(encoded_img))
            file.close()
        output = cv2.imread(path_auxiliar)

        return output
    
    def encode(img):
        path = ""
        cv2.imwrite(path, img)
        with open(path, 'rb') as file:
            code = base64.b64encode(file.read())
            file.close()
        
        return code.decode('utf-8')


ProcessImg.encode('teste.jpg')