class funcionario ():
  def __init__(self,nome,salario):
    self.nome = nome
    self.salario = salario
def salario_adic():
  nome = input("Digite o nome do  funcionario: ")
  for adicao in quadro:
    
    if nome == adicao.nome:
      print(adicao.salario)
      adc = int(input("Favor, digite o aumento do usuario: "))
      adc = adc/100
      sal = adicao.salario * adc
      adicao.salario = adicao.salario + sal
      print(adicao.salario)
      continue
def remover():
  print("#"*20)
  print("REMOVER")
  print("#"*20)
  nome = input("Digite o nome do funcionario: ")
  for adicao in quadro:
    if nome == adicao.nome:
      quadro.remove(adicao)
      print("Removido")
      continue

quadro = []
def adicionar():
  nome = input("Digite o nome do funcionário: ")
  salario = int(input("Digite o salario do funcionário: "))
  adicao = funcionario(nome,salario)
  quadro.append(adicao)
def exibir():
  for adicao in quadro:
    print("-"*20)
    print("Nome: ",adicao.nome)
    print("Salario: ",adicao.salario)
    print("-"*20)
while True:
  print("Escolha um numero para seguir:")
  print("1 - Ver funcionarios")
  print("2 - Adicionar funcionarios")
  print("3 - aumentar salario dos funcionarios")
  print("4 - Remover funcionario")
  print("5 - sair")
  esc = int(input("Escolha: "))
  if esc == 1:
    exibir()
  elif esc == 2:
    adicionar()
  elif esc == 3:
    salario_adic()
  elif esc == 4:
    remover()
  elif esc ==5:
    break
  else:
    print("Houve um erro, digite novamente")