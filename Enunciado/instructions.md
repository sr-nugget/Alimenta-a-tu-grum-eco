## Introducción

Ha pasado tiempo desde tus ultimas aventuras, y es hora de retomar tu trabajo como reportero. Tu ex jefe te mando información sobre una extraña isla, en esta  la cual quiere que sea su proxima noticia. Al ir llegando a la isla algo extraño sucede en la nave y te estrellas en una extraña aldea. Sus habitantes no son agresivos y se dicen llamar grumñecos. Dicen que tienen mucha hambre y tu deber es alimentarlos con unos seres llamados bichosnacks (insectos que tienen forma de comida del mundo del que vienes). Cuando consumen uno de estos bichosnacks, les cambia una parte del cuerpo a selección y se reemplaza por el alimento que representa el bichosnack.

## Objetivo

Se te entregaran 3 inputs:

1. El nombre del grumñeco al cual alimentarás (str).
2. Un str separado por comas con las formas de las partes del cuerpo actuales en el siguiente orden: "cabeza,brazo izquierdo,brazo derecho,pierna izquierda,pierna derecha".
3. Un str separado por comas con el bichosnack que consume, la parte que cambiará y el alimento que representa, en el formato: "bichosnack,parte_que_cambia,alimento".

Lo que deberas hacer es:

1. Imprimir el mensaje de alimentación con la siguiente estructura:
"[grumñeco] comio un(a) [bichosnack] y su [parte_que_cambia] ahora es un(a) [alimento]"
2. Imprimir el estado final de cada parte del cuerpo en el orden dado:
Si la parte no cambió y dice "Normal", debes imprimir:" Su [parte_del_cuerpo] sigue igual"
En caso contrario, debes imprimir: "Su [parte_del_cuerpo] es un(a) [alimento]"
## Ejemplo

#### Input
```py
    Gumno   
    Papa frita,Normal,Cafe,Nugget,Normal
    Big Buger,brazo izquierdo,Hamburguesa
```

#### Output
```py 
    Gumno comio un(a) Big Burger y su brazo izquierdo ahora es un(a) hamburguesa
    Su cabeza es un(a) papa frita
    Su brazo izquierdo es un(a) hamburguesa
    Su brazo derecho es un(a) cafe
    Su pierna izquierda es un(a) nugget
    Su pierna derecha sigue igual
```
**Explicación:** 
Gumno tenía el brazo izquierdo en estado Normal. Al comer una Big Burger, su brazo izquierdo cambioa la forma de una hamburguesa. Las demás partes conservan su valor inicial: la pierna derecha se mantiene en Normal (por lo que indica que sigue igual) y el resto conserva sus alimentos respectivos.