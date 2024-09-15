# EL4203: Programación Avanzada - Tarea 1
## Preguntas teóricas
- **¿Qué es un paradigma de programación?**

  Un paradigma de programación es un enfoque para escribir programas que define cómo se diseñan, estructuran y escriben las instrucciones. Cada paradigma guía de forma única el como se debe abordar y resolver los problemas en el código. La elección del paradigma correcto permite desarrollar un proyecto de forma más versátil y efectivo, siendo esto fundamental para el éxito. 

- **¿En qué se basa la programación orientada a objetos?**

  La programación orientada a objetos es un paradigma de programación que proporciona unas guías acerca de cómo trabajar con él y que se basa en el concepto de clases y objetos. Los objetos son instancias de clases que encapsulan tanto datos como métodos. Este enfoque se basa en conceptos como la encapsulación, la herencia y el polimorfismo.

- **¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big 𝑂?**
  
  Recursividad e iteración son dos técnicas que permiten repetir operaciones en un algoritmo, pero funcionan de maneras diferentes. Se le llama recursividad cuando una función se llama a sí misma para resolver un problema, cada recursión resuelve una parte más pequeña del problema hasta llegar al caso base. Por otro lado, se llama iteración al uso de bucles como `for` y `while` para repetir un bloque de codigo hasta que se cumpla una condición.

  En relación a la notación big 𝑂 se tiene que la recursividad posee generalmente una mayor complejidad que la iteración. Esto se debe a que esta última evita el uso de la pila de llamadas y resuelve cada subproblema una sola vez. Mientras que la recursividad realiza llamadas a funciones y recalcula los mismos problemas varias veces.

- **Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)**

  `𝑂(1)` significa que el tiempo de ejecución es constante, es decir, no depende del tamaño de la entrada. Mientras que `𝑂(n)` significa que el tiempo de ejecución de un algoritmo aumenta linealmente con el tamaño de la entrada. Por lo que si se utilizan entradas grandes, un algoritmo `𝑂(n)` será mucho más lento que uno `𝑂(1)`.

- **¿Cómo se calcula el orden en un programa que funciona por etapas?**

  Para calcular el orden en un programa que funciona por etapas, se debe analizar cómo cambia el número de operaciones necesarias según el tamaño de entrada. Por lo que se debe identificar las operaciones principales del algoritmo, contabilizar cuántas veces se repiten estas para diferentes tamaños de entradas y por último determinar como esto varía.

- **¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?**
  
  Para determinar la complejidad de un algoritmo recursivo se debe definir cómo el problema se descompone en subproblemas y cuánto trabajo adicional se realiza. Luego de esto se pueden utilizar métodos como el Teorema Maestro para obtener la solución, que dará la complejidad final.
  

## ¿Cómo obtener los resultados de la cantidad de caminos y el tiempo de ejecución con el código?

Primero se debe crear una instancia de la clase `Caminos`, especificando el tamaño de la grilla deseada, siendo los parametros el ancho y el largo de esta.

Luego para obtener el número de caminos y el tiempo de ejecución del método de solución deseado se debe utilizar la función `calcular_caminos(metodo)` a la cual se le aplicó un decorador definido anteriormente. El input de `calcular_caminos(metodo)` es el método con el que se calcula el número de caminos, por lo que este puede ser 'recursivo' o 'iterativo'.

Cuando se llama `calcular_caminos(metodo)`, se obtienen dos valores de forma tupla:
- El número total de caminos
- El tiempo que tomó calcular el número de los caminos

Por ejemplo, si se crea la instancia `pcb = Caminos(3,3)` se debe obtener los resultados de la siguiente forma:

```python
rec, tiempo_rec = pcb.calcular_caminos('recursivo')  # Para la solución recursiva
it, tiempo_it = pcb.calcular_caminos('iterativo')  # Para la solución iterativa
```
Donde:
- rec y it contienen el número de caminos
- tiempo_rec y tiempo_it contienen el tiempo de ejecución de cada método

