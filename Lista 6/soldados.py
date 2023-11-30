class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass

class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado está marchando para a frente.")

    def atacar(self):
        print("Soldado está atacando com sua espada.")

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro está se posicionando para atirar.")

    def atacar(self):
        print("Arqueiro está disparando flechas.")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro está carregando velozmente pelo campo.")

    def atacar(self):
        print("Cavaleiro está investindo com sua lança.")

# Criar instâncias de cada unidade
soldado1 = Soldado()
arqueiro1 = Arqueiro()
cavaleiro1 = Cavaleiro()

# Adicionar as instâncias à lista unidades
unidades = [soldado1, arqueiro1, cavaleiro1]

# Percorrer a lista e chamar os métodos
for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print("-----")
