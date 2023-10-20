class CadastroCliente():
    def __init__(self, nome, sobrenome, data_nascimento, email, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.tentativas_senha = 0
        self.bloqueado = False

    def fazer_cadastro(self):
        print('Cadastro realizado.')

    def fazer_login(self, email, senha):
        if self.bloqueado:
            print('Cadastro bloqueado. Entre em contato com o suporte')
            return False
        
        if email == self.email and senha == self.senha:
            print('Login realizado com sucesso.')
            return True
        
        else:
            self.tentativas_senha += 1
            if self.tentativas_senha >= 3:
                print('Senha incorreta. Cadastro bloqueado, entre em contato com o suporte')
                self.bloqueado = True
            else:
                print('Senha incorreta. Tentativas restantes:', 3 - self.tentativas_senha)
                return False
                

    def consultar_cadastro(self):
        if not self.bloqueado:
            print('Nome:', self.nome)
            print('Sobrenome:', self.sobrenome)
            print('Data de Nascimento:', self.data_nascimento)
            print('Email:', self.email)
            print('CPF:', self.cpf)
        else: 
            print("Cadastro bloqueado. Entre em contato com o suporte.")



cliente = CadastroCliente('William', 'Tuxen', '22/12/2002', 'william.tuxen@gmail.com', '123.456.789-00', '1234')

cliente.fazer_cadastro()

email_input = input("Digite seu email: ")
senha_input = input("Digite sua senha: ")
cliente.fazer_login(email_input, senha_input)

cliente.consultar_cadastro()
