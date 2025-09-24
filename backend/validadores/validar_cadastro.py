from backend.models.usuarios import Usuario

def validar_cadastro(nome_completo, senha):

    resultado = Usuario.buscar_usuario(nome_completo, senha)
    if resultado:
        return False, "Nome de Usuário Já Encontrado."

    if not nome_completo or not senha:
        return False, "Todos os Campos Devem ser Preechidos."
    
    if len(senha) < 8:
        return False, "Tamanho da Senha Inválido."
    
    return True, "Cadastro Bem Sucedido!"
    