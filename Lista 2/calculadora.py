
class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if num2 == 0:
            print("Aviso: Divisão por zero não é possível.")
            return -1
        return num1 / num2
    
calculadora = Calculadora()

resultado_soma = calculadora.somar(2, 2)
print(f"Soma: {resultado_soma}")

resultado_subtracao = calculadora.subtrair(2, 2)
print(f"Subtração: {resultado_subtracao}")

resultado_multiplicacao = calculadora.multiplicar(2, 2)
print(f"Multiplicação: {resultado_multiplicacao}")

resultado_divisao = calculadora.dividir(2, 2)
print(f"Divisão: {resultado_divisao}")

# Tentando uma divisão por zero
resultado_divisao_por_zero = calculadora.dividir(2, 0)
print(f"Divisão por zero: {resultado_divisao_por_zero}")
