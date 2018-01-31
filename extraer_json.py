import json
from slugify import slugify
import pypandoc
import urllib
import os

URL_BASE = 'http://es.wikieducator.org'
IMAGES = 'images/'


def cambia_url_imagen(texto, url):
    nueva_url = IMAGES + os.path.split(url)[-1]
    return texto.replace(url, nueva_url)

data = json.load(open('wedrive.json'))

for doc in data:
    title = slugify(doc['title'])
    texto = doc['html']

    for im in doc.get('images'):
        texto = cambia_url_imagen(texto, im)
    
    doc_md = pypandoc.convert_text(texto, 'md', format='html')

    with open('{}.md'.format(title), 'w') as fw:
        fw.write(doc_md)

    for image in doc.get('images'):
        urllib.request.urlretrieve(URL_BASE + image, 
            filename = IMAGES + os.path.split(image)[-1])
    