import json
import random
import os

# ASCII art de "SALVATION"
ascii_art = """
.d8888b.           888                   888    d8b                   
d88P  Y88b          888                   888    Y8P                   
Y88b.               888                   888                          
 "Y888b.    8888b.  888 888  888  8888b.  888888 888  .d88b.  88888b.  
    "Y88b.     "88b 888 888  888     "88b 888    888 d88""88b 888 "88b 
      "888 .d888888 888 Y88  88P .d888888 888    888 888  888 888  888 
Y88b  d88P 888  888 888  Y8bd8P  888  888 Y88b.  888 Y88..88P 888  888 
 "Y8888P"  "Y888888 888   Y88P   "Y888888  "Y888 888  "Y88P"  888  888 
"""

ascii_art2 = """
                .---.
           '-.  |   |  .-'         
             ___|   |___          
        -=  [           ]  =-    
            `---.   .---'         
         __||__ |   | __||__      
         '-..-' |   | '-..-'   
           ||   |   |   ||     
           ||_.-|   |-,_||     
         .-"`   `"`'`   `"-.   
       .'                   '.

"""
# aqui começa a salvação!! =D
def carregar_biblia():
    with open("biblia.json", "r", encoding="utf-8-sig") as file:
        return json.load(file)

def escolher_palavra(biblia):
    livro = random.choice(biblia)
    nome_livro = livro["abbrev"]
    capitulo_idx = random.randint(0, len(livro["chapters"]) - 1)
    capitulo = livro["chapters"][capitulo_idx]

    if len(capitulo) >= 3:
        versiculo_idx = random.randint(0, len(capitulo) - 3)
    else:
        versiculo_idx = 0 # se pegar um com mneos de 3



    trecho = capitulo[versiculo_idx:versiculo_idx + 3]
    print(f"\nTrecho da Bíblia:")
    print(f"Livro: {nome_livro}, Capítulo: {capitulo_idx + 1}, Versículos {versiculo_idx + 1} - {versiculo_idx + 3}")
    for i, texto in enumerate(trecho, start=1):
       print(f"{versiculo_idx + i}: {texto}")


#escolher_palavra() // função abandonada do arquivo .py


# para rezar o terço

def terco():
    roteiro = [
        "1. Faça o sinal da cruz.",
        "2. Reze o Credo.",
        "3. Reze o Pai Nosso.",
        "4. Reze 3 Ave-Marias.",
        "5. Reze o Glória ao Pai.",
        "6. Medite nos mistérios e reze as dezenas."
    ]
    print("\nRoteiro para Rezar o Terço:")
    for passo in roteiro:
        print(passo)


def livro():

# CLI, essa parte deu trabalho!

def main():
    if not os.path.exists("biblia.json"):
        print("erro 666.")
        return

    biblia = carregar_biblia()

    while True:
        print(ascii_art)
        print(ascii_art2)
        print("\nEscolha uma opção:")
        print("1 - Trecho da Biblia")
        print("2 - Roteiro para rezar o terço")
        print("3 - Ler um livro do inicio") # Ainda não adicionei
        print("4 - Sair")
        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            escolher_palavra(biblia)
        elif escolha == "2":
            terco()
        elif escolha == "3":
            #Coloque aqui
            break
        elif escolha == "4":
            print("Encerrando o programa. Que o Senhor te acompanhe")
            break
        else:
            print("Opção inválida. tente novamente.")
        
        continuar = input("\nDeseja continuar? (y/n): ").strip().lower()
        if continuar == 'y':
            continue
        elif continuar == 'n':
            print("Encerrando o programa. Que o Senhor te acompanhe.")
            break
        else:
            print("Entrada Invalida")



if __name__ == "__main__":
    main()
