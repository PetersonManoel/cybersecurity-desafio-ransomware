import os
import pyaes

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Verifica se o arquivo criptografado existe antes de proceder
if os.path.exists(file_name):
    # Abrir o arquivo criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    # Chave para descriptografia (deve ser idêntica à usada no encrypter.py)
    key = b"chave-segura123"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Salvar o arquivo descriptografado
    new_file = "teste.txt"
    with open(new_file, "wb") as file:
        file.write(decrypt_data)
    
    print(f"Arquivo {file_name} descriptografado com sucesso como {new_file}.")
else:
    print(f"Arquivo {file_name} não encontrado.")
