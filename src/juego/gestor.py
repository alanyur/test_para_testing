import random
import cacho
class gestor:
    def __init__(self):
        self.jugadores = []
        cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        while cantidad_jugadores <2 or cantidad_jugadores>5:
            cantidad_jugadores=int(input("ingrese la cantidad de jugadores (2-5): "))
        self.jugadores = [cacho.cacho() for i in range(cantidad_jugadores)]
        self.iniciar_juego()

    def iniciar_juego(self):
        # Elegir al azar quién comienza
        self.turno_actual = random.randint(0, len(self.jugadores) - 1)
        print(f"Inicia jugador {self.turno_actual + 1}")

    def turno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        print(f"Turno del jugador {self.turno_actual + 1}")
#### Me falta la funcionalidad para cuando queda solo un dado


if __name__ == "__main__":
    mi_gestor = gestor()