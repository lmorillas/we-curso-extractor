# Extractor de páginas de un curso en mediawiki / wikieducator


Scraper para extaer páginas de un curso de mediawiki a una estructura *.json*

Después se procesa el archivo .json para crear ficheros .md Las imágenes se guardan en una carpeta images 
y se modifica la ruta de los ficheros .md

## Instalar
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements
```

## Ejecutar scraper
```
$ scrapy crawl we -o wedrive.json
```

## Generar ficheros .md y descargar imágenes
```
$ python extraer_json.py
```



