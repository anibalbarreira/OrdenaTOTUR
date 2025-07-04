from views.acoes_view import TelaAcoes
from controllers.turista_controller import TuristaController
from controllers.pacote_controller import CadastroPacoteController
from controllers.atrativo_turistico_controller import CadastroAtrativoturisticoController
import tkinter as tk

class AcoesController:
    def __init__(self, root):
        self.root = root
        self.view = TelaAcoes(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
    
    def abrir_cadastro_turista(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        TuristaController(cadastro_window).iniciar_tela()

    def abrir_cadastro_atrativo_turistico(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        CadastroAtrativoturisticoController(cadastro_window).iniciar_tela()
    
    def abrir_cadastro_pacote(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        CadastroPacoteController(cadastro_window).iniciar_tela()

    def sair(self):
        self.root.quit()