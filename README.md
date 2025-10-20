# **Contagem Estoque**

Este software foi desenvolvido para ajudar a ter o controle do estoque de uma empresa de forma mais simples, centralizada e eficaz. <br>
Ele disponibiliza uma forma de contar o estoque e depois posteriormente usá-lo em outro sistema.

## **Funcionalidades Principais:**

* **`Contar Estoque`**: Permite o usuário contar o estoque e enviar a quantidade contada por meio de um arquivo csv.

## **Estrutura do Arquivo CSV**

* `codigo` - Armazena o Código do Produto.
* `nome` - Armazena o Nome do Produto.
* `quantidade` - Contém a quantidade contada pelo usuário.



## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **HTML5 e CSS3**
- **Sqlite3 3.45.3+**

## **Framework Utilizado**

- **Flask**

## **Banco de Dados**

- **`produtos.db`** - Usado para armazenar todos os dados dos produtos da empresa.

<br>

- **`contagem_temporarias.db`** - Ele armazena as contagens temporárias do usuário, como uma forma de backup da contagem feita por ele, caso ocorra algum problema de conexão.

<br>

- **`usuarios.db`** - Armazena todos os usuários cadastrados na aplicação.

<br>

## **Estrutura do Projeto**

```

├── app.py
|
├── arquivos/
|   ├── contagem_estoque.py
|   ├── PRODUTOS.CSV.py
│  
├── backend/
|   │   
|   ├── __init__.py
|   |
|   ├── models/
|   │   ├── __init__.py
|   │   ├── contagem.py
|   │   ├── produtos.py
|   │   ├── usuarios.py
|   |
│   ├── validadores/
|   │   ├── __init__.py
|   │   ├── validar_cadastro.py
|   │   ├── validar_login.py
|   
├── database/
|   ├── __init__.py
│   ├── banco_dados_contagem.py
│   ├── banco_dados_produtos.py
│   ├── banco_dados_usuarios.py
|
├── routes/
|   ├── __init__.py
|   ├── cadastro.py
|   ├── contagem_estoque.py
|   ├── homepage.py
|   ├── login.py
|   ├── salvar_contagem.py
|   ├── salvar_contagem_temporaria.py
|   ├── carregar_contagem_temporaria.py
|
├── scripts/
|   ├── __init__.py
|   ├── processar_arquivo_parametros.py
|   ├── salvar_arquivo_contagem_estoque.py
│   
├── static/
|   ├── css/
|   |   ├── cadastro.css
|   |   ├── contagem_estoque.css
|   |   ├── homepage.css
|   |   ├── login.css
|   |   ├── salvar_contagem.css
|   |
|   ├── images/
|   |   ├── logo_dbcambui_1.png
|   |   ├── logo_dbcambui_2.png
|   |   ├── logout_icon.png
|
├── templates/
|   ├── cadastro.html
|   ├── contagem_estoque.html
|   ├── homepage.html
|   ├── login.html
|   ├── salvar_contagem.html
│   
├── .gitignore
├── README.md

```

## **Como Executar**


1. Execute o `app.py`.
   ```bash
   python app.py
   ```

## **Autoria**
- Lucas Pereira Silva Mello

<br>

Fique à vontade para contribuir!
