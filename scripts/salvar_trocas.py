from models.trocas import Trocas


def salvar_troca(usuario_id: int, troca: dict):

    try:
        Trocas.inserir_troca(usuario_id, troca)

        return True, "<span class='mensagem-sucesso'>Sucesso ao Adicionar a Troca!</span>", ""

    except Exception as erro:
        return False, "<span class='mensagem-erro'>Erro ao Adicionar a Troca!</span>", erro
