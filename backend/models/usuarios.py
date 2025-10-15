from database.banco_dados_usuarios import conectar_banco_dados_usuarios

class Usuario:
    def __init__(self, usuario_id, nome_completo, senha):
        self.usuario_id = usuario_id
        self.nome_completo = nome_completo
        self.senha = senha

    def inserir_usuario(self):

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        INSERT INTO TabelaUsuarios (usuario_id, nome_completo, senha)
        VALUES (?, ?, ?)
        """, (self.usuario_id, self.nome_completo, self.senha)
        )

        conexao.commit()
        conexao.close()

    @staticmethod
    def excluir_usuario(usuario_id, nome_completo, senha):
        
        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        DELETE FROM TabelaUsuarios
        WHERE usuario_id = ? AND nome_completo = ? AND senha = ? 
        """, (usuario_id, nome_completo, senha)
        )

        conexao.commit()
        conexao.close()
    
    @staticmethod
    def buscar_usuarios(nome_completo, senha):

        conexao = conectar_banco_dados_usuarios()
        cursor = conexao.cursor()

        cursor.execute(
        """
        SELECT * FROM TabelaUsuarios
        WHERE nome_completo = ? AND senha = ?
        """, (nome_completo, senha)
        )

        resultado = cursor.fetchone()

        conexao.commit()
        conexao.close()

        return Usuario(*resultado)