import random
class TresenRaya:
    def __init__(self, jugador1, jugador2):
        self.tablero=[]
        for fila in range(3):
            fila=[" "," "," "]
            self.tablero.append(fila)
        num=random.randint(1,2)
        if num==1:
            self.jugadoractual=jugador1
            self.simboloactual="X"
        else:
            self.jugadoractual=jugador2
            self.simboloactual="O"
    def mostrar_tablero(self, con_numeros=True):
        print ("1   2   3")
        for fila in self.tablero:
            n=""
            for l in fila:
                n=n+"| "+" "
            n=n+"|"
            print("----------")
            print (n)
    def colocar_ficha(self, pos):
        for fila in self.tablero:
            if fila[pos]!=" ":
                print("Posicion ocupada")
                return
print("=== TRES EN RAYA ===")
salir=False
while salir==False:
    print(f"\n1. Jugar \n2. Ver historial \n3. Salir")
    opcion=int(input("Ingrese una opción: "))
    if opcion==1:
        jugador1=input("Jugador 1: Ingrese su nombre: ")
        jugador2=input("Jugador 2: Ingrese su nombre: ")
        juego=TresenRaya(jugador1, jugador2)
        juego.mostrar_tablero()
        print("Comienza:", juego.jugadoractual)
        pos=int(input("Ingrese la posicion: "))
        juego.colocar_ficha(pos)
    if opcion==2:
        puntuacion={}
        
    if opcion==3:
        salir=True
print("Hasta luego")
