from models.pacote_atrativo_model import Pacote_atrativo

class Pacote_atrativoController:
    def Pacote_atrativo(self, Nome, Descricao, Preco):
        Pacote_atrativo = Pacote_atrativo(Nome, Descricao, Preco)
        Pacote_atrativo.salvar()
        return Pacote_atrativo

    def listar_pacote_atrativo(self):
        return Pacote_atrativo.buscar_todos()

    def atualizar_pacote_atrativo(self, Nome, Descricao, Preco):
        Pacote_atrativo = Pacote_atrativo(Nome, Descricao, Preco id)
        Pacote_atrativo.salvar()
        return Pacote_atrativo

    def excluir_turista(self, id):
        Pacote_atrativo = Pacote_atrativo.buscar_por_id(id)
        if Pacote_atrativo:
            Pacote_atrativo.deletar()
            return True
        return False
    