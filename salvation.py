import json
import random
import os


# aqui começa a salvação!! =D


with open("biblia.json", "r", encoding="utf-8-sig") as file:
    biblia = json.load(file)

def escolher_palavra():
    livro = random.choice(biblia)
    nome_livro = livro["abbrev"]
    capitulo_idx = random.randint(0, len(livro["chapters"]) - 1)
    capitulo = livro["chapters"][capitulo_idx]

    if len(capitulo) >= 3:
        versiculo_idx = random.randint(0, len(capitulo) - 3)
    else:
        versiuclo_idx = 0 # se pegar um com mneos de 3



    trecho = capitulo[versiculo_idx:versiculo_idx + 3]
    print(f"\nTrecho da Bíblia:")
    print(f"Livro: {nome_livro}, Capítulo: {capitulo_idx + 1}, Versículos {versiculo_idx + 1} - {versiculo_idx + 3}")
    for i, texto in enumerate(trecho, start=1):
       print(f"{versiculo_idx + i}: {texto}")



#escolher_palavra() // função abandonada do arquivo .py
