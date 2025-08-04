from abc import ABC, abstractmethod 
# from <módulo> import <nome>
# módulo: noem do módulo ou pacote que irá importar 
# nome: nome da função, classe, variável ou submódulo que deseja importar
# import React from react
'''Classe abstrata: classe que não pode ser instanciada diretamente (não consigo criar) 
objetivos diretamente nela. Definimos regras que devem ser obedecidas'''
# Curso no geral
class Curso(ABC):
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []
    
    def inscrever_alunos(self,aluno,matricula):
        self.alunos.append((aluno, matricula))
        print(f"Aluno {aluno} com matícula nº {matricula}, inscrito no curso {self.nome}.")
    
    @abstractmethod
    def info_curso(self):
        pass
    
    def info_alunos(self): 
        print(f"Alunos inscritos no curso {self.nome}:")
        for aluno,  matricula in  self.alunos:
            print(f"-Nome: {aluno},  Matrícula: {matricula}")
    
# Curso específico
class CursoMatematica(Curso):
    def info_curso(self):
        print (f"Curso de {self.nome}: Foco em álgebra e geometria")

    
        
# Curso específico       
class CursoHistoria(Curso):
    def info_curso(self):
        print (f"Curso de {self.nome}: Foco em história mundial e cultura")
        
#testar
curso1 = CursoMatematica("Matemática")
curso2 = CursoHistoria("História")

curso1.inscrever_alunos("Lucca", "RES0145330")
curso1.inscrever_alunos("Breno", "RES0125681")
curso1.info_curso()

curso2.inscrever_alunos("Fernando", "RES0139448")
curso2.info_curso()

# crie a função info_alunos()
curso1.info_alunos()
curso2.info_alunos()

# inserir 