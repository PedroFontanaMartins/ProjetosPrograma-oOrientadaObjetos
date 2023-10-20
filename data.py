class Data():
    def __init__(self, dia, mês, ano):
        self.dia = dia
        self.mês = mês
        self.ano = ano


    def imprimirData(self):
        print(f"{self.dia}/{self.mês}/{self.ano}")
                 

    def imprimirDataPorExtenso(self, cidade):
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes_por_extenso = meses[self.mês -1]
        print(f'{self.dia} de {mes_por_extenso} de {self.ano} em {cidade}')

minha_data = Data(10, 10, 2023)
minha_data.imprimirData()
minha_data.imprimirDataPorExtenso("Porto Alegre")
