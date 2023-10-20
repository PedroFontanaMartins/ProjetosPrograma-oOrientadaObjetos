import random


class Dado:
    def __init__(self, faces):
        self.faces = faces


    def rolar(self):
        return random.randint(1, self.faces)
    

def jogar_dado(dado, jogadas):
    for i in range(jogadas):
        resultado = dado.rolar()
        print(f'Jogada {i + 1}: {resultado}')


def main():
    dado6 = Dado(6)
    dado8 = Dado(8)
    dado12 = Dado(12)

    print('Dado de 6 faces:')
    jogar_dado(dado6,3)
    
    print('Dado de 8 faces:')
    jogar_dado(dado8,3)

    print('Dado de 12 faces:')
    jogar_dado(dado12,3)


if __name__ == "__main__":
    main()
