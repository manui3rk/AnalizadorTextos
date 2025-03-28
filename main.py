import csv
import os
from collections import Counter #contador de estadísticas: 
import operator
import re, string
from typing import Text
import docx


list_ad = [] #Lista para guardar palabras del diccionario: Adverbios
list_adj = [] #Lista para guardar palabras del diccionario: Adjetivos
list_art = [] #Lista para guardar palabras del diccionario: Artículos
list_pron = [] #Lista para guardar palabras del diccionario: Pronombres
list_prep = [] #Lista para guardar palabras del diccionario: Preposiciones
list_sus = [] #Lista para guardar palabras del diccionario: Sustantivos
list_iniciales = [] #Lista para abreviaturas.  
contar_words = ['No analizado']
contar_caract = ['No analizado']
informe_adj = ['No analizado']
informe_prep = ['No analizado']
informe_ad = ['No analizado']
pala_mente = ['No analizado']
pala_su = ['No analizado']
informe_adj_frase_avanzado = []
informe_prep_frase_avanzado = []
informe_ad_frase_avanzado = []

repeticion_informe = ['No se analizó la aliteración de palabras en el texto']
path = 'D:\\TRABAJO\\PYTHON\\AnalizadorTextos\\DICCIONARIO'
path_carga = 'D:\\TRABAJO\\PYTHON\\AnalizadorTextos'

def pausa():
    input('Pulsa Enter para continuar')
    #os.system('cls')

def lectura_ficheros():
    #1ºLee los ficheros.csv por tipo de palabras, y carga las listas de palabras en sus respectivas listas
    #2ºCarga las listas en sus compresores, haciendo una lísta única para el tipo de palabra.
    fich = '/ad_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8') #encoding='utf-8' permite uso de símbolos como tildes y ñ
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_ad.append(fila[0]) #IMPORTANTE!!!!!! ELIMINA LA SEGUNDA LISTA
    lectura.close()

    fich= '/adj_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_adj.append(fila[0])
    lectura.close()

    fich = '/art_fich.csv' 
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_art.append(fila[0])
    lectura.close()


    fich = '/pron_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_pron.append(fila[0])
    lectura.close()
    
    fich = '/prep_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_prep.append(fila[0])
    lectura.close()

    fich = '/AlfabetoPunto.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_iniciales.append(fila[0])
    lectura.close()

    fich = '/sus_fich.csv'
    lectura = open(path + fich, 'r', encoding='utf-8')
    abrir = csv.reader(lectura)
    for fila in abrir:
        list_sus.append(fila[0])
    lectura.close() 

def carga_informe(x):
    informe_dir = path_carga + '/INFORME'
    os.makedirs(informe_dir, exist_ok=True)  # ✅ Esto crea la carpeta si no existe

    with open(informe_dir + '/informe.txt', 'w', encoding='utf-8') as fichero:
        escri = f'SU TEXTO: {x}\n\nCARACTERES: {contar_caract[0]}\nPALABRAS: {contar_words[0]}\n{informe_ad[0]}\n{informe_adj[0]}\n{informe_prep[0]}\n{pala_mente[0]}\n{pala_su[0]}\n\nPALABRAS REPETIDAS MÁS DE 3 VECES: {repeticion_informe}'
        fichero.write(escri)

    print('')
    input('Informe generado. Pulsa Enter para continuar')
    os.system('cls')
    menu_inicial()
#Dejo texto de prueba. De introducir algún input, se deberá hacer de párrafor a párrafo. Intentar meter más de un párrafo da un error sobre el visual studio code (Entiende los saltos de linea como ENTER)

# x = input("INTRODUCE EL PÁRRAFO DE UN TEXTO: ")

from docx import Document

def leer_docx(ruta_archivo):
    doc = Document(ruta_archivo)
    texto = "\n".join([p.text for p in doc.paragraphs])
    print(texto)
    return texto

