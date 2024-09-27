"""Se consulta con el usuario si tiene tareas pendientes para comenzar
con el funcionamiento del programa es decir, determinar si inresaremos al 
while o saltaremos directamente al for. """

#Ya se muestra el menu :)
print("Menu:")
print("1. Ingresar tareas")
print("2. Mostrar tareas")
print("3. Eliminar tareas")
"""Se declara la lista que va a guardar las tareas pendientes
(se definen todos sus elementos como None y solo tiene 100 elementos)"""
arreglo_tareas = [None] * 100   
"""Utilizamos el operador aritmetico de multiplicación para declarar el 
arreglo con 100 elementos y todos en None"""

"""Comenzamos a separar todo por funciones, dentro de la funcion ingresar_tareas 
haremos el registro de todas las tareas que el usuario desee y regresaremos 
el arreglo tareas."""
def ingresar_tareas(tarea): 
    i = 0 
    """A continuacion se agrega un bucle que solo terminará en caso de
    que el usuario ingrese que 'No' tiene tareas pendientes"""
    while(tarea=="Si"):
        print("Ingresa el nombre de tu tarea")
        """Esta variable guarda temporalmente el nombre de 
        la tarea:"""
        nom_tarea = input() 
        #Se le asigna a nuestro arreglo en la posicion i el valor de nom_tarea:
        arreglo_tareas[i] = nom_tarea
        """Usamos el operador de suma para que en cada vuelta del while
        la variable i aumente 1 y se vayan agegando las tareas al indice
        correspondiente del arreglo"""
        #Variable de control para nuestro while:
        i = i + 1 
        """Preguntamos al usuario si desea agregar mas tareas, en caso de que si
        repetimos el ciclo y si no se termina el while: """
        print("¿Deseas ingresar mas tareas?")
        tarea= input()
    return arreglo_tareas
#Fin del while que permite ingresar las tareas en el arreglo de tareas

#Aqui se creo una funcion para mostar las tareas pendientes. 
def mostrar_tareas(tareitas):

    """Se utiliza un ciclo for que se encarga de imprimir los elementos de
    nuestro arreglo el cual contiene las tareas; usamos j como variable de 
    control y definimos que el ciclo recorrera hasta el limite de nuestra lista
    sin embargo, dentro del for tenemos un if que revisa si lo que esta en j es 
    diferente de None y en caso de que si lo imprime."""
    for j in tareitas: 
        if j != None: #!= significa que si j es diferente a None se ejecutara el print
            print (j)
        else: return("No hay tareas registradas por favor ingresa tareas")
        

""" Dentro de esta funcion se eliminaran las tareas que el usuario decida utilizando una variable
contador para ingresar al indice y comparando lo que hay en dicha posicion del arreglo con nuestra
variable tarea_eliminar que almacena el nombre de la tarea que se desea eliminar. Al final del
metodo es se regresa el arreglo y dentro del if del menu mandamos a 
llamar al segundo metodo para imprimir la lista."""
def eliminar_tarea(arreglo_tarea, tarea_eliminar):
    j = 0 
    count = 0
    for j in arreglo_tarea:
        if j == tarea_eliminar:
            del arreglo_tarea[count]
            return arreglo_tarea
        count +=1

"""Mas adelante se planea utilizar un proceso similar pero con nuestro 
arreglo convertido en matriz en donde agregaremos la fecha de entrega y
una breve descripcion de la tarea. Tambien se podra eliminar y modificar
elementos asi mismo cada proceso ira en una funcion con el fin de modular
el proyecto"""

respuesta = 'Si'

"""Se manda a llamar a una funcion dentro de otra, primero el registro y luego 
la lista de las tareas guardadas. """ 

while (respuesta == "Si"):
    op = int(input("Ingresa la opcion correspondiente para el menu: "))
    if op==1: 
        print("Tienes tareas pendientes? 'Si' 'No' ")
        #Esta variable recibe la respuesta del usuario:
        tarea = input() 
        tareitas = ingresar_tareas(tarea)
        
    elif op==2: 
        """En programacion, los try y catch/except se utilizan para
        capturar excepciones, aqui practicamente fue necesario
        porque el metodo de mostrar depende del metodo registrar
        y si tratabamos de mostrar tareas registradas sin que hubiera ninguna
        el programa marca error ya que la lista tareitas no se habia creado.
        
        La diferencia del if y el try es que el try se encarga de capturar
        errores mientras que el if solo se utiliza para la logica de programacion 
        asi como para condiciones. """
        try:
            tareitas
        except NameError:
             print("No hay tareas registradas, por favor dirigete a la opción 1")
        else:
            print("Las tareas son:")
            mostrar_tareas(tareitas)

    if op==3:
        #Este metodo aun no funciona
        print("Que tareita deseas eliminar: ")
        tarea_eli = input()
        try:
            tareitas
        except NameError:
             print("No hay tareas registradas, por favor dirigete a la opción 1")
        else:
            tareitas = eliminar_tarea(tareitas, tarea_eli)
            print("Tus ahora tareas son: ")
            mostrar_tareas(tareitas)
        
    respuesta = input("Deseas continuar dentro del programa: ")