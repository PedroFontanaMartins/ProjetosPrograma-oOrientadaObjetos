class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Acelerando o veículo!")

    def frear(self):
        print("Freando o veículo!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def ligar_radio(self):
        print("Ligando o rádio do carro!")

    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinando a moto!")

    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def carregar(self):
        print("Carregando o caminhão!")

    def descarregar(self):
        print("Descarregando o caminhão!")

# Exemplos de uso:
carro = Carro("Miata", "RX-7", 2002, "Azul")
moto = Moto("Honda", "CBR", 2021, "600cc")
caminhao = Caminhao("Volvo", "VNL", 2020, "10 toneladas")

# Chamando métodos específicos de cada classe
carro.abrir_porta()
moto.empinar()
caminhao.carregar()

# Chamando métodos da classe base
carro.acelerar()
moto.frear()
