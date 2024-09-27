def cifra_cesar(mensagem_cesar, chave_cesar, modo_cesar):
    result = ""
    for letra in mensagem_cesar:
        if letra.isalpha():
            deslocamento = 65 if letra.isupper() else 97
            if modo_cesar == 'C':
                result += chr((ord(letra) - deslocamento + chave_cesar) % 26 + deslocamento)
            elif modo_cesar == 'D':
                result += chr((ord(letra) - deslocamento - chave_cesar) % 26 + deslocamento)
        else:
            result += letra
    return result


def gerar_chave(mensagem_vegenere, chave_vegenere):
    chave_vegenere = list(chave_vegenere)
    if len(chave_vegenere) == len(mensagem_vegenere):
        return chave_vegenere
    else:
        for i in range(len(mensagem_vegenere) - len(chave_vegenere)):
            chave_vegenere.append(chave_vegenere[i % len(chave_vegenere)])
    return "".join(chave_vegenere)

def cifra_vigenere(mensagem_vegenere, chave_vegenere, modo_vegenere):
    resultado = ""
    chave_vegenere = gerar_chave(mensagem_vegenere, chave_vegenere)
    for i in range(len(mensagem_vegenere)):
        letra = mensagem_vegenere[i]
        if letra.isalpha():
            deslocamento = 65 if letra.isupper() else 97
            if modo_vegenere == 'C':
                resultado += chr((ord(letra) + ord(chave_vegenere[i].lower()) - 2 * deslocamento) % 26 + deslocamento)
            elif modo_vegenere == 'D':
                resultado += chr((ord(letra) - ord(chave_vegenere[i].lower()) + 26) % 26 + deslocamento)
        else:
            resultado += letra
    return resultado

def ler_arquivo():
    nome_arquivo = input("Digite o nome do arquivo de texto (com extensão .txt): ")

    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:")
            print(conteudo)
            return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Verifique o nome e tente novamente.")

def menu():
    while True:
        print("\n=== MENU DE CRIPTOGRAFIA ===")
        print("1. Cifra de César")
        print("2. Cifra de Vigenère")
        print("3. Arquivo de Texto")
        print("\n0. Sair")
        print("=============================\n")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            mensagem_cesar = input("Digite a mensagem: ")
            chave_cesar = int(input("Digite a chave (número): "))
            modo_cesar = input("Escolha 'criptografar' ou 'descriptografar' [C / D]: ").upper()
            print("Resultado:", cifra_cesar(mensagem_cesar, chave_cesar, modo_cesar))

        elif escolha == "2":
            mensagem_vegenere = input("Digite a mensagem: ")
            chave_vegenere = input("Digite a chave: ")
            modo_vegenere = input("Escolha 'criptografar' ou 'descriptografar' [C / D]: ").upper()
            print("Resultado:", cifra_vigenere(mensagem_vegenere, chave_vegenere, modo_vegenere))

        elif escolha == "3":
            escolha_cifra = input("Escolha qual cifra: \n1- [C|C] ou 2- [C|V]: ")
            if escolha_cifra == "1":
                mensagem_cesar = ler_arquivo()
                chave_cesar = int(input("Digite a chave (número): "))
                modo_cesar = input("Escolha 'criptografar' ou 'descriptografar' [C / D]: ").upper()
                print("Resultado:", cifra_cesar(mensagem_cesar, chave_cesar, modo_cesar))

            elif escolha_cifra == "2":
                mensagem_vegenere = ler_arquivo()
                chave_vegenere = input("Digite a chave: ")
                modo_vegenere = input("Escolha 'criptografar' ou 'descriptografar' [C / D]: ").upper()
                print("Resultado:", cifra_vigenere(mensagem_vegenere, chave_vegenere, modo_vegenere))

            else:
                print("Opção Inválida, tente novamente!")
                break

        elif escolha == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
menu()
