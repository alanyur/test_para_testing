import random
class dado:
    total=[]
    def lanzar(self):
        resultado = random.randint(1, 6)
        valor ={
            1: "as",
            2: "tonto",
            3: "tren",
            4: "cuadra",
            5: "quina",
            6: "sexto"
        }
        print (resultado, valor[resultado])
        dado.total.append(valor[resultado])


if __name__ == "__main__":
    mi_dado = dado()
    mi_dado.lanzar()
    print (mi_dado.total)