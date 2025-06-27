from models.agencia_model import Turista

class agenciaController:
    def cadastrar_turista(self, Nome, Email, Telefone, Cidade, Nacionalidade):
        turista = turista(Nome, Email, Telefone, Cidade, Nacionalidade)
        turista.salvar()
        return turista

    def listar_turista(self):
        return Turista.buscar_todos()

    def atualizar_turista(self, id, nome, email, telefone):
        Turista = Turista(nome, email, telefone, id)
        Turista.salvar()
        return Turista

    def excluir_turista(self, id):
        turista = Turista.buscar_por_id(id)
        if turista:
            turista.deletar()
            return True
        return False
    