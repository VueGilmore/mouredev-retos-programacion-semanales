'''
Reto #5: ASPECT RATIO DE UNA IMAGEN

Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/
  mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una
  imagen de 1920*1080px.
'''

# Help by ChatGPT

from PIL import Image   # import the Image module from PIL library
import urllib.request   # import the request module from urllib library

# Define the URL of the image
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Open the image from the URL using urllib
with urllib.request.urlopen(url) as url:
    s = url.read()

# Save the image in a local file
with open("./2022/reto-05.jpg", "wb") as f:
    f.write(s)

# Open the image
image = Image.open("./2022/reto-05.jpg")

# Get the width and height of the image
width, height = image.size

# Calculate the aspect ratio
aspect_ratio = width / height

# Print the aspect ratio
print("Aspect ratio:", aspect_ratio)




# Another way of doing it.

import requests
from PIL import Image
from io import BytesIO

# Define the URL of the image
#url = "https://via.placeholder.com/1920x720.png"
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Send a GET request to the URL and get the image data
response = requests.get(url)
im = Image.open(BytesIO(response.content))

# Get the width and height of the image
width, height = im.size

# Calculate the aspect ratio
aspect_ratio = width / height

# Print the aspect ratio
print("Aspect ratio:", aspect_ratio)
