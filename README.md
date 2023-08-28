## Instrucciones ##

Para poder ejecutar el archivo my_code.py, es necesario agregar el argumento del nombre del archivo en la línea de comandos.

python my_code.py input.txt

## Primeros Pensamientos ##
Una vez leído el problema, se identifican claramente los objetivos de este proyecto. Estos objetivos eran:

    - Mostrar el nombre del Estudiante
    - Mostrar la cantidad de minutos de asistencia a clases
    - Mostrar la cantidad de días en que el estudiante asistió

Una vez identificados estos, comencé a codificar.

## Codificación ##
1.- Función "main()", la cual será la primera en ejecutarse y solo contendría el llamado de las funciones y la variable args.


2.- Función "load_data()", la cual en un principio no recibía parámetros. Esta función crea un diccionario llamado "student_record", el cual se encarga de guardar la información de los estudiantes (key) y sus asistencias. Este diccionario fue pensado para tener la siguiente estructura:

```python
student_record = {
    "Pedro": {
        "attendances": [(1, "11:00", "12:00"), (1, "13:00", "14:00")] # (día, hora de inicio, hora de fin)
    },
    "Juan": {
        "attendances": [(2, "11:00", "12:00"), (4, "11:00", "12:00")] # (día, hora de inicio, hora de fin)
    }
}
```

Esta estructura tiene como fin que cada estudiante contenga otro diccionario dentro de sí para guardar la información relevante y así poder ser mas facil de modificar o de agregar atributos.


3.- Función "process_data(a)": Encargada de procesar la data. Esta recibe el diccionario previamente creado para trabajar sobre él. Esta función inicia creando otro diccionario llamado "result = {}", el cual será retornado una vez que el proceso termine. Uno de los principales objetivos de esta función es:

Calcular los minutos totales de clases: Para resolver este objetivo, se creó una función específica para eso, la función "time_to_minutes(a, b)". Por temas de orden, esta función será explicada en el siguiente punto.

Calcular la cantidad de días de asistencia identificando que sean días únicos: Para resolver este problema, se utilizó la función set(), la cual crea un conjunto de datos que no se repiten entre sí. Esta función era necesaria ya que existen casos en que un estudiante asiste a más de una clase en el mismo día. Por ende, se creó una variable "unique_days" como un "conjunto de datos set()". Una vez que el código filtró todos los casos excepcionales, como por ejemplo, que los días tenían que estar en el rango 1 a 7 y que el estudiante debía asistir más de 5 minutos a la clase para que esta sea contabilizada, se agregaba el día recorrido por dicho "for" con el comando "unique_days.add(day)".

Este diccionario "result" cuenta con la siguiente estructura una vez procesado los datos:

```python
result = {
    "Pedro": {
        "total_minutes": 150,
        "unique_days": {1}
    },
    "Juan": {
        "total_minutes": 190,
        "unique_days": {2, 4}
    }
}
```

Este diccionario es de estructura similar al anterior (student_record) con la diferencia de que este contiene los ítems "total_minutes", que almacena la cantidad de minutos que el estudiante asistió, y "unique_days", que almacena los días de la semana a los cuales el estudiante asistió a clases.

Al finalizar la función, esta retorna el diccionario "result".


4.- Función "time_to_minutes(a, b)": Esta función recibe dos strings de hora que contiene el documento, la hora de inicio y la hora de fin. Una vez recibidos, utilizando la librería "datetime", la función identifica si el formato del string es el esperado ("HH:MM"). Si el formato es válido, utilizando la función ".strptime(a, format)", se separan las horas y los minutos y se almacenan en dos variables, start_time y end_time. Finalmente, para obtener la cantidad de minutos, se realiza una operación matemática que consiste en transformar las horas a minutos y luego restar el resultado del tiempo final menos el tiempo de inicio. Dicha operación se almacena en la variable "minutes", la cual es retornada al final de la función.


5.- Función "report(a)": Encargada de imprimir los resultados y ordenarlos de manera descendente. Para lograr dicho ordenamiento, se utiliza la función "sorted(a, b)", que recibe el argumento que se quiere ordenar (a) y una key (b) que indica cómo se quieren ordenar los datos. Se utiliza una función lambda para ordenar los resultados por la cantidad de minutos y la variable "reverse=True" para asegurar que el ordenamiento se haga de manera descendente. El formato de cómo se imprimirán los datos es el siguiente:

Juan: 190 minutes in 2 days
Pedro: 150 minutes in 1 day


6.- Función "store_results(a)": Su objetivo es guardar los resultados de manera estructurada en un archivo JSON. Para esto, es necesario importar la librería "JSON". Dentro de esta función, se tuvieron que reemplazar las tuplas por listas ya que JSON no es compatible con tuplas. El formato dentro del JSON quedaría de la siguiente manera:

```json
{
  "Pedro": { "total_minutes": 150, "unique_days": [1]},
  "Juan": { "total_minutes": 190, "unique_days": [2,4]}
}
```

7.- Función "parse_arguments()": Su objetivo es parsear el argumento ingresado a través de la línea de comandos. Es necesario importar la librería "argparse".

## Enfoque al Testing ##
El testing en Python utiliza una librería llamada "unittest", la cual ayudará a realizar pruebas automatizadas a las funciones.
El testing fue implementado para dos funciones del archivo my_code.py.

Todos los testing están dentro del archivo testing.py. Dicho archivo contiene la un "unittest.main()" para diferenciarlo del "main()" común

```python
if __name__ == "__main__":
    unittest.main()
```

Las dos funciones seleccionadas para testear son "time_to_minutes" y "process_data".
Para realizar esto, es necesario importar el archivo donde se encuentran declaradas estas funciones junto al nombre del a función.

Todas las funciones de testing están dentro de la clase "test_my_code(a)":

1.- Prueba para "time_to_minutes()": La prueba está focalizada en el formato de la hora entregada y la conversión a enteros del resultado final. Por ende, utilicé un caso real con el formato correcto "minutes = time_to_minutes("09:00", "12:30")" y lo comparé utilizando la función "assertEqual(r, e)" donde como segundo parámetro le envié el valor esperado que debería tener la función.

La segunda parte de la función está focalizada en validar el formato. En caso de no recibir la hora en el formato esperado, se informará un error.

2.- Prueba para "process_data()": Esta prueba toma el diccionario de datos de asistencia de estudiantes y realiza cálculos sobre ellos. Esto con el fin de que la función calcule correctamente los minutos y días únicos, y compararlos con una variable que contenga el resultado esperado.

En la segunda parte, "data_no_attendances", se proporciona un diccionario de datos que contiene un estudiante sin asistencias. Se verifica que la función maneje adecuadamente este caso y devuelva la cantidad de minutos 0 y un conjunto de datos vacío.


## -- ## 
