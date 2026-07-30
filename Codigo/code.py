nombre = input()
lista_partes = input().split(",")
lista_cambio = input().split(",")

print(f"{nombre} comio un(a) {lista_cambio[0]} y su {lista_cambio[1]} ahora es un(a) {lista_cambio[2]}")
lista_b = ["cabeza", "brazo izquierdo", "brazo derecho", "pierna izquierda", "pierna derecha"]

for i in range(5):
    if lista_cambio[1] == lista_b[i]:
        lista_partes[i] = lista_cambio[2]

for i in range(5):
    if lista_partes[i] == "Normal":
        print(f"Su {lista_b[i]} sigue igual")
    else:
        print(f"Su {lista_b[i]} es un(a) {lista_partes[i]}")