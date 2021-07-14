import csv

list_ad = [] #Almacenador de Adjetivos
list_adj = [] #Almacenador de Adverbios
list_art = [] #Almacenador de Artículos
list_pron = [] #Almacenador de pronombres
list_prep = [] #Almacenador de proposiciones
list_sign = [] #¿Signos de puntuación?

path = 'C:\\Master Python\\ZZZ PROYECTO\\Conseguidos'
def lectura_ficheros():
    #Lee los ficheros.csv por tipo de palabras, y los carga en sus respectivas listas
    fich = '/ad_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8') #encoding='utf-8' permite uso de símbolos como tildes y ñ
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_ad.append(fila)
    lectura.close()

    fich= '/adj_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_adj.append(fila)
    lectura.close()    

    fich = '/art_fich.csv' 
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_art.append(fila)
    lectura.close()
    
    fich = '/pron_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_pron.append(fila)
    lectura.close()
    
    fich = '/prep_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_prep.append(fila)
    lectura.close()    

    return list_art, list_ad, list_adj, list_prep, list_pron



print("{0:.2f}".format(float(5.1234567)))
