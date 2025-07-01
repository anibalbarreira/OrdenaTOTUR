from views.acoes_view import TelaAcoes
from controllers.turista_controller import TuristaController
class AcoesController:
    def __init__(self, root):
        self.root = root
        self.view = TelaAcoes(self)

    def iniciar_tela(self):
        self.view.mostrar()
'''
    def abrir_cadastro_turista(self):
        turista_controller = TuristaController(self.root)
        tela_cadastro_turista = TelaCadastroTurista(turista_controller, self.root)
        self.root.withdraw()
        tela_cadastro_turista.mostrar()'''