# **Contagem Estoque**

Este software foi desenvolvido para ajudar a ter o controle das operações de uma empresa de forma mais simples, centralizada e eficaz. <br>

## **Funcionalidades Principais:**

* **`Contagem Bebidas`**: Permite o usuário contar o estoque de bebidas e enviar a quantidade contada por meio de um arquivo csv.

* **`Contagem Doces`**: Também permite o usuário contar o estoque de doces e enviar a quantidade contada por um arquivo csv.

* **`Contagem Geladeiras`**: Permite que o usuário conte o estoque de equipamentos e envie a contagem por meio de um arquivo csv.

* **`Contagem Datas`**: Possibilita o usuário contar o todas as datas de todos os pallets do estoque, e depois enviar um arquivo csv com a contagem.

## **Estrutura do Arquivo CSV**

### Contagem Estoque
* `codigo` - Armazena o Código do Produto.
* `nome` - Armazena o Nome do Produto.
* `quantidade` - Contém a quantidade contada pelo usuário.

### Contagem Doces
* `codigo` - Armazena o Código do Produto.
* `nome` - Armazena o Nome do Produto.
* `quantidade` - Contém a quantidade contada pelo usuário.

### Contagem Geladeiras
* `codigo` - Contém o código do equipamento.
* `quantidade`  - Nesse caso só 1 (um equipamento por código).

### Contagem Datas
* `id` - Armazena o id do pallet.
* `rua` - A rua em que o pallet está.
* `bloco` - O bloco em que o pallet está.
* `coluna` - A coluna do pallet.
* `nivel` - O nível em que se encontra o pallet.
* `codigo_produto` - O código do produto que está armazenado no pallet.
* `nome` - O nome do produto.
* `data_fabricacao` - A data de fabricação.
* `data_validade` - A data da validade.


## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **HTML5 e CSS3**
- **Sqlite3 3.45.3+**

## **Framework Utilizado**

- **Flask**

## **Banco de Dados**

- **`app.db`** - É o banco de dados principal, contém todas as tabelas.

<br>

## **Estrutura do Projeto**

```

|
├── archives/
|   ├── exports/
|   |   ├── contagem_datas/
|   |   ├── contagem_estoque/
|   |   ├── contagem_estoque_doces/
|   |   ├── contagem_geladeiras/
|   ├── imports/
│  
├── constants/
|   ├── __init__.py
|   ├── bancos_dados.py
|   ├── layout_estoque.py
|   ├── lista_produtos.py
|   ├── paths.py
|
├── database/
|   ├── __init__.py
|   ├── app.db
│   ├── banco_dados_principal.py
│   ├── tabela_contagens_datas_temporarias.py
│   ├── tabela_contagens_datas.py
│   ├── tabela_contagens_temporarias.py
│   ├── tabela_contagens.py
│   ├── tabela_usuarios.py
|
├── models/
|   ├── __init__.py
|   ├── contagem_temporaria.py
|   ├── contagens_datas_temporaria.py
|   ├── contagens_datas.py
|   ├── contagens.py
|   ├── usuarios.py   
|
├── routes/
|   ├── __init__.py
|   ├── cadastro.py
|   ├── carregar_contagem_temporaria.py
|   ├── contagem_datas.py
|   ├── contagem_doces.py
|   ├── contagem_estoque.py
|   ├── contagem_geladeira.py
|   ├── homepage.py
|   ├── login.py
|   ├── relatorio_entrada.py
|   ├── salvar_contagem_datas_temporaria.py
|   ├── salvar_contagem_datas.py
|   ├── salvar_contagem_doces.py
|   ├── salvar_contagem_geladeira.py
|   ├── salvar_contagem_temporaria.py
|   ├── salvar_contagem.py
|   ├── selecionar_contagem.py
|
├── scripts/
|   ├── __init__.py
|   ├── gerador_pdf.py
|   ├── ler_arquivo_xml.py
|   ├── salvar_arquivo_contagem_datas.py
|   ├── salvar_arquivo_contagem_doces.py
|   ├── salvar_arquivo_contagem_estoque.py
|   ├── salvar_arquivo_contagem_geladeiras.py
|
├── services/
|   ├── __init__.py
|   ├── contagem_datas.py
│   
├── static/
|   ├── css/
|   |   ├── cadastro.css
|   |   ├── contagem_datas.css
|   |   ├── contagem_doces.css
|   |   ├── contagem_estoque.css
|   |   ├── contagem_geladeira.css
|   |   ├── homepage.css
|   |   ├── login.css
|   |   ├── relatorio_entrada.css
|   |   ├── salvar_contagem.css
|   |   ├── selecionar_contagem.css
|   |
|   ├── images/
|   |   ├── cabeçalho.png
|   |   ├── logo_dbcambui_1.png
|   |   ├── logo_dbcambui_2.png
|   |   ├── logout_icon.png
|
├── templates/
|   ├── cadastro.html
|   ├── contagem_datas.html
|   ├── contagem_doces.html
|   ├── contagem_estoque.html
|   ├── contagem_geladeiras.html
|   ├── homepage.html
|   ├── login.html
|   ├── relatorio_entrada.html
|   ├── salvar_contagem.html
|   ├── selecionar_contagem.html
|
│   ├── validadores/
|   │   ├── __init__.py
|   │   ├── validar_cadastro.py
|   │   ├── validar_login.py
│   
├── .gitignore
├── app.py
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
