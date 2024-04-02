import sys
from scapy.all import *

id_identificador = 9
num_seq = 1

ping = b'\x08\x00\xf7\xff'
def enviar_char_icmp(char):
    try:
        global id_identificador
        global num_seq
        # Rellenar con valores hexadecimales
        padding = bytes([i for i in range(0x10,0x38)])[:(42-len(char))]
        three_bytes = bytes([0xfa,0x20,0x13]) 
        bytes_extra = bytes([0xfa,0x20,0x13,0x15]) * 2
        payload = char.encode() + ping + bytes_extra + three_bytes + padding 
        # Crear paquete ICMP request
        paquete_icmp = IP(dst="8.8.8.8") / ICMP(type=8,code=0,id=id_identificador,seq=num_seq) / Raw(load=payload)
        id_identificador += 1
        num_seq += 1
        send(paquete_icmp)
        
    except Exception as e:
        print(f"Error al enviar el caracter '{char}': {str(e)}")
        
def main():
    if len(sys.argv) != 2:
        print("Uso: python3 pingv4.py <texto>")
        sys.exit(1)
    texto = sys.argv[1]
    for char in texto:
       enviar_char_icmp(char)

if __name__ == "__main__":
    main()
    
    