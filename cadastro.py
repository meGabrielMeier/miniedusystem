class Usuario:
  def __init__(self, nome, tipo, idade):
    self.nome = nome
    self.tipo = tipo
    self.idade = idade
  
  def exibir_acao(self):
    return f"{self.tipo} {self.nome} parabéns pelos seus {self.idade} anos."
  
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
    if tipo.lower() == 'aluno' or 'aluna':
      usuario = Aluno(nome, idade)
    elif tipo.lower() == 'professor' or 'professora':
      usuario = Professor(nome, idade)
    else:
      raise ValueError("Erro, apenas digite 'Aluno' ou 'Professor'!")
    
    self.cadastro.append(usuario)

  def exibir_cadastrados(self):
    for usuario in self.cadastro:
      print(usuario.exibir_informacoes())


cadastro = CadastraUsuario()

while True:
    opcao = input("\n1 - Fazer Cadastro\n2 - Exibir cadastrados\n3 - Sair\nDigite: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        tipo = input("Tipo (Aluno ou Professor): ")
        idade = input("Idade: ")
        cadastro.funcao_cadastro(nome, tipo, idade)
    elif opcao == "2":
        print("-------------")
        cadastro.exibir_cadastrados()
        break
    elif opcao == "3":
      print("Saindo do sistema...")
      break
