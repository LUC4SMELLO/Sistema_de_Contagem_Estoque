from database.banco_dados_contagem import conectar_banco_dados_contagem

class Contagem:
    def __init__(self, data, usuario_id, codigo_produto, quantidade_contada):
        self.data = data
        self.usuario_id = usuario_id
        self.codigo_produto = codigo_produto
        self.quantidade_contada = quantidade_contada

    def inserir_contagem(self):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaContagem (
        data,
        usuario_id,
        codigo_produto,
        quantidade_contada
        )
        VALUES (?, ?, ?, ?)
        """, (self.data, self.usuario_id, self.codigo_produto, self.quantidade_contada)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def carregar_contagem(usuario_id):

        conexao = conectar_banco_dados_contagem()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT * FROM TabelaContagem
        WHERE usuario_id = ?
        """, (usuario_id,)
        )

        resultado = cursor.fetchall()

        conexao.commit()
        conexao.close()

        return Contagem(*resultado)
