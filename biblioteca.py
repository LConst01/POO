class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo 
        self.autor = autor

def main():
    #criar lista de livros disponíveis
    livros = [
        Livro("Senhor dos Anéis", "J.R.R. Tolkien"),
        Livro("Harry Potter", "J.K. Rowling"), 
        Livro("A Roda do Tempo", "Robert Jordan"),
        Livro("O Nome do Vento", "Patrick Rothfuss"),
        Livro("As Crônicas de Nárnia", "C.S. Lewis"),
        Livro("Eragon", "Christopher Paolini"),
        Livro("A Canção do Sangue", "Anthony Ryan"),
        Livro("O Poder da Espada", "Joe Abercrombie"),
        Livro("Percy Jackson e os Olimpianos", "Rick Riordan"),
        Livro("O Castelo Animado", "Diana Wynne Jones")
    ]

    #solicitar nome do usuário
    nome = input("Digite o seu nome: ")

    #exibir lista de livros disponíveis
    print("\n Livros disponíveis para empréstimo: ")
    for i, livro in enumerate(livros, start=1):
        print(f" {i}. {livro.titulo} - {livro.autor}")

    #solicitar a escolha do livro pelo usuário
    while True:
        escolha = int(input("Digite o número do livro que deseja pegar emprestado: "))
        if 1 <= escolha <= len(livros):
            livro_selacionado = livros[escolha -1]
            break
        else:
            print(f"Por favor, digite um número entre 1 e {len(livros)}.")

    print(f"\n Epréstimo confirmado!")
    print(f"{nome} pegou emprestado o livro {livro_selacionado.titulo} de {livro_selacionado.autor}")

main()