# proyecto_tc1028
Organizador de tareas escolares (O.T.E)

El Organizador de Tareas Escolares es una herramienta diseñada para mejorar la gestión académica de los estudiantes. Su objetivo principal es ofrecer un sistema eficiente que permita a los alumnos tener un control total sobre su tiempo y responsabilidades, facilitando la organización de tareas y actividades.

Este software busca aumentar la productividad de los estudiantes al proporcionarles un acceso rápido a sus pendientes, permitiéndoles planificar su día y priorizar tareas según la urgencia y complejidad, basándose en la fecha de entrega y la descripción de cada actividad. 

Además, OTE ayuda a reducir el estrés al ofrecer una visualización clara de las prioridades, permitiendo que los estudiantes se enfoquen en lo más importante de manera efectiva.

El programa funciona como un formulario y calendario en el que el usuario ingresa el nombre de la tarea, su descripción, la materia correspondiente y la fecha de entrega. Las tareas se almacenan en una lista, donde pueden ser modificadas, marcadas como finalizadas, o eliminadas según sea necesario. También permite ver una lista completa de tareas pendientes. El programa corre en terminal Python 3.

El algoritmo del proyecto es algo parecido a lo que se muestra a continuación: 

Proceso tareas_diarias (tarea, nomtarea)
    Escribir "Tienes tareas pendientes, escribe si o no"
    Definir respuesta Como Cadena
    Leer tarea
    
    Definir arreglo Como Cadena
	Dimension arreglo[100] 
    Definir indice Como Entero
    indice = 1  
    
    Mientras respuesta = "si" Hacer
        Escribir "Ingresa el nombre de la tarea"
        Definir nomTarea Como Cadena
        Leer nomTarea
        
        arreglo[indice] = nomTarea
        indice = indice + 1  
        
        Escribir "¿Tienes más tareas pendientes? escribe si o no"
        Leer respuesta
    FinMientras
    
    Escribir "Tus tareas para hoy son:"
	Definir i Como Entero
    Para i = 1 Hasta indice - 1 Con Paso 1 Hacer
        Escribir arreglo[i]
    FinPara
    
FinProceso
