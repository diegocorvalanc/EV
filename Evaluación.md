# Problema de código en Foris

Para el siguiente paso en el proceso, nos gustaría ver cómo programas. Somos conscientes del tiempo, así que tratamos de mantener el tamaño del problema al mínimo posible.

Buscamos una solución que sea representativa del código que tendrías que escribir en un proyecto real, incluyendo el uso de testing. Puedes completar el problema en el tiempo que más te acomode, pero no debería tomar más de un par de horas. Para esta entrevista en particular debes utilizar el lenguaje de programación Python, pero el uso o no uso de frameworks queda a tu elección.

Si tienes alguna pregunta puedes mandar un correo a angel.maturana@foris.cl. Si el problema no especifica algo, eres libre de tomar la decisión que prefieras. Tu código _no será_ evaluado en su capacidad de manejar algo que no haya sido mencionado aquí.

Finalmente, la entrega debe incluir un README donde nos cuentes cómo abordaste el problema.

## Problema

### Descripción

Buscamos detectar a los estudiantes que más asisten a clases.

El código procesará un archivo de entrada. Puedes elegir si aceptar el input a través de la entrada estándar (e.g. si usaras Python: `cat input.txt | python yourcode.py`) o como un nombre de archivo entregado como parámetro (e.g. `python yourcode.py input.txt`).

Cada línea del archivo de entrada empieza con un comando. Hay dos comandos posibles.

El primero es `Student`, que registra el nombre de un nuevo estudiante en la aplicación. Ejemplo:

```
Student Matthias
```

El segundo comando es `Presence`, que registra la presencia/asistencia de un estudiante en la universidad. Esta línea tiene los siguientes datos separados por espacios:

- el comando (`Presence`)
- el nombre del estudiante
- el día de la semana
- la hora inicial de detección
- la hora final de detección
- el código de la sala en la que se realizó la detección

Observaciones:

- Los días de la semana van de 1 a 7
- Los tiempos se entregan en formato HH:MM, usando un reloj de 24 horas.
- También se asume que ningún estudiante se queda en la universidad después de media noche (es decir, la hora de inicio siempre será anterior a la hora de fin).

Ejemplo:

```
Presence Matthias 2 09:04 10:35 F100
```

Esto indica que Matthias estuvo en la sala F100 el día martes desde las 9:04 hasta las 10:35.

### Objetivo

Genera un reporte que liste cada estudiante con el total de minutos registrados y la cantidad de días que asistió a la universidad. Ordena el resultado por la cantidad de minutos de mayor a menor.

Descarta cualquier registro que indique presencias menores a 5 minutos.

Ejemplo de entrada:

```
Student Marco
Student David
Student Fran
Presence Marco 1 09:02 10:17 R100
Presence Marco 3 10:58 12:05 R205
Presence David 5 14:02 15:46 F505
```

Ejemplo de salida:

```
Marco: 142 minutes in 2 days
David: 104 minutes in 1 day
Fran: 0 minutes
```

## Expectativas y Criterios de Evaluación

Como ingenieros de software, sabemos que hay muchas soluciones para cualquier problema. Aunque entregamos un problema relativamente sencillo de resolver, buscamos que implementes suficiente código como para demostrar tu habilidad, en especial en cuanto a modelamiento y a testing.

Nos interesa el razonamiento detrás de tus decisiones, por lo que te pedimos tomarte un tiempo para capturarlo en el README. No consideramos que una opción de implementación sea necesariamente mejor que las otras. Por ejemplo, para representar tus datos podrías usar tipos primitivos, estructuras u objetos. Sin embargo, esperamos que puedas tomar una decisión intencional, implementarla consistentemente y comunicar en el README (en formato libre) por qué elegiste ese acercamiento.

Evaluaremos las soluciones basándonos en los siguientes criterios:

- Modelamiento del problema y estructura del código
- Uso de expresiones típicas (_idioms_) y prácticas propias del lenguaje utilizado (PEP 8)
- Enfoque al testing
- Razonamiento detrás de las decisiones en el README

En resumen, lo que más nos interesa es que entiendas el problema y seas capas de plasmar ese entendimiento tanto en tu código como en la siguiente etapa de nuestra entrevista, la cual consiste en que nos expliques tu solución.

## Envío

Mándanos tu código como un comprimido o como un gitbundle. Para evitar problemas con GMail (el servicio de correo que usamos), recomendamos usar gitbundle, pero si prefieres mandar un comprimido (`.tgz`), cámbiale la extensión a algo distinto (por ejemplo `your-code.tarball`). Sabemos que GMail filtra los comprimidos adjuntos que contengan archivos `.jar` o `.js`, por lo que el cambio de extensión es necesario en esos casos.

Acá unos comandos útiles para comprimir:

- tar: `tar zcvf your-code.tgz your-code-dir`
- gitbundle: `GIT_DIR=your-code-dir/.git git bundle create your-code.gitbundle --all`
