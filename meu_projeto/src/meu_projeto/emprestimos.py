from livros import Livro
from usuarios import Usuario

class Emprestimo(Livro, Usuario):
    def __init__(self, livro : Livro, usuario : Usuario):
        if Livro.disponivel == False:
            raise ValueError
        
        self.livro = Livro
        self.usuario = Usuario
        self.ativo = True

        Livro.disponivel = False

    def devolver(self):
        self.ativo = False
        Livro.disponivel = True

    


