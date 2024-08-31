"""Se consulta con el usuario si tiene tareas pendientes para comenzar
con el funcionamiento del programa es decir, determinar si inresaremos al 
while o saltaremos directamente al for. """

print("Tienes tareas pendientes? 'Si' 'No' ")
#Esta variable recibe la respuesta del usuario:
tarea= input() 




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
def mostrar_tareas(arreglo_tareas):
    print("Tus tareas para hoy son: ")
    """Se utiliza un ciclo for que se encarga de imprimir los elementos de
    nuestro arreglo el cual contiene las tareas; usamos j como variable de 
    control y definimos que el ciclo recorrera hasta el limite de nuestra lista
    sin embargo, dentro del for tenemos un if que revisa si lo que esta en j es 
    diferente de None y en caso de que si lo imprime."""
    for j in arreglo_tareas: 
        if j != None: #!= significa que si j es diferente a None se ejecutara el print
            print (j)

# Dentro de esta funcion se eliminaran las tareas que el usuario decida (aun le faltan detalles)
def eliminar_tarea(arreglo_tarea, tarea_eliminar):
    j = 0 
    for j in arreglo_tareas: 
        if j == tarea_eliminar:
            arreglo_tarea[j] = None
            return arreglo_tareas
      
    

"""Mas adelante se planea utilizar un proceso similar pero con nuestro 
arreglo convertido en matriz en donde agregaremos la fecha de entrega y
una breve descripcion de la tarea. Tambien se podra eliminar y modificar
elementos asi mismo cada proceso ira en una funcion con el fin de modular
el proyecto"""

"""Se manda a llamar a una funcion dentro de otra, primero el registro y luego 
la lista de las tareas guardadas. """ 
mostrar_tareas(ingresar_tareas(tarea))



