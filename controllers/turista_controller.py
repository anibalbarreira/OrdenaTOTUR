from models.turista_model import Turista

class TuristaController:
    def cadastrar_turista(self, Nome, Email, Telefone, Cidade, Nacionalidade):
        if not self.validar_email(Email):
            raise ValueError("Email inválido.")
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

    def validar_email(self, email):
        return "@" in email and "." in email