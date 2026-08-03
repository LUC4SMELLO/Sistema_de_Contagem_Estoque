from models.relatorios_entradas import RelatoriosEntradas


def salvar_relatorio_entrada(dados_relatorio: dict, usuario_id: int):
    """
    Salva o relatório de entrada no banco de dados e retorna uma mensagem.

    Parameters
    ----------
        dados_relatorio
            Um dicionário com os dados do relatório de entrada.
        usuario_id
            O id do usuário.
    
    Returns
    -------
        bool
            Verdadeiro se tudo certo, Falso caso tenha dado algum erro.
        mensagem
            Mensagem de sucesso ou do erro.
        erro
            A mensagem do erro, caso tenha algum.
    """

    try:
        
        RelatoriosEntradas.inserir_relatorio(usuario_id, dados_relatorio)

        # LÓGICA PARA EXCLUIR CONTAGEM TEMPORÁRIA AQUI

        return True, "<span class='mensagem-sucesso'>Sucesso ao Enviar o Relatório!</span>", ""

    except Exception as erro:
        return False, "<span class='mensagem-erro'>Erro ao Enviar a Contagem!</span>", erro
