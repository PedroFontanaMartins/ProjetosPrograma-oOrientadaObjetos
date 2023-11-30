class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto, deslocamento=None):
        deslocamento = deslocamento if deslocamento is not None else self.deslocamento
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                char_cifrado = chr((ord(char) - ord('a' if char.islower() else 'A') + deslocamento) % 26 + ord('a' if char.islower() else 'A'))
                texto_cifrado += char_cifrado
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        # Adicionar um argumento padrão em cifrar
        return self.cifrar(texto_cifrado, deslocamento=-self.deslocamento)

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            char_cifrado = chr(ord(char) ^ self.chave)
            texto_cifrado += char_cifrado
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        # Decifrar é a mesma operação que cifrar com a mesma chave
        return self.cifrar(texto_cifrado)

# Exemplo de uso:
cesar = CifraCesar(3)
xor = CifraXor(42)

texto_original = "Hello, World!"

texto_cifrado_cesar = cesar.cifrar(texto_original)
texto_decifrado_cesar = cesar.decifrar(texto_cifrado_cesar)

texto_cifrado_xor = xor.cifrar(texto_original)
texto_decifrado_xor = xor.decifrar(texto_cifrado_xor)

print("Texto Original:", texto_original)
print("Texto Cifrado (Cifra de César):", texto_cifrado_cesar)
print("Texto Decifrado (Cifra de César):", texto_decifrado_cesar)
print("\nTexto Cifrado (Cifra XOR):", texto_cifrado_xor)
print("Texto Decifrado (Cifra XOR):", texto_decifrado_xor)
