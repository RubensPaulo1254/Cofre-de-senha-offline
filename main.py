import sqlite3
import time
import getpass
import sys
from os import system
conn = sqlite3.connect("date2.db")
cursor = conn.cursor()
def cadastroPrimeiroAcesso(login2,passd):
    cursor.execute("""
    INSERT INTO dados2 (login, senha)
    VALUES(?,?)
""", (login2,passd))        
    conn.commit()
    conn.close()
    
def start():
    while(True):
        print("[1] Cadastrar")
        print("[2] Login")
        op = input()
        system('cls')
        if(op == "1"):
            print("Digite um login:")
            op1 = input()
            print("Digite uma senha:")
            op2 = input()
            system('cls')
            cadastroPrimeiroAcesso(op1,op2)
        if(op == "2"):
            print("login:")
            op1 = input()
            print("senha:")
            op2 = input()
            system('cls')
            login(op1, op2)
        
def login(op1, op2):
    
    cursor.execute(""" SELECT * FROM dados2;
""")
    for linha in cursor.fetchall():
        if(linha[0] == op1 and linha[1] == op2):
            main()
        else:
            print("ERROR")

def cadastro():
    conn = sqlite3.connect("date.db")
    cursor = conn.cursor()

    print("Digite o login usado. EMAIL OU ID:")
    id1 = input()
    print("Digite a senha:")
    passd = input()

    cursor.execute("""
    INSERT INTO dados(login, senha)
    VALUES(?,?)
""", (id1, passd))
    conn.commit()
    conn.close()
    system('cls')
    print("Cadastro realizado com sucesso")
    time.sleep(3)
    system('cls')

            
def main():
    while(True):
        print("[1] Cadastrar nova senha")
        print("[2] Acessar senha")
        print("[3] Excluir senha")
        print("[4] Atualizar senha")
        op = input()
        if(op == "1"):
            cadastro()
            system('cls')
        elif(op=="2"):
            system('cls')
            conn = sqlite3.connect('date.db')
            cursor = conn.cursor()
            cursor.execute("""
            SELECT * FROM dados;
            """)
            for linha in cursor.fetchall():
                print(linha)
            conn.close
            input("Digite para continuar")
            system('cls')


start()



