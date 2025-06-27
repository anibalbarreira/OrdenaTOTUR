from models.pacote_model import Pacote

class PacoteController:
    def Pacote(self, Nome, Descricao, Duracao, Preco_total):
        Pacote = Pacote(Nome, Descricao, Duracao, Preco_total)
        Pacote.salvar()
        return Pacote

    def listar_pacote(self):
        return Pacote.buscar_todos()

    def atualizar_pacote(self, Nome, Descricao, Duracao, Preco_total):
        Pacote = Pacote(Nome, Descricao, Duracao, Preco_total, id)
        Pacote.salvar()
        return Pacote

    def excluir_turista(self, id):
        Pacote = Pacote.buscar_por_id(id)
        if Pacote:
            Pacote.deletar()
            return True
        return False
    