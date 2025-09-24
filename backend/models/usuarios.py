from database.banco_dados_usuarios import conectar_banco_dados_usuarios

class Usuario:
    def __init__(self, nome_completo, senha):
        self.nome_completo = nome_completo
        self.senha = senha

    def inserir_usuario(self):

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaUsuarios (
        nome_completo,
        senha
        )
        """, (self.nome_completo, self.senha)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_usuario(nome_completo, senha):
        
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE FROM TabelaUsuarios
        WHERE nome_completo = ? AND senha = ?
        """, (nome_completo, senha)
        )

        conexao.commit()
        conexao.close()
    
    @staticmethod
    def buscar_usuarios(nome_completo, senha):

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT 1 FROM TabelaUsuarios
        WHERE nome_completo = ? AND senha = ?
        """, (nome_completo, senha)
        )

        conexao.commit()
        conexao.close()

        resultado = cursor.fetchone()

        return resultado