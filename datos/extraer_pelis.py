'''
Programa que extrae los datos de https://www.imdb.com/chart/top/
y genera un json ...

'''


def datos_peli(peli):
    ''''
    Función que dado un elemento tr de imdb con 
    los datos de una película devuelve un diccionario
    con los datos de ...
    '''
    # datos a devolver
    datos = {}

    elementos = peli.xpath(".//td")
    imagen = elementos[0]
    titulo = elementos[1]

    #imagen
    imagensrc = imagen.xpath(".//img/@src")[0]
    datos['img'] = imagensrc

    # url de la peli
    url = titulo.xpath(".//a/@href")[0]
    datos['url'] = url

    # cast
    cast = titulo.xpath(".//a/@title")[0]
    datos['cast'] = cast

    # titulo
    titulo_ = titulo.xpath(".//a/text()")[0]
    datos['titulo'] = titulo_

    # año
    year = titulo.xpath(".//span/text()")[0].replace("(", "").replace(')', '')
    datos['year'] = year
    
    return datos
