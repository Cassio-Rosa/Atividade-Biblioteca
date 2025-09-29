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
    ano DATE,
    disponivel TEXT               
    )
""")