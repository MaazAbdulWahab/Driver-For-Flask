import requests
from PIL import Image


data={'image' :open('puppy.jpg','rb')}



reply=requests.post('http://127.0.0.1:8080/check', files=data)

file = open("returnimage.jpg", "wb")
file.write(reply.content)
file.close()

im=Image.open('returnimage.jpg')
im.show()



