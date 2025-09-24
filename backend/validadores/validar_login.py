from backend.models.usuarios import Usuario

def validar_login(nome_completo, senha):

    resultado = Usuario.buscar_usuario(nome_completo, senha)
    if not resultado:
        return False, "Usuário Não Encontrado."

    if not nome_completo or not senha:
        return False, "Todos os Campos Devem ser Preechidos."
    
    if len(senha) < 8:
        return False, "Tamanho da Senha Inválido."
    
    return True, "Login Bem Sucedido!"