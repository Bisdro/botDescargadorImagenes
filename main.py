import requests
from bs4 import BeautifulSoup
from requests.exceptions import URLRequired
print("bienvenido al bot descargador de iamgenes")
url =input("inserte la url por favor \n")
urlObtenida =requests.get(url)
soup = BeautifulSoup(urlObtenida.content , "html.parser")

bodysImagenes = str(soup.find("body"))
textoBodys =open("textoFoto.txt","wt")
subLista = bodysImagenes.split()
preImagen =subLista[1]
URLimagenFinal ="https://catalogo.bn.gov.ar"+ str(preImagen.split('"')[1])
textoBodys.write(URLimagenFinal)
textoBodys.close()
print("la  url imagen final es "+URLimagenFinal)


