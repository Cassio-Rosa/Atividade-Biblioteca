import funções_streamlit as fst
import streamlit as st
import pandas as pd



aba1,aba2,aba3,aba4 = st.tabs(["Cadastrar Livros", "Mostrar os livros", "Remover um livro","Mudar a disponibilidade"])
with aba1:
    fst.cadastrar_livros()
with aba2:
    fst.mostrar_livros()
with aba3:
    fst.remover_livro()
with aba4:
    fst.atualizar_livro()