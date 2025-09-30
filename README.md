# 📚 Sistema de Gerenciamento de Biblioteca (SQLite3)

Um sistema simples em **Python + SQLite3** para gerenciar livros.  
Permite **cadastrar, listar, atualizar disponibilidade e remover** livros do banco de dados `biblioteca.db`.

---

## 🚀 Funcionalidades

- 📁 **Banco de dados automático** — Cria o arquivo `biblioteca.db` e a tabela `livros` se não existirem.  
- ✍️ **Cadastrar livros** com título, autor, ano e disponibilidade.  
- 📜 **Listar livros** cadastrados.  
- 🔄 **Atualizar disponibilidade** (SIM/NÃO) de um livro existente.  
- 🗑️ **Remover livros** pelo ID.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- **SQLite3** (biblioteca padrão do Python)

---

## 📂 Estrutura do Projeto
biblioteca/
│
├── biblioteca.db # Banco de dados SQLite3 (gerado automaticamente)
└── main.py # Script com todas as funções

yaml
Copiar código

---

## ⚙️ Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seuusuario/biblioteca.git
   cd biblioteca
Execute o script

bash
Copiar código
python main.py
Utilize as funções no terminal

cadastrar_livros() → cadastra um novo livro

mostrar_livros() → lista todos os livros cadastrados

atualizar_livro() → altera a disponibilidade (SIM/NÃO)

remover_livro() → remove um livro pelo ID

📝 Estrutura da Tabela livros
Campo	Tipo	Descrição
id	INTEGER	Identificador único (auto incremento)
titulo	TEXT	Nome do livro
autor	TEXT	Autor do livro
ano	INTEGER	Ano de lançamento
disponivel	TEXT	Status (SIM/NÃO)

🔎 Exemplo de Uso
bash
Copiar código
Digite o título da obra: Dom Casmurro
Digite o autor da obra: Machado de Assis
Digite o ano de lançamento da obra: 1899
Livro cadastrado com sucesso!
💡 Possíveis Melhorias
Criar menu interativo no terminal para navegar entre funções.

Adicionar busca por título ou autor.

Desenvolver uma interface gráfica usando Tkinter ou PyQt.
