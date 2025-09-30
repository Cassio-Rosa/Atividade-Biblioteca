import streamlit as st
import pandas as pd
import sqlite3 

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

        nome = st.text_input("Digite o titulo da obra: ")
        if nome:
            autor = st.text_input("Digite o autor da obra: ")
            if autor:
                ano = st.text_input("Digite o ano de lançamente da obra: ")
                if ano:

                    cursor.execute("""
                    INSERT INTO livros (titulo, autor, ano, disponivel)
                    VALUES (?,?,?,?)
                    """, (nome, autor, ano, "SIM"))
                    conexao.commit()

                    if nome and autor and ano:
                        st.success("Livro cadastrado com sucesso")
                    else:
                        st.error("Deu ruim ai")

    except Exception as erro:
        st.write(f"Se ferrou ai pai. Erro = {erro}")
    finally:
    #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
                conexao.close()

def mostrar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        tabela_livros = {
            "id": [linha[0] for linha in livros],
            "titulo": [linha[1] for linha in livros],
            "autor": [linha[2] for linha in livros],
            "ano": [linha[3] for linha in livros],
            "disponivel": [":green[Sim]" if linha[4] == "SIM" else ":red[NÃO]" for linha in livros],
        }
        st.table(tabela_livros, border="horizontal")
    except Exception as erro:
        print(f"Se ferrou ai pai. Erro = {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

def atualizar_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        id_mudar = int(input("Digite o id do livro que você quer alterar a disponibilidade: "))
        cursor.execute("""
SELECT disponivel FROM livros WHERE id = ?

""", (id_mudar,))
        retorno = cursor.fetchone()
        if retorno[0] is None:
            print("ID não encontrado")
            return
        if retorno[0] == "SIM":
            cursor.execute("""
        UPDATE livros
        SET disponivel = ?
        WHERE id = ?
        """, ("NÃO",id_mudar))
        conexao.commit()
        if retorno[0] == "NÃO":
            cursor.execute("""
        UPDATE livros
        SET disponivel = ?
        WHERE id = ?    
        """, ("SIM",id_mudar))
        conexao.commit()
        

    except Exception as erro:
        print(f"Se ferrou ai pai. Erro = {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

def remover_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o ID do livro que deseja deletar: "))

        cursor.execute("DELETE FROM livros WHERE id=?", (id_livro,))
        conexao.commit()
        #Verificar se o item foi deletado
        if cursor.rowcount > 0:
            print("Aluno removido com sucesso")
        else:
            print("Nenhum aluno cadastrado com o ID fornecido")
    except Exception as erro:
        print(f"Errp ap tentar excluir o aluno. Erro = {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()
