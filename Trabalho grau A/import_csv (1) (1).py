import csv
import random
import os
import tkinter as tk
from tkinter import messagebox

# Função para carregar dados de usuários, figurinhas e trocas

logged_in = False
nome_usuario = None
senha = None


def carregar_dados():
    usuarios = []
    figurinhas = []
    trocas = []

    if os.path.exists("usuarios.csv"):
        with open("usuarios.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                usuarios.append(row)

    if os.path.exists("figurinhas.csv"):
        with open("figurinhas.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                figurinhas.append(row)

    if os.path.exists("trocas.csv"):
        with open("trocas.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                trocas.append(row)

    return usuarios, figurinhas, trocas

# Função para salvar dados em arquivos


def salvar_dados(usuarios, figurinhas, trocas):
    with open("usuarios.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

    with open("figurinhas.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(figurinhas)

    with open("trocas.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trocas)

# Função para criar um novo álbum


def novo_album(usuarios,nome_usuario,senha):

    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            print("Usuário já existe. Tente novamente.")
            return

    # A terceira coluna pode ser usada para armazenar as figurinhas do álbum
    usuarios.append([nome_usuario, senha, ""])

    popup = tk.Toplevel(janela)
    popup.title("Pop-up")
    label = tk.Label(popup, text=f"Usuario {nome_usuario} criado com sucesso")
    label.pack()
    popup.geometry("200x100")
    ok_button = tk.Button(popup, text="OK", command=lambda: [popup.destroy(), janela.destroy()])
    ok_button.pack()

def chamar_novo_album():
    nome_usuario = entry1.get()
    senha = entry2.get()
    novo_album(usuarios,nome_usuario,senha)
# Função para acessar o álbum


def acessar_album(usuarios, figurinhas):
    global nome_usuario
    global senha 

    for usuario in usuarios:
        if usuario[0] == nome_usuario and usuario[1] == senha:
            # A terceira coluna armazena as figurinhas como uma string separada por ","
            album = usuario[2].split(",")
            print(f"Bem-vindo ao álbum de {nome_usuario}!")
            print("Figurinhas no álbum:", album)
            messagebox.showinfo("album", f"Bem-vindo ao álbum de {nome_usuario}!")
            messagebox.showinfo("album", f"Figurinhas no álbum:{album}")

            # Adicione aqui as opções adicionais que você deseja oferecer no álbum
            return

    print("Nome de usuário ou senha incorretos. Tente novamente.")


def chamar_acessar_album():
    acessar_album(usuarios, figurinhas)


def atribuir_figurinhas(usuarios, nome_usuario):
    figurinhas_disponiveis = input("Digite as figurinhas a serem atribuídas (separadas por vírgula): ").split(',')
    
    for usuario in usuarios:
        if usuario[0] == nome_usuario:
            usuario[2] += ",".join(figurinhas_disponiveis)
            print(f"Figurinhas atribuídas ao álbum de {nome_usuario}: {figurinhas_disponiveis}")
            return

    print("Usuário não encontrado.")

def chamar_atribuir_figurinhas():
    nome_usuario = input("Digite seu nome de usuário: ")
    atribuir_figurinhas(usuarios, nome_usuario)




def abrir_pacote_figurinhas(usuarios, nome_usuario, senha):
    try:
        with open('pokemonn.csv', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            # Gerar um índice aleatório para selecionar uma linha aleatória
            linhas_csv = list(leitor_csv)
            linha_aleatoria = random.choice(linhas_csv)
            
            # Verifique se o usuário e a senha são válidos
            for usuario in usuarios:
                if usuario[0] == nome_usuario and usuario[1] == senha:
                    # Verifique se a linha aleatória possui índice 3
                        usuario[2] += ",".join(linha_aleatoria)
                        print(f"Figurinhas do pacote adicionadas ao álbum de {nome_usuario}: {linha_aleatoria}")
                        messagebox.showinfo("abriu", f"Figurinhas do pacote adicionadas ao álbum de {nome_usuario}: {linha_aleatoria}")

            return

            print("Nome de usuário ou senha incorretos. Tente novamente.")
        
    except FileNotFoundError:
        return "Arquivo não encontrado"

def chamar_abrir_pacote_figurinhas():
     global nome_usuario,senha
     for usuario in usuarios:
        if usuario[0] == nome_usuario and usuario[1] == senha:
          abrir_pacote_figurinhas(usuarios,nome_usuario,senha)
        return

     print("Nome de usuário ou senha incorretos. Tente novamente.")

def pagina_login():
    global janela
    global nome_usuario
    global senha

    janela = tk.Tk()
    janela.title("Login")

    label_usuario = tk.Label(janela, text="Usuário:")
    label_usuario.pack(pady=5)

    entry1 = tk.Entry(janela)
    entry1.pack(pady=5)

    label_senha = tk.Label(janela, text="Senha:")
    label_senha.pack(pady=5)

    entry2 = tk.Entry(janela, show="*")
    entry2.pack(pady=5)

    def verificar_credenciais():
        global nome_usuario
        global senha
        nome_usuario = entry1.get()
        senha = entry2.get()

        # Verificar as credenciais do usuário (adicionar a sua lógica aqui)
        for usuario in usuarios:
            if usuario[0] == nome_usuario and usuario[1] == senha:
                janela.destroy()
                janelaNova = tk.Tk()
                janelaNova.title("Opcões")
                # Botão para acessar álbum
                botao_acessar_album = tk.Button(
                 janelaNova, text="Acessar Álbum", command=chamar_acessar_album)
                botao_acessar_album.pack(pady=10)

                botao_atribuir_figurinhas = tk.Button(
                 janelaNova, text="Atribuir Figurinhas", command=chamar_atribuir_figurinhas)
                botao_atribuir_figurinhas.pack(pady=10)
      
                 # Botão para abrir pacote
                botao_sair = tk.Button(
                 janelaNova, text="Abrir pacote de figurinhas", command=chamar_abrir_pacote_figurinhas)
                botao_sair.pack(pady=10)

                 # Botão para ver colecao
                botao_sair = tk.Button(
                 janelaNova, text="Ver coleção", command=chamar_gerenciar_coleção)
                botao_sair.pack(pady=10)
                espacamento_vertical = 20  # Espaçamento vertical entre os botões
                botao_acessar_album.pack(pady=espacamento_vertical, anchor="center")
                botao_acessar_album.pack(pady=espacamento_vertical, anchor="center")
                return

        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos. Tente novamente.")

    botao_login = tk.Button(janela, text="Login", command=verificar_credenciais)
    botao_login.pack(pady=10)

    largura_janela = 400
    altura_janela = 300
    janela.geometry(f"{largura_janela}x{altura_janela}")

    janela.mainloop()
 

def chamar_gerenciar_coleção():    
    chamar_abrir_pacote_figurinhas()


def pagina_registro():

     # Criar a janela principal
    global janela
    janela = tk.Tk()
    janela.title("Criar registro")
    
    # Label para "Usuário"
    label_usuario = tk.Label(janela, text="Usuário:")
    label_usuario.pack(pady=5)
    
    # Text Box 1
    global entry1
    entry1 = tk.Entry(janela)
    entry1.pack(pady=5)

    # Label para "Senha"
    label_senha = tk.Label(janela, text="Senha:")
    label_senha.pack(pady=5)

    # Text Box 2
    global entry2
    entry2 = tk.Entry(janela, show="*")  # Para esconder a senha com asteriscos
    entry2.pack(pady=5)

    # Definir a largura e a altura da janela
    largura_janela = 400  # Altere para a largura desejada
    altura_janela = 300   # Altere para a altura desejada
    janela.geometry(f"{largura_janela}x{altura_janela}")

    # Botão para criar novo álbum
    botao_novo_album = tk.Button(
        janela, text="Criar", command=chamar_novo_album)
    botao_novo_album.pack(pady=10)


# Função principal
def main():
    # Carregar dados existentes
    global usuarios, figurinhas, trocas
    usuarios, figurinhas, trocas = carregar_dados()

    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Aplicativo de Álbum")

    # Definir a largura e a altura da janela
    largura_janela = 400  # Altere para a largura desejada
    altura_janela = 300   # Altere para a altura desejada
    janela.geometry(f"{largura_janela}x{altura_janela}")

    # Botão para criar novo álbum
    botao_novo_album = tk.Button(
        janela, text="Novo Álbum", command=pagina_registro)
    botao_novo_album.pack(pady=10)

    botao_fazer_login = tk.Button(
        janela, text="Fazer Login", command=pagina_login)
    botao_fazer_login.pack(pady=10)



    # Botão para sair do aplicativo
    botao_sair = tk.Button(
        janela, text="Sair do Aplicativo", command=janela.quit)
    botao_sair.pack(pady=10)

    # Para centralizar os botões
    espacamento_vertical = 20  # Espaçamento vertical entre os botões
    botao_novo_album.pack(pady=espacamento_vertical, anchor="center")
    botao_sair.pack(pady=espacamento_vertical, anchor="center")

    # Executar o loop principal da interface gráfica
    janela.mainloop()


if __name__ == "__main__":
    main()
