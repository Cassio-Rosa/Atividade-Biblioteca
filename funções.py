#Importar a biblioteca sqlite3
import sqlite3

#Cria uma conexão com o banco de dados chamado "escola.db"

conexao = sqlite3.connect("biblioteca.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

#Criar uma tabela no banco de dados
cursor.execute("""

CREATE TABLE IF NOT EXISTS livros (
               
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT,
    ano INTEGER,
    disponivel TEXT               
    )
""")

def cadastrar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        for linha in cursor.fetchall:
            print(f"ID do livro que você vai cadastrar {linha[0]}")

        nome = input("Digite o titulo da obra: ")
        autor = input("Digite o autor da obra: ")
        ano = input("Digite o ano de lançamente da obra: ")

        cursor.connection("""
        INSERT INTO livros (nome, autor, ano)
        VALUES (?,?,?)
        """, (nome, autor, ano, "SIM"))

        if cursor.rowcount > 0:
            print("Livro cadastrado com sucesso")
        else:
            print("Deu ruim ai")

    except Exception as erro:
        print(f"Errp ap tentar excluir o aluno. Erro = {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()
       
    