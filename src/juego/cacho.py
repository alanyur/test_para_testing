from src.juego import dado
class cacho:
    extra=0
    def __init__(self):
        self.dados = [dado.dado() for _ in range(5)]

    def agitar(self):
        for d in self.dados:
            d.lanzar()

    def perder_dado(self):
        print("perdiste un dado")
        if self.dados:
            self.dados.pop()
        else:
            print("No tienes más dados para perder.")

    def dados_extra(self):
        print("ganaste un dado")
        if len(self.dados)<5:
            self.dados.append(dado())
        else:
            self.extra+=1


    def estado1(): ###aca hay que cambiarlo
        print("partida cerrada")
    def estado2():
        print("partida abierta")

