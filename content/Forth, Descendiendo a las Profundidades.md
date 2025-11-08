Title: Forth, Descendiendo a las Profundidades
Date: 2025-11-06
Modified: 2025-11-07
Category: Artículos
Tags: Aprender, forth, nasmjf
Slug: Echa un vistazo a los engranes de Forth
Author: Yurizan Peres Fernandez
Summary: Un paseo por los detalles de una implementación de Forth

## Que es Forth.
Es un lenguaje de programación orientado a pila.

## La Implementación.
Estaremos analizando la portación a i386 NASM realizado por Dave Gauer de la implementación i386 GNU GAS JonesForth por Richard WM Jones. Puedes descargar los fuentes de [ratfactor.com](https://ratfactor.com/repos/nasmjf){:target="_blank" rel="noreferrer noopener"}. Este repositorio contiene las fuentes originales de JonesForth.

## Como funciona Forth
Más que un lenguaje Forth es un ambiente que integra un interprete, el compilador, el editor y la shell ¡Todo en uno! 

En este ambiente el usuario define y corre subrutinas (funciones), a las que se les llama "palabras". Estas "palabras" pueden ser definidas, usadas, probadas, depuradas y redefinidas a medida que el código fuente es ingresado, sin recompilar o reiniciar.

### El paradigma.
Todo, absolutamente todo en Forth son "palabras". Esto incluye las variables y los operadores básicos. En este articulo se utilizara el termino `palabra` muchas...muchas veces con los dos significados siguientes:

* `palabra` ->  Concepto fundamentar en Forth. 
* palabra ->    concepto gramatical, minima agrupación de caracteres con  significado

### La Pila.
Ya mencionamos que Forth es un lenguaje orientado a la pila ¡tiene dos! La de parámetros y la de retorno. La pil ade retorno se maneja mediante el registro `ebp` y la de parámetros con el registro `esp`

La implicación más obvia de esto es que no se suelen usar variables como en C o Python, ni registros como en ASM. La segunda implicación del uso de pilas es que tenemos que usar la notación polaca. 

Supongamos que queremos sumas dos números "4 + 5".  

En C:
```c
#include <stdio.h>

int main() {
    int a = 4;
    int b = 5;
    int suma = a + b;
    printf("La suma de %d y %d es: %d\n", a, b, suma);
    return 0;
}
```

En Python:
```python
# Programa que suma 4 y 5 y muestra el resultado
a = 4
b = 5
suma = a + b
print("La suma de", a, "y", b, "es:", suma)
```

En Forth:
```forth
4 5 + . 9 ok
```

Expliquemos el código Forth. El literal "4" pone en la pila el valor 4, igual para el 5. El operador "+" toma dos valores del tope te la pila y los suma dejando el resultado en la pila. El operador "." muestra el valor del tope de la pila. El "9" es el resultado mostrado y el "ok" es un indicador de que todo a marchado bien. 

!!! note "Nota"
    Los espacios son fundamentales en la sintaxis de Forth. Como en una oración los espacios separan las palabras. Recuerde en Forth todo son "palabras" 

### Entrando en detalles.
Un sistema Forth se compone de `palabras`. Son como funciones.: Contienen una serie de instrucciones. Estas instrucciones son, en realidad, una lista de referencias a otras `palabras`. Así que son palabras de principio a fin. Bueno, en realidad, no ocurre nada realmente útil hasta que se llega a una de las `palabras` base escritas en código máquina. Estas "palabras clave" son las primitivas de bajo nivel que proporcionan la funcionalidad de "arranque" para todas las demás palabras construidas sobre ellas.

Aunque todo en Forth son "palabras" no todas son iguales. Se pueden encontrar dos tipos de `palabra`:

Primitivas
: Son las "palabras" básicas del lenguaje. Estas están implementadas por el interprete/compilador y su cuerpo contiene código maquina.

Definidas
: Ó de usuario. son "palabras" que define el usuario y su cuerpo constituye una lista de punteros a otras `palabra`. Estas ultimas pueden ser primitivas ó definidas.

Independientemente de que una palabra sea una palabra normal o una palabra de código, tiene la misma estructura básica, todas las palabras tiene un encabezado como el siguiente:

<img src="/static/img/CabeceraPalabras.svg" alt="Imagen de cabecera de palabras" class="svgresaltado" />

El cuerpo de una `palabra` primitiva se ve así.

<img src="/static/img/PrimitivasCuerpoPalabras.svg" alt="Imagen del cuerpo de primitiva" class="svgresaltado" />

Lo cual parece extraño e inútil (¿por qué no empezar a ejecutar el código  máquina directamente?) hasta que vemos una `palabra` definida por el usuario, que no tiene código máquina. Una `palabra` de usuario se ve así:

<img src="/static/img/DefinidasCuerpoPalabras.svg" alt="Cuerpo de una `palabra` de usuario" class="svgresaltado" />

Lo que las "palabras" primitivas y la definidas por el usuarios tienen en común es  que el primer puntero del cuerpo de ambas apunta al  código máquina que se ejecutará. Para las "Palabras" primitivas sera el código maquina que realiza la acción designada. Para las `palabra` de usuario sera, en la mayoría de los casos, DOCOL que se conoce como la *`palabra` primitiva  intérprete*. 

El intérprete ejecuta el resto del `código` de la palabra actual incrementando el puntero de instrucción (esi) y llamando a la macro NEXT. Esto se llama "código enhebrado indirecto" debido al segundo nivel de indirección del puntero. Recuerde el `código` de una `palabra` de usuario es una lista de punteros a otras palabras.

Puede ser útil resumir en este punto:

 | Palabra  | Comienza con | Termina con  | ¿Qué se usa?                    | 
 |:---------|:-------------|:-------------|:--------------------------------| 
 | Definida | Ptr a DOCOL  | EXIT ptr     | esi, memoria principal de datos | 
 | Primitiva| Ptr a código | NEXT macro   | ebp ("RSP"), pila de Retorno    | 
  
 Además, visualicemos el diseño de una `palabra` primitiva y una definida por el usuario, una al lado de la otra.:

 <img src="/static/img/ComparacionCuerpos.svg" alt="Cuerpo de una `palabra` de usuario" class="svgresaltado" />

 En la proxima entrega comenzaremos con el análisis del código. Este articulo y los siguientes comparten la etiqueta #nasmjf 