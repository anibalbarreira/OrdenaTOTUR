from views.acoes_view import TelaAcoes

class AcoesController:
    def __init__(self, root):
        self.root = root
        self.view = TelaAcoes(self)

    def iniciar_tela(self):
        self.view.mostrar()