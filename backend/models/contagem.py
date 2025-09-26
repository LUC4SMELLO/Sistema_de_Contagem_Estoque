from database.banco_dados_contagem import conectar_banco_dados_contagem

class Contagem:
    def __init__(self, data, usuario, codigo_produto, quantidade_contada):
        self.data = data
        self.usuario = usuario
        self.codigo_produto = codigo_produto
        self.quantidade_contada = quantidade_contada

    def inserir_contagem(self):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaContagem (
        data,
        usuario,
        codigo_produto,
        quantidade_contada
        )
        VALUES (?, ?, ?, ?)
        """, (self.data, self.usuario, self.codigo_produto, self.quantidade_contada)
        )

        conexao.commit()
        conexao.close()
