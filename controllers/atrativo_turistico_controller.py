from models.atrativo_turistico_model import Atrativo_turistico

class Atrativo_turisticoController:
    def cadastrar_atrativo_turistico(self, Nome, Tipo, Cidade, Preco):
       Atrativo_turistico = Atrativo_turistico(Nome, Tipo, Cidade, Preco)
       Atrativo_turistico.salvar()
       return Atrativo_turistico

    def listar_Atrativo_turistico(self):
        return Atrativo_turistico.buscar_todos()

    def atualizar_Atrativo_turistico(self, Nome, Tipo, Cidade, Preco):
        Atrativo_turistico = Pacote(Nome, Tipo, Cidade, Preco, id)
        Atrativo_turistico.salvar()
        return Atrativo_turistico

    def excluir_Atrativo_turistico(self, id):
        Atrativo_turistico = Atrativo_turistico.buscar_por_id(id)
        if Atrativo_turistico:
            Atrativo_turistico.deletar()
            return True
        return False
    