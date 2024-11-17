class carro():
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
ler = []
def adicionar_carro():
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))
    adicionar = carro(marca,modelo,ano)
    ler.append(adicionar)
def exibir():
    for adicionar in ler:
        print("Marca: ",adicionar.marca)
        print("Modelo: ",adicionar.modelo)
        print("Ano: ",adicionar.ano)
adicionar_porra()
exibir()