#!/usr/bin/python3
"""*dos*
hello.py
  justamente es el script que toca escribir (ahí lo tienes escrito), luego de
  indicar en clase que ya teníamos un script en el repositorio que conseguía
  listar 'títulos' de fotos desde el fedd público de Flickr.
  Completa el proyecto. Lo que falta es presentar resultados.
  -- se está viendo se te ha servido la introducción que estamos llevando sobre
     python y el fw web flask"""
from flask import Flask, render_template
from lxml import etree
from urllib.request import urlopen
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person/<name>')
def person(name):
    return render_template('person.html',a_name=name)

@app.route('/titulosFotosSevilla')
def titFotos():
    titulosFotos = list()
    titulosFotos = findTitulos()
    return render_template('titFotos.html', titulos=titulosFotos)

@app.route('/FotosSevilla')
def imagesFotos():
    imagesFotos = list()
    imagesFotos = findimages()
    return render_template('titFotos.html', arcompleto=imagesFotos)

@app.route('/advices')
def advices():
    data = [
       'Always finish what you started',
       'Do what you\'re doing your best',
       'Do not cling to anything that will eventually destroy you'
    ]
    return render_template('advices.html', comments=data)

def findimages():
  ns={"Atom" : "http://www.w3.org/2005/Atom"}
  parser=etree.XMLParser()
  tree=etree.parse(urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=sevilla'),parser)
  links = tree.xpath("//Atom:entry/Atom:link[@rel='enclosure']/@href", namespaces=ns)
  arNodes = tree.xpath('//Atom:entry/Atom:title', namespaces=ns)
  images = list()
  arTitulos = list()
  arcompleto = (images,arTitulos)
  for link in links:
    images.append(link)
    print(link)
  for node in arNodes:
    arTitulos.append(node.text)
    print(node.text)
  return arcompleto
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)


