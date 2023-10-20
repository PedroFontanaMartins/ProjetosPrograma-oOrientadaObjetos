# Definição da classe Mago 
class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola, nome_magia, atributo_magia):
        # Atributos de instância
        self.__nome = nome 
        self.idade = idade   
        self.escola = escola 
        self.nome_magia = nome_magia
        self.atributo_magia = atributo_magia
        print('Mago ', self.__nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola todos! Meu nome é ',self.__nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def cumprimentar(self,nome):
        print('Ola, ', nome)

    def lançarMagia(self):
        print(self.__nome, 'Lançou a',self.nome_magia)

    def atributomagia(self):
        print('O atributo da',self.nome_magia, 'é',self.atributo_magia)


    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 

    #Método de set 
    def setNome(self,novoNome):
        self.__nome = novoNome
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts', 'Accio', 'Manipulação')
gd = Mago('Gandalf', 2000, 'Magia Cinza', 'You shall not pass', 'Manipulação')
mf = Mago('Mago de fogo', 30, 'Escola de Fogo', 'Bola de fogo', 'Fogo')
mg = Mago('Mago de gelo', 30, 'Escola de gelo', 'Bola de gelo','Gelo')
ma = Mago('Mago de Água', 30, 'Escola de Água', 'Bola de água','Água')

#Acessando atributos públicos
# print(hp.__nome)
#hp.__nome = "Merlin"
hp.setNome("Merlin")

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()
hp.cumprimentar("Rossana")

gd.falar()
gd.cumprimentar("Gabriel")

mg.lançarMagia()
mf.lançarMagia()
ma.lançarMagia()

mg.atributomagia()
mf.atributomagia()
ma.atributomagia()
