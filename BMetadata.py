#!/usr/bin/env python3
from BScraping import Scraping
import BImages 
class Metadata():
    def __init__(self):
        try:
            url=input("Ingrese el url de donde quiere descargar las imagenes: ")
            scraping = Scraping()
            scraping.scrapingImages(url)
            BImages.image()
        except:
            print("Ah ocurrido un error, por favor, inicie el script de nuevo.")
