Title: Forth, Descendiendo a las Profundidades
Date: 2025-11-06
Modified: 2025-11-06
Category: Artículos
Tags: Aprender, Forth
Slug: Echa un vistazo a los engranes de Forth
Author: Yurizan Peres Fernandez
Summary: Un paseo por los detalles de una implementación de Forth

## Que es Forth.
Es un lenguaje de programación orientado a pila.

## La Implementación.
Estaremos analizando la portación a i386 NASM realizado por Dave Gauer de la implementación i386 GNU GAS JonesForth por Richard WM Jones. Puedes descargar los fuentes de [ratfactor.com](https://ratfactor.com/repos/nasmjf){:target="_blank" rel="noreferrer noopener"}
. Este repositorio contiene las fuentes originales de JonesForth.

## Como funciona Forth
Más que un lenguaje Forth es un ambiente que integra un interprete, el compilador, el editor y la shell ¡Todo en uno! 

En este ambiente el usuario define y corre subrutinas (funciones), a las que se les llama "palabras". Estas "palabras" pueden ser definidas, usadas, probadas, depuradas y redefinidas a medida que el código fuente es ingresado, sin recompilar o reiniciar.

### El paradigma.
Todo, absolutamente todo en Forth son "palabras". Esto incluye las variables y los operadores básicos. En este articulo se utilizara el termino "palabra" muchas...muchas veces con los dos significados siguientes:

* "palabra" ->  Concepto fundamentar en Forth. 
* palabra ->    concepto gramatical, minima agrupación de caracteres con  significado

### La Pila.
Ya mencionamos que Forth es un lenguaje orientado a la pila ¡tiene dos! La de parámetros y la de retorno. La implicación más obvia de esto es que no se suelen usar variables como en C o Python, ni registros como en ASM. La segunda implicación del uso de pilas es que tenemos que usar la notación polaca. 

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

Expliquemos el código Forth. El literal "4" pone en la pila el valor 4, igual para el 5. El operador "+" toma dos valores del tope te la pila y los suma dejando el resultado en la pila. El operador "." muestra el valor del tope de la pila. El "9" es el resultado mostrado y el "ok" es un indicador de que todo a marchado bien. Note que los espacios son fundamentales en la sintaxis de Forth. Como en una oración los espacios separan las palabras. Recuerde en Forth todo son "palabras"

### 

Aquí quiero mostrar datos desde la API:

<solicitud>
{
    "method": "POST",
    "url": "https://jsonplaceholder.typicode.com/posts",
    "headers": {
        "Content-Type": "application/json; charset=UTF-8"
    },
    "body": {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
}
</solicitud>


