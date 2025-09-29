import funções as fnc
import sqlite3


while True:
    print(f"""
-----------------------------
          SISTEMA 
         BIBLIOTECA
-----------------------------
          
    1 - Cadastrar livros
          
    2 - Mostrar os livros cadastrados
          
    3 - Alterar a disponibilidade de livros
        
    4 - Remover um livro cadastrado
          
    5 - Sair do sistema
          
-----------------------------

    """)
    escolha = int(input("Digite um numero para realizar a ação: "))
    if escolha == 1:
        fnc.cadastrar_livros()
    elif escolha == 2:
        fnc.mostrar_livros()
    elif escolha == 3:
        fnc.atualizar_livro()
    elif escolha == 4:
        fnc.remover_livro()
    elif escolha == 5:
        print("Ate a proxima")
        break
    else:
        print("Insira um numero valido")





