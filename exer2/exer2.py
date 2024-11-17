class livro():
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
class biblioteca():
    def __init__(self,tt,at,ap):
        self.tt = tt
        self.at = at 
        self.ap = ap
def adicionar_bb():
    for adicao in prat:
        tt = adicao.titulo
        at = adicao.autor 
        ap = adicao.ano_publicacao
        bib = biblioteca(tt,at,ap)
        bb.append(bib)
bb = []
prat = []
def adicionar_livro():
    titulo = input("Digite um titulo: ")
    autor = input("Digite o nome do autor: ")
    ano_publicacao = int(input("Digite o ano de publicação: "))
    adicao = livro(titulo,autor,ano_publicacao)
    prat.append(adicao)
def exibir():
    for bib in bb:
        print("-"*20)
        print("TITULO: ",bib.tt)
        print("AUTOR: ",bib.at)
        print("ANO DE PUBLICAÇÂO: ",bib.ap)
        print("-"*20)
        print("#"*20)
def remover():
    print("#")
    print("REMOVER")
    print("#")
    titulo_remover = input("Remover Titulo: ")
    titulo_autor = input("Remover Autor: ")
    titulo_ano = input("Remover ano: ")
    encontrado = False
    for bib in bb:
        if bib.tt == titulo_remover:
            bb.remove(bib)
            encontrado = True
            print("Titulo ",titulo_remover,"removido")
        if bib.tt == titulo_autor:
            bb.remove(bib)
            encontrado = True
            print("Autor ",titulo_autor,"removido")
        if bib.tt == titulo_ano:
            bb.remove(bib)
            encontrado = True
            print("Ano de Publicação ",titulo_ano,"removido")
        
while True:
    print("O que deseja?")
    print("1- Ver livros")
    print("2- Adicionar livros")
    print("3- Remover livros")
    print("4- Sair")
    esc = int(input("Escolha: "))
    if esc == 1:
        exibir()
    elif esc ==2:
        adicionar_livro()
        adicionar_bb()
    elif esc==3:
        remover()
    elif esc ==4:
        break
    else:
        print("Tente novamente")

