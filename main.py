#Henrique Soares Serra-RM573618

import os
import csv
import json

def cadastrar_alunos():
    novos = []
    print("\n--- CADASTRO DE ALUNOS ---")
    print("Digite RM vazio para encerrar.")
    while True:
        rm = input("RM: ").strip()
        if rm == "":
            break
        nome = input("Nome: ").strip()
        cp1 = float(input("CP1: "))
        cp2 = float(input("CP2: "))
        cp3 = float(input("CP3: "))

        menor = cp1
        if cp2 < menor:
            menor = cp2
        if cp3 < menor:
            menor = cp3
        media = (cp1 + cp2 + cp3 - menor) / 2

        aluno = {"rm": rm, "nome": nome, "cp1": cp1, "cp2": cp2, "cp3": cp3, "media": media}
        novos.append(aluno)
    if novos:
        gravar_txt(novos)
        gravar_csv(novos)
        gravar_json(novos)
        gravar_excel(novos)
        print(f"\n{len(novos)} aluno(s) gravado(s) nos 4 arquivos.")
    else:
        print("\nNenhum aluno cadastrado, voltando ao menu.")

def gravar_txt(novos):
    with open("alunos.txt", "a", encoding="utf-8") as arq:
        for aluno in novos:
            arq.write(f"{aluno['rm']};{aluno['nome']};{aluno['cp1']};{aluno['cp2']};{aluno['cp3']};{aluno['media']}\n")

def gravar_csv(novos):
    existe = os.path.exists("alunos.csv")
    with open("alunos.csv", "a", newline="", encoding="utf-8") as arq:
        w = csv.writer(arq, delimiter=";")
        if not existe:
            w.writerow(["RM", "Nome", "CP1", "CP2", "CP3", "Media"])
        for aluno in novos:
            w.writerow([aluno["rm"], aluno["nome"], aluno["cp1"], aluno["cp2"], aluno["cp3"], aluno["media"]])

def gravar_json(novos):
    if os.path.exists("alunos.json"):
        with open("alunos.json", encoding="utf-8") as arq:
            antigos = json.load(arq)
    else:
        antigos = []
    todos = antigos + novos
    with open("alunos.json", "w", encoding="utf-8") as arq:
        json.dump(todos, arq, ensure_ascii=False, indent=4)

def gravar_excel(novos):
    existe = os.path.exists("alunos.xlsx")
    with open("alunos.xlsx", "a", newline="", encoding="utf-8") as arq:
        w = csv.writer(arq, delimiter=";")
        if not existe:
            w.writerow(["RM", "Nome", "CP1", "CP2", "CP3", "Media"])
        for aluno in novos:
            w.writerow([aluno["rm"], aluno["nome"], aluno["cp1"], aluno["cp2"], aluno["cp3"], aluno["media"]])

def ler_txt():
    try:
        with open("alunos.txt", encoding="utf-8") as arq:
            linhas = arq.readlines()
    except FileNotFoundError:
        print("\nalunos.txt ainda não existe. Cadastre alunos antes.")
        return
    print("\n--- alunos.txt ---")
    for linha in linhas:
        dados = linha.strip().split(";")
        if len(dados) == 6:
            rm, nome, cp1, cp2, cp3, media = dados
            print(f"RM: {rm} | Nome: {nome} | CP1: {cp1} | CP2: {cp2} | CP3: {cp3} | Media: {media}")

def ler_csv():
    try:
        with open("alunos.csv", encoding="utf-8") as arq:
            linhas = list(csv.reader(arq, delimiter=";"))
    except FileNotFoundError:
        print("\nalunos.csv ainda não existe. Cadastre alunos antes.")
        return
    print("\n--- alunos.csv ---")
    for linha in linhas:
        if len(linha) == 6:
            rm, nome, cp1, cp2, cp3, media = linha
            print(f"RM: {rm} | Nome: {nome} | CP1: {cp1} | CP2: {cp2} | CP3: {cp3} | Media: {media}")

def ler_json():
    try:
        with open("alunos.json", encoding="utf-8") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        print("\nalunos.json ainda não existe. Cadastre alunos antes.")
        return
    print("\n--- alunos.json ---")
    for aluno in alunos:
        print(f"RM: {aluno['rm']} | Nome: {aluno['nome']} | CP1: {aluno['cp1']} | CP2: {aluno['cp2']} | CP3: {aluno['cp3']} | Media: {aluno['media']}")

def ler_excel():
    try:
        with open("alunos.xlsx", encoding="utf-8") as arq:
            linhas = list(csv.reader(arq, delimiter=";"))
    except FileNotFoundError:
        print("\nalunos.xlsx ainda não existe. Cadastre alunos antes.")
        return
    print("\n--- alunos.xlsx ---")
    for linha in linhas:
        if len(linha) == 6:
            rm, nome, cp1, cp2, cp3, media = linha
            print(f"RM: {rm} | Nome: {nome} | CP1: {cp1} | CP2: {cp2} | CP3: {cp3} | Media: {media}")

def ler_arquivo():
    while True:
        print("\n--- LER ARQUIVO ---")
        print("1 - Texto")
        print("2 - CSV")
        print("3 - JSON")
        print("4 - Excel")
        print("0 - Voltar")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            ler_txt()
            break
        elif opcao == "2":
            ler_csv()
            break
        elif opcao == "3":
            ler_json()
            break
        elif opcao == "4":
            ler_excel()
            break
        elif opcao == "0":
            break
        else:
            print("Opção inválida, digite novamente.")

def pesquisar_aluno():
    if not os.path.exists("alunos.json"):
        print("\nalunos.json ainda não existe. Cadastre alunos antes.")
        return
    with open("alunos.json", encoding="utf-8") as arq:
        alunos = json.load(arq)
    rm = input("\nDigite o RM do aluno: ").strip()
    encontrado = False
    for aluno in alunos:
        if aluno["rm"] == rm:
            print("\nAluno encontrado:")
            print(f"RM: {aluno['rm']}")
            print(f"Nome: {aluno['nome']}")
            print(f"CP1: {aluno['cp1']}")
            print(f"CP2: {aluno['cp2']}")
            print(f"CP3: {aluno['cp3']}")
            print(f"Media: {aluno['media']}")
            encontrado = True
            break
    if not encontrado:
        print(f"\nNenhum aluno encontrado com o RM {rm}.")

while True:
    print("\n--------------------------")
    print("MENU PRINCIPAL")
    print("0 - SAIR")
    print("1 - Gravar alunos")
    print("2 - Ler arquivo")
    print("3 - Pesquisa")
    print("--------------------------")
    opcao = input("Escolha: ").strip()
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar_alunos()
    elif opcao == "2":
        ler_arquivo()
    elif opcao == "3":
        pesquisar_aluno()
    else:
        print("Opção inválida, digite novamente.")