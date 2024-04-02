import sys
from scapy.all import rdpcap, ICMP
from termcolor import colored
from nltk.corpus import words

english_words = set(words.words())

def count_english_words(text):
    words_found = 0
    for word in text.split():
        if word.lower() in english_words:
            words_found += 1
    return words_found

def decrypt_cesar(text, shift):
    decrypted_texts = []
    for s in range(26):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr(((ord(char) - ord('a') - s) % 26) + ord('a'))
                elif char.isupper():
                    decrypted_char = chr(((ord(char) - ord('A') - s) % 26) + ord('A'))
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 cesar_decrypt.py <captura.pcapng>")
        sys.exit(1)

    pcapng_file = sys.argv[1]
    
    packets = rdpcap(pcapng_file)
    encrypted_text = ""
    
    for packet in packets:
        if packet.haslayer(ICMP) and packet[ICMP].type == 8:
            encrypted_text += chr(packet[ICMP].load[0])
            
    best_shift = None
    best_word_count = 0
    
    decrypted_texts = decrypt_cesar(encrypted_text, 0) 
    for shift, decrypted_text in enumerate(decrypted_texts):
        english_word_count = count_english_words(decrypted_text)
        if english_word_count > best_word_count:
            best_shift = shift
            best_word_count = english_word_count
            
    for shift, decrypted_text in enumerate(decrypted_texts):
        if shift == best_shift:
            print(colored(f"{shift}: {decrypted_text}", 'green'))
        else:
            print(f"{shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
    