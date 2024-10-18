"""Sub competencia: Operadores aritmeticos de manera eficaz
    Error original: No habia hecho uso de operaciones aritmeticas
    Cambio realizado: Se creo la funcion calcular_promedios que corresponde
    a la opcion 4 del menu
    Lineas de codigo donde se ve la corrección: 164-215"""
     
"""Proyecto Python
    Organizador de tareas escolares.
    El programa realiza una serie de funciones mediante un menu
    las cuales le permite al usuario llevar control de sus tareas 
    pendientes asi mismo puede calcular el promedio en base a los
    criterios que el escoja.
"""

#Opciones del menu
print("Menu:")
print("1. Ingresar tareas")
print("2. Mostrar tareas")
print("3. Eliminar tareas")
print("4. Calcular promedio")


"""------Funciones auxiliares relacionadas con las fechas------"""
def valida_fecha(dia, mes, year):
    """
    (uso de operadores boleanos, uso de funciones, uso de anidación condiciones)
    recibe: dia valor numérico, mes valor numérico, year valor numérico
    Es una funcion auxiliar que valida el formato de la fecha
    devuelve: Un valor booleano. 
    """
    bol= True
    if dia > 31 or dia<1: 
        bol= False
    elif mes>12 or mes<1:
        bol= False
    elif year>2024 or year<2024:
        bol= False
    return bol

def llenar_fecha():
    """
    (uso de condicionales, uso de funciones, uso de ciclo while, 
    uso de manipulación de cadenas)
    recibe: no recibe nada
    Es una funcion auxiliar que hace el registro de las fechas siempre 
    y cuando sean correctas, de lo contrario se pediran nuevamente. 
    devuelve: dia un valor entero, mes un valor entero, cadena_Fecha una cadena

    """
    dia = 0
    mes = 0 
    year = 0
    i = 0
    while valida_fecha(dia, mes, year) == False:
        if i >0:
            print("Registra las fechas nuevamente, los calores no son validos")
        print("Ingresa el dia (01-31)")
        dia=int(input())
        print("Ingresa el mes (01-12)")
        mes=int(input())
        print("Ingresa el año (2024)")
        year=int(input())
        i=i+1
    cadena_Fecha= f"{dia}/{mes}/{year}"
    return dia, mes, cadena_Fecha

def compara_fechas(dia_I, mes_I,dia_F, mes_F ):
    """
    (uso de condicionales, uso de funciones, uso de anidacion de condiciones, 
    uso de operadores booleanos).
    recibe: dia_I un valor entero, mes_I un valor entero, dia_F un valor
            entero, mes_F un valor entero.
    Es una función que valida que la fecha de fin sea mayor a la fecha 
    de inicio mediante los meses y dias correspondientes a cada fecha.   
    devuelve: un valor booleano.

    """
    if mes_F > mes_I:
     return True
    elif mes_F == mes_I:
        if dia_I > dia_F:
            return False
        else: return True
    else: return False
"""--------Funciones principales/Opciones del menú-------""" 
def ingresar_tareas(tarea):
    """ 
    (uso de ciclos while, uso de funciones, uso de arreglos,
    uso de condicionales, manejo de cadenas, uso de operadores boleanos)
    recibe: tarea que es una cadena
    Dentro de esta funcion se registran las tareas: nombre, fecha de inicio
    y fin. Asi mismo, valida que la tarea no exista y asi mismo con 
    ayuda de las funciones auxiliares se valida la fecha. 
    devuelve: un arreglo con los nombres y fechas de las tareas
    """
    arreglo_fechas=[]
    arreglo_tareas=[]
    i = 0 
    while(tarea=="SI"):
        print("Ingresa el nombre de tu tarea")
        nom_tarea = input() 
        if(nom_tarea.upper() not in arreglo_tareas):
            arreglo_tareas.append(nom_tarea.upper())
            print("Ingresa la fecha de Inicio")
            dia_I, mes_I, cadena_Fecha_I = llenar_fecha()
            print("Ingresa la fecha de fin")
            dia_F, mes_F,cadena_Fecha_F =llenar_fecha()
            while compara_fechas(dia_I, mes_I,dia_F, mes_F) == False:
                print("La fecha de fin no puede ser menor a la de inicio")
                print("Ingresa nuevamente la fecha de Inicio")
                cadena_Fecha_I= llenar_fecha()
                print("Ingresa nuevamente la fecha de fin")
                cadena_Fecha_F =llenar_fecha()
            print("Si se guardo")
            arreglo_fechas.append(cadena_Fecha_I)
            arreglo_fechas.append(cadena_Fecha_F)
        else:
            print("La tarea ya existe")
        i = i + 1 
        print("¿Deseas ingresar mas tareas? 'Si' 'No'")
        tarea= input().upper() 
    arreglo_final = [arreglo_tareas,arreglo_fechas]
    return arreglo_final
 
