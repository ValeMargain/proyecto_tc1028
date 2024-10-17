# proyecto_tc1028
Organizador de tareas escolares (O.T.E)

El Organizador de Tareas Escolares es una herramienta diseñada para mejorar la gestión académica de los estudiantes. Su objetivo principal es ofrecer un sistema eficiente que permita a los alumnos tener un control total sobre su tiempo y responsabilidades, facilitando la organización de tareas y actividades.

Este software busca aumentar la productividad de los estudiantes al proporcionarles un acceso rápido a sus pendientes, permitiéndoles planificar su día y priorizar tareas según la urgencia y complejidad, basándose en la fecha de inicio y entrega de cada tarea.

Además, OTE ayuda a reducir el estrés al ofrecer una visualización clara de las prioridades, permitiendo que los estudiantes se enfoquen en lo más importante de manera efectiva.

El programa comienza con un menú que funciona como un formulario y calendario, donde el usuario ingresa el nombre de la tarea, su fecha de inicio y la fecha de entrega. Las tareas se almacenan en una lista y, dependiendo de la opción que el usuario elija, pueden ser visualizadas o eliminadas. Para evitar errores comunes como la selección de opciones no válidas el programa utiliza bloques try-except que permiten mandar un mensaje de error sin que se pare el programa. 

La sentencia  try permite probar un bloque de código para detectar errores. En caso de que haya un error el except permite gestionar el error y el else permite ejecutar código cuando no hay ningún error (W3Schools.com, s. f.).

Como característica adicional, OTE incluye una opción para calcular el promedio del usuario, solicitando los valores y criterios de evaluación correspondientes. El programa se ejecuta en la terminal usando Python 3.

Finalmente, con estos funcionamientos OTE pretende ser indispensable en la vida de los estudiantes. 

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

Referencias:
W3Schools.com. (s. f.). https://www.w3schools.com/python/python_try_except.asp


