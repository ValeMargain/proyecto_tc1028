"""Se consulta con el usuario si tiene tareas pendientes para comenzar
con el funcionamiento del programa es decir, determinar si ingresaremos al 
while o saltaremos directamente al for. """

#Ya se muestra el menu :)
print("Menu:")
print("1. Ingresar tareas")
print("2. Mostrar tareas")
print("3. Eliminar tareas")
"""Se declaran dos listas, una que va a guardar las tareas pendientes y la segunda que
guardara la fecha de inicio y fin de cada tarea (se definen como vacias al inicio)"""
arreglo_tareas=[]
arreglo_fechas=[]


"""Comenzamos a separar todo por funciones, dentro de la funcion ingresar_tareas 
haremos el registro de todas las tareas que el usuario desee y regresaremos 
el arreglo final que corresponde al arreglo con todas las tareas y fechas ingresadas."""
def ingresar_tareas(tarea): 
    i = 0 
    """A continuacion se agrega un bucle que solo terminará en caso de
    que el usuario ingrese que 'No' tiene tareas pendientes"""
    while(tarea=="SI"):
        print("Ingresa el nombre de tu tarea")
        """Esta variable guarda temporalmente el nombre de 
        la tarea:"""
        nom_tarea = input() 
        #Se validara que la tarea no exista en el arreglo, solo que aun no funciona
        if(nom_tarea.upper() not in arreglo_tareas):
            arreglo_tareas.append(nom_tarea)
            print("Ingresa la fecha de inicio")
            fecha_ini_tarea = input() 
            print("Ingresa la fecha de fin")
            fecha_fin_tarea = input() 
            #Se valida que la fecha de inicio sea menor o igual a la fecha final
            if(fecha_ini_tarea<=fecha_fin_tarea):
                print("Si se guardo")
                arreglo_fechas.append(fecha_ini_tarea)
                arreglo_fechas.append(fecha_fin_tarea)
            else:
                """En caso de que no se cumpla la condicion anterior ingresaremos al ciclo
                while que se repetira hasta que se ingresen correctamente las fechas. 
                """
                while fecha_ini_tarea>fecha_fin_tarea:
                    print("No se guardo, intenta con otra fecha:")
                    print("Ingresa la fecha de inicio")
                    fecha_ini_tarea = input() 
                    print("Ingresa la fecha de fin")
                    fecha_fin_tarea = input() 
                print("Fechas correctas, se fuardo :)")
                arreglo_fechas.append(fecha_ini_tarea)
                arreglo_fechas.append(fecha_fin_tarea)
        else:
            print("La tarea ya existe")
        """Usamos el operador de suma para que en cada vuelta del while
        la variable i aumente 1 y se vayan agegando las tareas al indice
        correspondiente del arreglo"""
        #Variable de control para nuestro while:
        i = i + 1 
        """Preguntamos al usuario si desea agregar mas tareas, en caso de que si
        repetimos el ciclo y si no se termina el while: """
        print("¿Deseas ingresar mas tareas?")
        """Usamos el metodo upper para que si el usuario ingresa si, Si, sI o SI se
          tome como valida la opcion """
        tarea= input().upper()
        """Creamos un arreglo que contenga los arreglos anteriores. 
        """
    arreglo_final = [arreglo_tareas,arreglo_fechas]
    return arreglo_final
#Fin del while que permite ingresar las tareas en el arreglo de tareas

#Aqui se creo una funcion para mostar las tareas pendientes. 
def mostrar_tareas(tareitas):

    """Se utiliza un ciclo for que se encarga de imprimir los elementos de
    nuestro arreglo el cual contiene las tareas y sus fechas; usamos i como variable de 
    control y definimos que el ciclo recorrera hasta el limite de nuestra lista
    sin embargo, dentro del for tenemos un if que revisa si i es menor a la longitud del arreglo en la poscion
    1 entre la longitud el msimo arreglo en la posicion 0. Esto para aregurarnos de que las fechas
    sean proporcionales a las tareas. En caso de que la condicion se cumpla imprimimos las fechas (es decir, tareitas[1]) 
    en dos elementos consecutivos, debido a que nuestra tarea  tiene fecha de inicio y fin.  """
    for i in range(len(tareitas[0])):  
        print([tareitas[0][i]])
        if i < len(tareitas[1]) // len(tareitas[0]):  
            print(tareitas[1][i * 2:(i + 1) * 2]) 
    else: return("No hay tareas registradas por favor ingresa tareas")
        

""" Dentro de esta funcion se eliminaran las tareas que el usuario decida utilizando un 
condicional if para validar si lo que registro el usuario se encuentra dentro de nuestro 
arreglo, pero unicamente en la poscion 0 porque es la que corresponde al nombre de la tarea
En caso de que la condicion se cumpla, la guardamos dentro de una variable llamada pos y 
utilizamos el metodo 'del' que se encarga de eliminar un elemento de un arreglo
en base a la posicion indicada. Una vez eliminado el nombre de la tarea, eliminamos
las fechas que le corresponden mediante una multiplicacion para determinar la posicion o indice
inicial dentro de la posicion [1] de nuestro arreglo y tenemos la posicion obtenida + 1 
y multiplicado por dos para obtener la posicion final.  """
def eliminar_tarea(arreglo_tarea, tarea_eliminar):
    if tarea_eliminar in arreglo_tarea[0]:
        pos = arreglo_tarea[0].index(tarea_eliminar)
        del tareitas[0][pos]  
        del tareitas[1][pos * 2:(pos + 1) * 2]
        print("Tarea eliminada")
        return tareitas
    else:
        print("No se encontro la tarea")
        return tareitas
"""Mas adelante se planea utilizar un proceso similar pero con nuestro 
arreglo convertido en matriz en donde agregaremos la fecha de entrega y
una breve descripcion de la tarea. Tambien se podra eliminar y modificar
elementos asi mismo cada proceso ira en una funcion con el fin de modular
el proyecto"""

respuesta = 'SI'

"""Se manda a llamar a una funcion dentro de otra, primero el registro y luego 
la lista de las tareas guardadas. """ 

while (respuesta == "SI"):
    op = int(input("Ingresa la opcion correspondiente para el menu: "))
    if op==1: 
        print("Tienes tareas pendientes? 'Si' 'No' ")
        #Esta variable recibe la respuesta del usuario:
        tarea = input().upper() 
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
        
    respuesta = input("Deseas continuar dentro del programa: ").upper()