class Usuario:
  def __init__(self, nome, tipo, idade):
    self.nome = nome
    self.tipo = tipo
    self.idade = idade
  
  def exibir_informacoes(self):
    return f"-{self.nome} {self.tipo} {self.idade}"
  
class Aluno(Usuario):
  def __init__(self, nome, idade):
    super().__init__(nome,'Aluno', idade)

class Professor(Usuario):
  def __init__(self, nome, idade):
    super().__init__(nome, 'Professor', idade)



class CadastraUsuario:
  def __init__(self): 
    self.cadastro = []  

  def funcao_cadastro(self, nome, tipo, idade):
    if tipo.lower() == 'aluno':
      usuario = Aluno(nome, idade)
    elif tipo.lower() == 'professor':
      usuario = Professor(nome, idade)
    
    self.cadastro.append(usuario)

  def exibir_cadastrados(self):
    for usuario in self.cadastro:
      print(usuario.exibir_informacoes())


cadastro = CadastraUsuario()

while True:
    opcao = input("\n1 - Fazer Cadastro\n2 - Exibir cadastrados\n3 - Sair\nDigite: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        while True:
          tipo = input("Tipo (Aluno ou Professor): ").strip().lower()
          if tipo.lower() != 'aluno' and tipo.lower() != 'professor':
            print("-------------")
            print("Por Favor,apenas digite 'Aluno' ou 'Professor'")
            tipo = input("Tipo (Aluno ou Professor): ").strip().lower()
          else:
            break
        while True:
          idade = input("Idade: ")
          if not idade.isdigit():
            print("Apenas use números")
            idade = input("Idade: ")
          else:
            idade = int(idade)
            break
          print("Cadastrado com sucesso!")
        cadastro.funcao_cadastro(nome, tipo, idade)
   
    elif opcao == "2":
        print("-------------")
        cadastro.exibir_cadastrados()
    elif opcao == "3":
      print("Saindo do sistema...")
      break
