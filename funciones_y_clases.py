global1 = 34

def cambiar_global(a):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = a
    print (global1)

cambiar_global(7)
   


def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    if anio%4 == 0:
      bisiesto = True
      if anio%100 == 0:
        bisiesto = False
        if anio%400 == 0:
          bisiesto = True
        else:
          bisiesto = False
    else:
      bisiesto = False
    #print(bisiesto)
    return(bisiesto)

es_bisiesto = anio_bisiesto(2021)
print(es_bisiesto)
print('')


def contar_valles(lista1):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    lista2 = []
    valora = 0
    valorb = 0
    valoranterior = 0
    #iteracion = 0

    for elemento in lista1:
        valora = elemento
        valorb = valoranterior
        if elemento != 0:
          if (elemento == 1 and len(lista2) > 0) or elemento == -1:
            if valora != valorb:
              lista2.append(elemento)
              valoranterior = elemento
    print(lista2)
    
    valle = 0
    contador = 0

    for elemento2 in lista2:
      valle += elemento2
      print(valle)
      if valle == 0:
        contador += 1
    return(contador)   

terreno=[-1 , 1 , 0 , 1 , 1 , -1 , 0 , 0 , 1 , -1 , 1 , 1 , -1 , -1 ]
cantvalles = contar_valles(terreno)
print('cantidad de valles: ' + str(cantvalles))

terreno=[0 , 1 , 0 , 1 , 1 , -1 , 0 , 0 , 1 , -1 , 1 , 1 , -1 , -1 ]
cantvalles = contar_valles(terreno)
print('cantidad de valles: ' + str(cantvalles))

terreno=[0, 0 , 0 , 1 , 1 , -1 , 0 , 0 , 1 , -1 , -1 , -1 , -1 , -1 ]
cantvalles = contar_valles(terreno)
print('cantidad de valles: ' + str(cantvalles))
print('')

def saltando_rocas(listarocas):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''

    pos = -1
    contador_s = 0
    iterador = 0

    for i in listarocas:

      if iterador == pos or pos == -1:

        if (pos + 3) < len(listarocas):
        
          if listarocas[pos+1] == listarocas[pos+2] == listarocas[pos+3] ==1:
            pass 

          elif listarocas[pos+3] == 0:

            pos += 3
            contador_s += 1
            print('paso1')

          elif listarocas[pos+2] == 0:

            pos += 2
            contador_s += 1
            print('paso2')

          elif listarocas[pos+1] == 0:
            
            pos += 1
            contador_s += 1
            print('paso3')

          print(pos)
          print(contador_s)

        elif (pos + 2) < len(listarocas):

          if listarocas[pos+1] == listarocas[pos+2] ==1:
            pass 

          elif listarocas[pos+2] == 0:

            pos += 2
            contador_s += 1
            print('paso4')

          elif listarocas[pos+1] == 0:

            pos += 1
            contador_s += 1         
            print('paso5') 

          print(pos)
          print(contador_s)

        elif (pos + 1) < len(listarocas):

          if listarocas[pos+1] ==1:
            pass
          elif listarocas[pos + 1] == 0:
            pos += 1
            contador_s += 1   

            print('paso6')     
          print(pos)
          print(contador_s)
          
        print('posicion: ' + str(pos))
        print('contador: ' + str(contador_s))
      
      iterador += 1
      print('')
    return(contador_s)

listar = [0,0,0,1,1,0,1]
cantidad_saltos = saltando_rocas(listar)
print(listar)
print('cantidad de saltos: ' + str(cantidad_saltos))

listar = [0,0,1,1,0,0,1]
cantidad_saltos = saltando_rocas(listar)
print(listar)
print('cantidad de saltos: ' + str(cantidad_saltos))

listar = [0,1,1,1,0,0,1]
cantidad_saltos = saltando_rocas(listar)
print(listar)
print('cantidad de saltos: ' + str(cantidad_saltos))

def pares_medias():
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    pass

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'




# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'





# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.

