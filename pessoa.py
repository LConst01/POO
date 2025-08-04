class Pessoa:
    def __init__(self, nome,  idade):
        self.nome =  nome #atributo público
        self.__idade = idade #atributo privado
    
    def mostra_idade(self):
        print(f"Idade: {self.__idade}")

p = Pessoa("ET-Bilu", 2005802)
print(p.nome)#acesso público
p.mostra_idade() #acesso privado via método

# print(p.__idade) erro