def mostrar_tareas(tareitas):
    """ 
    (uso de ciclos for, uso de funciones, uso de arreglos,
    uso de condicionales, uso de operadores boleanos)
    recibe: tareitas que es una matriz
    Imprime la matriz tareitas y revisamos que las fechas sean 
    proporcionales a las tareas, de ese modo se distingue que fechas 
    corresponden a que tareas.
    devuelve: muestra la matriz de las tareas y sus fechas o un
    mensaje en caso de que no haya tareas que mostrar.
    """
    for i in range(len(tareitas[0])):  
        print([tareitas[0][i]])
        if i < len(tareitas[1]) // len(tareitas[0]):  
            print(tareitas[1][i * 2:(i + 1) * 2]) 
        else: return("No hay tareas registradas por favor ingresa tareas")
        
def eliminar_tarea(arreglo_tarea, tarea_eliminar):
    """ 
    (uso de funciones, uso de arreglos,
    uso de condicionales, uso de operadores boleanos)
    recibe: arreglo_tarea que es una matriz y tarea_eliminar
            que es una cadena.
    Revisa si el nombre de la tarea que ingreso el usuario se 
    encuentra en el arreglo de las tareas y la borra junto con 
    su fecha, en caso de que no hayan coincidencias le informa al 
    usuario. 
    devuelve: matriz tareitas. 
    """
    if tarea_eliminar in arreglo_tarea[0]:
        pos = arreglo_tarea[0].index(tarea_eliminar)
        del tareitas[0][pos]  
        del tareitas[1][pos * 2:(pos + 1) * 2]
        print("Tarea eliminada")
        return tareitas
    else:
        print("No se encontro la tarea")
        return tareitas

def calcular_promedios(criterios):
    """ 
    (uso de funciones, uso de arreglos, ciclos while anidados,
    uso de condicionales, uso de operadores boleanos, 
    uso de operadores aritmeticos)
    recibe: criterios valor entero.
    En esta función se en carga de registrar los nombres, valores 
    actividades de cada criterio de evaluación. Calcula el promedio
    de cada criterio en base al valor que se le haya asignado y al 
    final da el promedio final. 
    devuelve: el arreglo arre_noms y prom que es float.
    """
    i=0
    res = 0
    arre_nom_cri=[]
    prom=0
    suma_val=0
    arre_noms= []
    while i <criterios:
        nom_cri=input("Ingresa el nombre del criterio: ")
        arre_nom_cri.append(nom_cri)
        bol= True
        while bol == True:
            val = int(input("Ingresa el valor del criterio (0-100): "))
            if val == 100:
                i = criterios
                bol = False
            elif val < 0 or val > 100:
                print("Valor fuera de rango. Escribe de nuevo el valor: ")
            elif suma_val + val > 100  :
                print("La suma de los valores no puede ser mayor a 100,"
                       +"intenta de nuevo.")
            else:
                suma_val += val
                bol = False
        acts = int(input("Cuantas actividades tiene tu criterio: "))
        j=0
        suma_cal=0
        while j < acts:
            cal=float(input("Ingresa la calificacion de tu actividad (0-100): "))
            while cal >100 or val <0:
                print("Escribe de nuevo el valor: (0-100) ")
                cal=int(input())
            suma_cal+=cal
            j=j+1
        res=suma_cal/acts
        res = res*val
        res= res/100
        prom+=res
        i=i+1
        arre_noms.append(arre_nom_cri)
    return arre_noms, prom

"""------------Parte principal del programa-----------"""

#Inicializa la variable respuesta
respuesta = 'SI'

#Se programa el menú
while (respuesta == "SI"):
    op = int(input("Ingresa la opcion correspondiente para el menu: "))
    if op==1: 
        print("Tienes tareas pendientes? 'Si' 'No' ")
        #Esta variable recibe la respuesta del usuario:
        tarea = input().upper() 
        tareitas = ingresar_tareas(tarea)

    if op==2: 
        #Se valida que el arreglo tareitas exista
        try:
            tareitas
        except NameError:
            print("No hay tareas registradas, por favor dirigete a la opción 1")
        else:
            #Se muestran las tareas registradas
            print("Las tareas son:")
            mostrar_tareas(tareitas)

    if op==3:
        print("Que tareita deseas eliminar: ")
        tarea_eli = input()
        #Validar que el arreglo exista
        try:
            tareitas
        except NameError:
            print("No hay tareas registradas, por favor dirigete a la opción 1")
        else:
            #Eliminar la tarea
            tareitas = eliminar_tarea(tareitas, tarea_eli)
            print("Tus ahora tareas son: ")
            mostrar_tareas(tareitas)

    if op==4:
        criterios=int(input("Ingresa la cantidad de criterios que tienes: "))
        print("A continuacion, se le solicitaran los criterios"+
            "en caso de que el valor total de los criterios sea"+
             "mayor a 100,se volvera a pedir toda la información")
        arre_cri= [calcular_promedios(criterios)]
        arre_nom=arre_cri[0]
        prom=arre_cri[0][1]
        print("Tus criterios de evaluacion son: ", arre_nom)
        print("Tu promedio es: ",prom)
    if op !=1 and op !=2 and op !=3 and op !=4:
            print("Opcion no valida")
respuesta = input("Deseas continuar dentro del programa 'Si' 'No': ").upper()