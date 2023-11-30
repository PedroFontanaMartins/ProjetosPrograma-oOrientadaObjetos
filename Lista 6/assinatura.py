class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

# Criar instâncias de cada assinatura
assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

# Adicionar as instâncias ao array assinaturas
assinaturas = [assinatura_simples, assinatura_premium]

# Percorrer o array e exibir informações
for assinatura in assinaturas:
    print(f"Tipo de Assinatura: {assinatura.__class__.__name__}")
    print(f"Preço: R$ {assinatura.calcular_preco():.2f}")
    assinatura.exibir_detalhes()
    print("-----")
