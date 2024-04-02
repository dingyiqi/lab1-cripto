import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ''
    for char in texto:
        if char.isalpha():
            codigo = ord(char)
            if char.isupper():
                codigo_cifrado = (codigo - 65 + corrimiento) % 26 + 65
            else:
                codigo_cifrado = (codigo - 97 + corrimiento) % 26 + 97
            caracter_cifrado = chr(codigo_cifrado)
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += char
    return texto_cifrado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py <texto> <corrimiento>")
        sys.exit(1)
        
    texto_para_cifrar = sys.argv[1]
    corrimiento = int(sys.argv[2])
    
    texto_cifrado = cifrar_cesar(texto_para_cifrar, corrimiento)
    print(texto_cifrado)
