# dados_exemplo.py
from crud.crud_livro import criar_livro
from crud.crud_aluno import criar_aluno
from crud.crud_professor import criar_professor
from crud.crud_bibliotecario import criar_bibliotecario
from crud.crud_diretor import criar_diretor
from crud.crud_supervisor import criar_supervisor
from crud.crud_reserva import criar_reserva
from crud.crud_emprestimo import criar_emprestimo
from crud.crud_sugestao import criar_sugestao
from crud.crud_historicoleitura import criar_historico
from crud.crud_relatorio import criar_relatorio
from crud.crud_livro import criar_livro as ci_livro
from crud.crud_livro import listar_livros

def popular():
    # categorias (assume que categoria CRUD existe; se ainda não, insera direto am SQL)
    # livro 
    ci_livro("Dom Casmurro", "Machado de Assis", isbn="97885775412621", sinopse="Romance Clássico", capa=None, quatidade=3, categoria_id=None)
    ci_livro("A Hora da Estrela", "Clarice Lispecto", isbn="9788535911500", sinopse="Romance", capa=None, quantidade=2, categoria_id=None)

    # alunos
    criar_aluno("João Silva", "joao@escola.local", "senha123", "9A")
    criar_aluno("Maria Oliveira", "maria@escola.local", "senha123", "8B")

    # professorores 
    criar_professor("Carlos Sousa", "carlos@escola.local", "senha123", disciplina="História")
    criar_professor("Patricia Lima", "patricia@escola.local", "senha123", disciplina="Português")

    # bibliotecario / diretor / supervisor
    criar_bibliotecario("Ana Bibli", "ana.bibli@escola.local", "senha123")
    criar_diretor("João Diretor", "joão.dir@escola.local", "senha123")
    criar_supervisor("Supervisor X", "supx@escola.local", "senha123")

    # empéstimo exemplo (aluno 1 pega livro 1)
    criar_emprestimo(1,1)
    # reserva exemplo
    criar_reserva(2,2)
    # sugestão
    criar_sugestao("Livro Novo", "Autor X", "Ficção", "Seria bom ter este livro.", aluno_id=1)
    # histórico
    criar_historico(1,1)
    # relatório exemplo
    criar_relatorio("mensal", "2025-08-01", "2025-08-31", gerado_por_bibliotecario=1)

    print("Dados de exemplo inseridos (verifique ids a tabelas).")

if __name__ == "__main__":
    popular()