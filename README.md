# **Contagem Estoque**

Este software foi desenvolvido para ajudar a ter o controle do estoque de uma empresa de forma mais simples, centralizada e eficaz. Para isso ele conta com diversas funcionalidades para ajudar.

## **Funcionalidades Principais:**

### 
* **`FUNCIONALIDADE`**: 

## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **Tkinter 8.4+**
- **Sqlite3 3.45.3+**

## **Banco de Dados**

- **`PRODUTOS`** - 
## **Estrutura do Projeto**

```

├── app.py

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
   python main.py
   ```

## **Autoria**
- Lucas Pereira Silva Mello

<br>

Fique à vontade para contribuir!
