import gestor
import contador
class arbitro:
    def __init__(self):
        self.gestor_juego =  gestor.gestor()
        self.partida()


    def partida(self):
        pintas={
                "as":int(0),
                "tonto":int(1),
                "tren":int(2),
                "cuadra":int(3),
                "quinta":int(4),
                "sexta":int(5)
            }
        print("ingrese una cantidad y una pinta")
        cantidad1=int(input("ponga cantidad"))
        pinta1=input("ponga pinta")
        self.gestor_juego.turno()
        while True:
            resp=input("ingrese su jugada (subir, calza, duda): ")
            ###aqui va el validador de apuestasr
            if(resp=="subir"):
                cantidad1=int(input("ponga cantidad")) ###tengo que hacer una manera para que se haga un ciclo hasta que se calce o dude
                pinta1=input("ponga pinta")
                print("que bueno que subiste")
            if(resp=="calza"):
                cantidad_dados=self.mi_contador=contador.contador().cuenta(self.gestor_juego.jugadores)
                indice=pintas[pinta1]
                if cantidad_dados[indice] == cantidad1:
                    self.gestor_juego.jugadores[self.gestor_juego.turno_actual].dados_extra()
                else:
                    self.gestor_juego.jugadores[self.gestor_juego.turno_actual].perder_dado()
            elif(resp=="duda"):
                cantidad_dados=self.mi_contador=contador.contador().cuenta(self.gestor_juego.jugadores)
                indice=pintas[pinta1]
                if cantidad_dados[indice] >= cantidad1:
                    self.gestor_juego.jugadores[self.gestor_juego.turno_actual-1].perder_dado()
                    print("jugador anterior")
                else:
                    self.gestor_juego.jugadores[self.gestor_juego.turno_actual].perder_dado()
            self.gestor_juego.turno()


if __name__ == "__main__":
    mi_arbitro = arbitro()