def leer_txt(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        return f.read()

modo = input("¿Quieres introducir texto (1), leer .txt (2) o .docx (3)? ")

if modo == "1":
    x = input("INTRODUCE EL PÁRRAFO DE UN TEXTO: ")
elif modo == "2":
    ruta = input("Introduce la ruta del archivo .txt: ")
    x = leer_txt(ruta)
elif modo == "3":
    ruta = input("Introduce la ruta del archivo .docx: ")
    x = leer_docx(ruta)
else:
    print("Opción no válida.")


lectura_ficheros()

def inicio():
    print('')
    print('')
    print('Esto se trata de una librería de funciones para ayudar a la corrección de estilo en un texto literario.\nIMPORTANTE:No se trata de una corrección ortográfica. Esta librería trata de hacer recomendaciones (que queda en decisión del autor tomar o no) para mejorar el ritmo de lectura en el lector.')
    pausa()
    os.system('cls')
    menu_inicial()

def menu_inicial():

    print('menú inicial'.upper().center(100,'*'))
    print(f'1== Contar los caracteres de tu texto')
    print(f'2== Contar el número de palabras totales de tu texto')
    print(f'3== Contar el número de frases que tiene tu texto')
    print(f'4== ¿Que palabra se repite más en todo el texto?')
    print(f'5== Señalar las palabras acabas en -mente')
    print(f'6== Buscar palabras "Su" (Redundancia)')
    print(f'7== Contar palabras (AVANZADO)')
    print(f'8== Contar oraciones (AVANZADO)')
    print(f'9== Generar informe')
    print(f'')
    print(f'0== SALIR')
    op = input('¿Que opición desea utilizar?: ')
    
    if op == "1":
        contar_caracteres(x)
    elif op == "2":
        contar_palabras(x)
    elif op =="3": 
        dividir_frases(x)
    elif op == '4':
        frecuencia_palabras(x)
    elif op == '5':
        palabra_mente(x)
    elif op == '6':
        buscar_su(x)
    elif op == '7':
        contar_palabras_avanzado(x)
    elif op == '8':
        dividir_frases_avanzado(x)    
    elif op == '9':
        carga_informe(x)
    elif op == '0':
        print('GRACIAS')

    else:
        print('')
        print('NO EXISTE DICHA OPCIÓN O ESTÁ EN CONSTRUCCIÓN')
        menu_inicial()

def contar_caracteres(x):
    #Cuenta los caracteres del texto. CON SIGNOS DE PUNTAUCIÓN :
    caracteres = (f'\nEl texto tiene: {len(x)} caracateres \n')
    print(caracteres)
    contar_caract.clear()
    contar_caract.append(caracteres)
    pausa()
    menu_inicial()

def contar_palabras(x):    
    no_puntuacion = x.translate(str.maketrans('', '', string.punctuation)) #Quita los signos de puntuación.
    text_frase = no_puntuacion.lower().split() #lo separa por palabras y crea una lista. 
    input('\nEl siguiente proceso contará el número de adverbios, adjetivos y preposiciones, y te dará un porcentaje global de uso según palabras. \nTenga en cuenta que el abuso de este tipo de palabras, pueden enlentecer la lectura y crear redundancias\nUn texto sobreadjetivado puede parecer poético, pero también saturar al lector.\nAhora se le dará un porcentaje, y deberá valorar si debe o no quitar algunos de estos elementos de su texto.\nIMPORTANTE: Tenga en cuenta que muchas palabras pueden tener distintos usos, y el sondeo se realiza con el diccionario de la RAE\nSi quiere una visión más precisa de estos porcentajes, utilice la versión avanzada de contar palabras.\nPULSE ENTER PARA CONTINUAR...')
    palabras = (f'\nEl texto tiene: {len(text_frase)} palabras') #te da el número de elementos que tiene la lista = cuenta las palabras
    print(palabras)
    contar_adverbios(text_frase) #Llama a la función contar_adverbios. 
    contar_adjetivos(text_frase) #Llama a la función contar_adjetivos. 
    contar_preposiciones(text_frase) #Llama a la función contar_preposiciones. 
    contar_words.clear()
    contar_words.append(palabras)
    pausa()
    menu_inicial()

def contar_adverbios(x):
    if type(x) is list:
        ad = [] #Lista donde meterá las palabras que comprobará con diccionario correspondiente. 
        por =  len(x) #Lo usará más adelante para dar el porcentaje, a base de hacer la medición de X 
        for ele in x: #Bucle para comprobar palabras
            if ele in list_ad: #Sí la palabra del bucle, coincide con alguna de la lista del diccionario correspondiente...
                ad.append(ele) #... la añade a la lista AD
        x = (f'\t De las cuales {len(ad)} son adverbios. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%') #Len(ad) da el número de palabras incluida en la lista. La siguiente función da el porcentaje (Float) con dós dígitos.  
        print(x)
        informe_ad.clear()
        informe_ad.append(x)

    elif type(x) is str: #Esto se utiliza para gestionar la "x" desde contar_oraciones

        lista = x.split() #Antes separa las palabras en una lista y continúa por el mismo proceso. 
        ad = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_ad:
                ad.append(ele)
        x = (f'\t De las cuales {len(ad)} son adverbios. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%')
        print(x)

def contar_adverbios_oracion(x):
    pass

def contar_adjetivos(x):
    if type(x) is list:
        ad = [] 
        por =  len(x)
        for ele in x:
            if ele in list_adj:
                ad.append(ele)
        x = (f'\t De las cuales {len(ad)} son adjetivos. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%')
        print(x)
        informe_adj.clear()
        informe_adj.append(x)
    elif type(x) is str:
        lista = x.split()
        ad = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_adj:
                ad.append(ele)
        x = (f'\t De las cuales {len(ad)} son adjetivos. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%')
        print(x)

def contar_preposiciones(x):
    #1º convierte la cadena en minúsculas para poder hacer la comparación.    
    #2º Cuenta las preposiciones totales del texto.    
    if type(x) is list:
        ad = [] 
        por =  len(x)
        for ele in x:
            if ele in list_prep:
                ad.append(ele)
        x = (f'\t De las cuales {len(ad)} son preposiciones. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%')
        print(x)
        informe_prep.clear()
        informe_prep.append(x)

    elif type(x) is str:
        lista = x.split()
        ad = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_prep:
                ad.append(ele)
        x = (f'\t De las cuales {len(ad)} son preposiciones. Lo que constituye un {"{0:.2f}".format(float((len(ad)/por)*100))}%') 
        print(x)

def frecuencia_palabras(x):
    print('')
    print('Uno de los errores más típicos en la escritura es la aliteración de palabras. Algo fácil de ver en oraciones, pero más difícil en su conjunto\nEsta función delimitará las palabras más utilizadas en el texto para que el escritor pueda reflexionar sobre ello.')
    r = x.split() # ->
    for palabra in r: # ->
        if palabra in list_iniciales: #->
            x = x.replace(palabra,'word') #-> Esto quita las iniciales. Pasa el bucle por una lista, y si encuentra alguna inicial (T. o J.) la cambia por la palabra word en el texto. 

    print(f'SOLO APARECEN LAS PALABRAS QUE SE REPITAN MÁS DE 3 VECES\n')
    texto = x.translate(str.maketrans('', '', string.punctuation)) #-> Se quitan signos de puntuación
    contar_palabras = texto.lower().split() #-> Se divide en minúsculas para crear la lista contar_palabras
    repeticion_informe.clear()
    frecuenciaPalab = [] #-> Lista para frecuencia de palabras. 
    for p in contar_palabras: #->
        frecuenciaPalab.append(contar_palabras.count(p)) #-> Se crea una lista con el número de veces que se repite cada palabra. 
    
    repeticiones = [] #-> Lista para introducir repeticiones. 

    por = len(contar_palabras) #-> Se crea para medir porcentaje 

    for x in range(0, len(contar_palabras)):  #->
        repeticiones.append((contar_palabras[x], frecuenciaPalab[x]))  #->

    frecuencia = list(set(repeticiones)) #-> se crea una lista con sets que quitan las palabras repetidas para luego meterlo en una lista de duplas (palabra, nº de veces que se repite)

    frecuencia = sorted(frecuencia, key=operator.itemgetter(1), reverse=True) #->
    for x in range(0, len(frecuencia)):#->
        if frecuencia[x][1] >= 3: #-> Si dentro del bucle no aparece más de 3 veces, se omite. 
            if frecuencia[x][0].lower() in list_prep: #-> Si es una preposición, se omite
                pass
            elif frecuencia[x][0].lower() in list_art: #-> Si no está en la lista de artículos, se omite. 
                pass
            elif frecuencia[x][0].lower() == 'y': #-> Si es una conjunción se omite. 
                pass
            else:
                x = (f'La palabra {frecuencia[x][0].upper()} aparece {str(frecuencia[x][1])} veces. Supone un {"{0:.2f}".format(float((frecuencia[x][1])/por)*100)}% del texto. ') 
                print(x)
                repeticion_informe.append(x)

    print('')
    pausa()
    menu_inicial()

def dividir_frases(x): #Divide en frases
    print('')
    input('ESTO DIVIDIRÁ EL TEXTO EN ORACIONES, Y HARÁ PORCENTAJES DE ADVERBIOS/ADJETIVOS/PREPOSICIONES POR ORACIÓN. IMPORTANTE: NO GENERARÁ INFORME\n\nPULSA ENTER PARA CONTINUAR')
    r = x.split() # ->
    for palabra in r: # ->
        if palabra in list_iniciales: #->
            x = x.replace(palabra,'word') #-> Esto quita las iniciales. Pasa el bucle por una lista, y si encuentra alguna inicial (T. o J.) la cambia por la palabra WORD en el texto. 
                #¿Y si hay una inicial al final del texto? IMPORTANTE (TRABAJANDO EN ELLO) !############################################
    Frases = x.lower().split('.') #Una vez quitadas las iniciales, busca los puntos (.) para separar las oraciones. Pone el texto en minúsculas y lo separa por iniciales en una lista. 
    no_punt_fra = [] #-> 
    for fra in Frases: #->
        no_punt_fra.append(fra.translate(str.maketrans('', '', string.punctuation))) #-> Quita TODOS los signos de puntuación y los añade a la lista no_punt_fra
    print(f' El texto tiene {len(Frases)-1} oraciones') #Resta la última oración porque estará vacía. 
    input('Pulsa ENTER PARA CONTINUAR'.upper()) 
    for fra in no_punt_fra:
        fra_pa = fra.split() #->Divide cada frase en número de palabras para medirla posteriormente. 
        if len(fra_pa) == 0: #-> Si encuentra una frase vacía (la última) no la analiza. 
            pass
        else:
            print(f'Frase {no_punt_fra.index(fra)} tiene {len(fra_pa)} palabras') #Imprime el número de frase, y dice cuantas palabras tiene 
            contar_adverbios(fra) #pasa cada frase de la lista no_punt_fra por sus respectivos analizadores de palabras. 
            contar_adjetivos(fra)
            contar_preposiciones(fra)
    menu_inicial()

def palabra_mente(x):
    texto = x.translate(str.maketrans('', '', string.punctuation)) #-> Quita singos de puntuación
    text = texto.lower().split() #-> Texto en minúsculas y convertido en lista
    mente = [] #-> Lista vacía para almacenar las palabras acabadas en -mente. 
    lista = [] #-> Lista vacía para menter TODO el texto y poder hacer porcentajes según longitud del texto. 
    for ele in text: #->
        if ele[-5:] == 'mente': #-> Bucle que busca las palabras acabadas en 'mente'. 
            mente.append(ele) #-> Las introduce en la lista mente
        lista.append(ele) #-> introduce TODAS las palabras 
    x = (f'\nLas palabras acabadas en -mente aparecen un número de {len(mente)} veces. Lo que constituye un {"{0:.2f}".format(float((len(mente)/len(lista))*100))}%')
    print(x)
    pala_mente.clear()
    pala_mente.append(x)
    print('')
    op = input('Las palabras acabadas en -mente son ADVERBIOS construidos a través de ADJETIVOS. Pueden entorpecer la lectura.\n \nSe recomienda su eliminación siempre que sea posible\n \n¿Desea ver las palabras en el texto? "y" para afirmar. Cualquier otra tecla para negar: ')
    #-> Se da una recomendación, y se pregunta si se quiere ver las palabras acabadas en mente en su contexto, de forma que uno pueda decidir si sobra o no. 
    if op.lower() == 'y':
        for ele in lista: 
            if ele[-5:] == 'mente':
                print(f'... {lista[lista.index(ele)-2]} {lista[lista.index(ele)-1]} {lista[lista.index(ele)]} {lista[lista.index(ele)+1]} {lista[lista.index(ele)+2]}...')
    pausa()
    menu_inicial()

def buscar_su(x): 
    print(f'')
    print(f'Con esta opción se buscarán las palabras SU del texto. Dichas palabras tienden a usarse erroneamente como posesivo, creando redundancias\nPOR EJEMPLO: Él se agarró su mano... Cuando obviamente si SE agarró la mano, es obvio que es SU mano. \nSe mostrarán frases con SU para que valores su contexto y decidas si debes quitarla')
    print('')
    input('Pulse Enter para continuar')    
    print('')
    su = []
    s = ['su','sus']
    texto = x.translate(str.maketrans('', '', string.punctuation)) #-> Quita singos de puntuación
    text = texto.lower().split() #-> Texto en minúsculas y convertido en lista
    lista = [] #-> Lista vacía para menter TODO el texto y poder hacer porcentajes según longitud del texto. 
    for ele in text: #->
        if ele in s: #-> Bucle que busca las palabras acabadas en 'su/sus'. 
            su.append(ele) #-> Las introduce en la lista "su"
    # for ele in text:
    #     if ele == 'sus':
    #         su.append(ele) #-> Las introduce en la lista "sus"

        lista.append(ele) #-> introduce TODAS las palabras 
    
    x = (f'\nEl uso de su/sus aparecen un número de {len(su)} veces. Lo que constituye un {"{0:.2f}".format(float((len(su)/len(lista))*100))}%')
    print(x)
    pala_su.clear()
    pala_su.append(x)
    print('')

    #IMPORTANTE: Lo que viene a continuación sería mostrar al usuario la palabra en un contexto, pero parece que Python tiene algún problema con "su/sus" y no sabe sacarlas de la lista de elemntos. Se ha probado con otros textos y en otros ficheros .py y pasa igual
    # op = input('¿Desea ver las palabras en el texto? "y" para afirmar. Cualquier otra tecla para negar: ')
    # #-> Se da una recomendación, y se pregunta si se quiere ver las palabras acabadas en mente en su contexto, de forma que uno pueda decidir si sobra o no. 
    # if op.lower() == 'y':
    #     for ele in lista: 
    #         if ele == 'su':
    #             print(f'... {lista[lista.index(ele)-2]} {lista[lista.index(ele)-1]} {lista[lista.index(ele)]} {lista[lista.index(ele)+1]} {lista[lista.index(ele)+2]}...')

    #PRUEBA: 
    # x = ['muchacho', 'su','sus','pony','su','casa']

    #     for ele in x: 
    #         if ele == 'su':
    #             print(f'... {x[x.index(ele)-1]} {x[x.index(ele)]} {x[x.index(ele)+1]}...')
    #RESULTADO
    # ... muchacho su sus...
    # ... muchacho su sus...

    pausa()
    menu_inicial()

def contar_palabras_avanzado(x):
    no_puntuacion = x.translate(str.maketrans('', '', string.punctuation)) #Quita los signos de puntuación.
    text_frase = no_puntuacion.lower().split() #lo separa por palabras y crea una lista. 
    input('\nEl siguiente proceso contará el número de adverbios, adjetivos y preposiciones, y te dará un porcentaje global de uso según palabras. \nTenga en cuenta que el abuso de este tipo de palabras, pueden enlentecer la lectura y crear redundancias\nUn texto sobreadjetivado puede parecer poético, pero también saturar al lector.\nAhora se le dará un porcentaje, y deberá valorar si debe o no quitar algunos de estos elementos de su texto.\nIMPORTANTE: Tenga en cuenta que muchas palabras pueden tener distintos usos, y el sondeo se realiza con el diccionario de la RAE\nCon cada discordancia se valorará la palabra en su contexto y el autor podrá decidir.\nPULSE ENTER PARA CONTINUAR...')
    contar_adverbios_avanzado(text_frase) #Llama a la función contar_adverbios. 
    contar_adjetivos_avanzado(text_frase) #Llama a la función contar_adjetivos. 
    contar_preposiciones_avanzado(text_frase) #Llama a la función contar_preposiciones. 
    x = (f'\nEl texto tiene: {len(text_frase)} palabras') #te da el número de elementos que tiene la lista = cuenta las palabras
    contar_words.clear()
    contar_words.append(x)
    print(x)
    print(informe_ad[0])
    print(informe_adj[0])
    print(informe_prep[0])
    pausa()
    menu_inicial()

def contar_adverbios_avanzado(x):
    if type(x) is list: #Comprueba si X es una lista o un string. 
        ad_avanzado = [] #Lista donde meterá las palabras que comprobará con diccionario correspondiente. 
        por =  len(x) #Lo usará más adelante para dar el porcentaje, a base de hacer la medición de X 
        for ele in x: #Bucle para comprobar palabras
            if ele in list_ad: #Sí la palabra del bucle, coincide con alguna de la lista del diccionario correspondiente...
                print('')
                print(f'... {x[x.index(ele)-2]} {x[x.index(ele)-1]} {ele.upper()} {x[x.index(ele)+1]} {x[x.index(ele)+2]}...') #Te da la palabra en el contexto del texto y te pregunta si la escribiste cómo un adverbio
                print('')
                question = input(f'¿Es la palabra {ele.upper()} un ADVERBIO? ("y" para afirmar. Cualquier otro caracter para negar: ')
                if question.lower() == 'y':
                    ad_avanzado.append(ele) #... En caso afirmativo, la añade a la lista de adverbios empleados en el texto
        x = (f'\t De las cuales {len(ad_avanzado)} son adverbios. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%') #Len(ad) da el número de palabras incluida en la lista. La siguiente función da el porcentaje (Float) con dós dígitos.  

        informe_ad.clear()
        informe_ad.append(x)


    elif type(x) is str: #Si es un string....
        lista = x.split() #Antes separa las palabras en una lista y continúa por el mismo proceso. Esta diferenciación la uso para diferenciar entre la función de CONTAR PALABRAS y CONTAR ORACIONES, ya que el resultado de las mismas, difiere en string o lista. 
        ad_avanzado = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_ad:
                print('')
                print(f'... {lista[lista.index(ele)-2]} {lista[lista.index(ele)-1]} {ele.upper()} {lista[lista.index(ele)+1]} {lista[lista.index(ele)+2]}...')
                print('')
                question = input(f'¿Es la palabra {ele.upper()} un ADVERBIO? ("y" para afirmar. Cualquier otro caracter para negar: ')
                if question.lower() == 'y':
                    ad_avanzado.append(ele)
        x = (f'\t De las cuales {len(ad_avanzado)} son adverbios. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%')
        informe_ad_frase_avanzado.clear()
        informe_ad_frase_avanzado.append(x)

def contar_adjetivos_avanzado(x):
    if type(x) is list: #Comprueba si X es una lista o un string. 
        ad_avanzado = [] #Lista donde meterá las palabras que comprobará con diccionario correspondiente. 
        por =  len(x) #Lo usará más adelante para dar el porcentaje, a base de hacer la medición de X 
        for ele in x: #Bucle para comprobar palabras
            if ele in list_adj: #Sí la palabra del bucle, coincide con alguna de la lista del diccionario correspondiente...
                print('')
                print(f'... {x[x.index(ele)-2]} {x[x.index(ele)-1]} {ele.upper()} {x[x.index(ele)+1]} {x[x.index(ele)+2]}...') #Te da la palabra en el contexto del texto y te pregunta si la escribiste cómo un adverbio
                print('')
                question = input(f'¿Es la palabra {ele.upper()} un ADJETIVO? ("y" para afirmar. Cualquier otro caracter para negar: ')
                if question.lower() == 'y':
                    ad_avanzado.append(ele) #... En caso afirmativo, la añade a la lista de adjetivos empleados en el texto
        x = (f'\t De las cuales {len(ad_avanzado)} son ADJETIVOS. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%') #Len(ad) da el número de palabras incluida en la lista. La siguiente función da el porcentaje (Float) con dós dígitos.  
        informe_adj.clear()
        informe_adj.append(x)


    elif type(x) is str: #Si es un string....
        lista = x.split() #Antes separa las palabras en una lista y continúa por el mismo proceso. Esta diferenciación la uso para diferenciar entre la función de CONTAR PALABRAS y CONTAR ORACIONES, ya que el resultado de las mismas, difiere en string o lista. 
        ad_avanzado = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_adj:
                print('')
                print(f'... {lista[lista.index(ele)-2]} {lista[lista.index(ele)-1]} {ele.upper()} {lista[lista.index(ele)+1]} {lista[lista.index(ele)+2]}...')
                print('')
                question = input(f'¿Es la palabra {ele.upper()} un ADJETIVO? ("y" para afirmar. Cualquier otro caracter para negar: ')
                if question.lower() == 'y':
                    ad_avanzado.append(ele)
        x = (f'\t De las cuales {len(ad_avanzado)} son adverbios. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%')
        informe_adj_frase_avanzado.clear()
        informe_adj_frase_avanzado.append(x)

def contar_preposiciones_avanzado(x):
    if type(x) is list: #Comprueba si X es una lista o un string. 
        ad_avanzado = [] #Lista donde meterá las palabras que comprobará con diccionario correspondiente. 
        por =  len(x) #Lo usará más adelante para dar el porcentaje, a base de hacer la medición de X 
        for ele in x: #Bucle para comprobar palabras
            if ele in list_prep: #Sí la palabra del bucle, coincide con alguna de la lista del diccionario correspondiente...
                print('')
                print(f'... {x[x.index(ele)-2]} {x[x.index(ele)-1]} {ele.upper()} {x[x.index(ele)+1]} {x[x.index(ele)+2]}...') #Te da la palabra en el contexto del texto y te pregunta si la escribiste cómo un adverbio
                print('')
                question = input(f'¿Es la palabra {ele.upper()} una PREPOSICIÓN? ("y" para afirmar. Cualquier otro caracter para negar: )')
                if question.lower() == 'y':
                    ad_avanzado.append(ele) #... En caso afirmativo, la añade a la lista de preposiciones empleados en el texto
        x = (f'\t De las cuales {len(ad_avanzado)} son preposiciones. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%') #Len(ad) da el número de palabras incluida en la lista. La siguiente función da el porcentaje (Float) con dós dígitos.  
        informe_prep.clear()
        informe_prep.append(x)


    elif type(x) is str: #Si es un string....
        lista = x.split() #Antes separa las palabras en una lista y continúa por el mismo proceso. Esta diferenciación la uso para diferenciar entre la función de CONTAR PALABRAS y CONTAR ORACIONES, ya que el resultado de las mismas, difiere en string o lista. 
        ad_avanzado = [] 
        por =  len(lista)
        for ele in lista:
            if ele in list_prep:
                print('')
                print(f'... {lista[lista.index(ele)-2]} {lista[lista.index(ele)-1]} {ele.upper()} {lista[lista.index(ele)+1]} {lista[lista.index(ele)+2]}...')
                print('')
                question = input(f'¿Es la palabra {ele.upper()} una PREPOSICIÓN? ("y" para afirmar. Cualquier otro caracter para negar: )')
                if question.lower() == 'y':
                    ad_avanzado.append(ele)
        x = (f'\t De las cuales {len(ad_avanzado)} son preposiciones. Lo que constituye un {"{0:.2f}".format(float((len(ad_avanzado)/por)*100))}%')
        informe_prep_frase_avanzado.clear()
        informe_prep_frase_avanzado.append(x)

def dividir_frases_avanzado(x): #Divide en frases
    print('')
    input('ESTO DIVIDIRÁ EL TEXTO EN ORACIONES, Y HARÁ PORCENTAJES DE ADVERBIOS/ADJETIVOS/PREPOSICIONES POR ORACIÓN. IMPORTANTE: NO GENERARÁ INFORME\n\nPULSA ENTER PARA CONTINUAR')
    
    r = x.split() # ->
    for palabra in r: # ->
        if palabra in list_iniciales: #->
            x = x.replace(palabra,'word') #-> Esto quita las iniciales. Pasa el bucle por una lista, y si encuentra alguna inicial (T. o J.) la cambia por la palabra WORD en el texto. 
                #¿Y si hay una inicial al final del texto? IMPORTANTE (TRABAJANDO EN ELLO) !############################################
    Frases = x.lower().split('.') #Una vez quitadas las iniciales, busca los puntos (.) para separar las oraciones. Pone el texto en minúsculas y lo separa por iniciales en una lista. 
    no_punt_fra = [] #-> 
    for fra in Frases: #->
        no_punt_fra.append(f"': : :'{fra.translate(str.maketrans('', '', string.punctuation))}': : :')") #-> Quita TODOS los signos de puntuación y los añade a la lista no_punt_fra
    print(f' El texto tiene {len(Frases)-1} oraciones') #Resta la última oración porque estará vacía. 
    input('Pulsa ENTER PARA CONTINUAR'.upper()) 
    for fra in no_punt_fra:
        fra_pa = fra.split() #->Divide cada frase en número de palabras para medirla posteriormente. 
        if len(fra_pa) == 0: #-> Si encuentra una frase vacía (la última) no la analiza. 
            pass
        else:
            print(fra)
            contar_adverbios_avanzado(fra) #pasa cada frase de la lista no_punt_fra por sus respectivos analizadores de palabras. 
            contar_adjetivos_avanzado(fra)
            contar_preposiciones_avanzado(fra)
            print('')
            input('FRASE ANALIZADA')
            print('')
            print(f'Frase {no_punt_fra.index(fra)} tiene {len(fra_pa)} palabras'.upper()) #Imprime el número de frase, y dice cuantas palabras tiene 
            print(informe_ad_frase_avanzado[0])
            print(informe_adj_frase_avanzado[0])
            print(informe_prep_frase_avanzado[0])
    menu_inicial()

inicio()


