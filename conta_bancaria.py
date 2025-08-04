class ContaBancaria:
    def __init__(self, titular, salario_inicial=0):
        self.__titular = titular
        self.__saldo = salario_inicial 
    
    #Método público para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso")
        else:
            print("Valor de depósito inválido")
     
    #Método público para sacar      
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso")
        else:
            print("Saldo insuficiente ou valor inválido para saque")
    
    #Método público para consultar o saldo
    def consultar_saldo(self):
        return self.__saldo
    
    '''Getter| Setter
    Getter: é um método usado para obter(ler) o valor de um atributo privado de uma classe
    Setter: é usado para definir(escrever) ou alterar o valor de um atributo privado de uma classe'''
    
    #Getetr para titular(somente leitura)
    @property #getter - cria um método que pode ser acessado como se fosse um atributo 
    def titular(self):
        return self.__titular
    
    #uasar classe 
conta = ContaBancaria("João Silva", 1000)
print(conta.titular) #Saída: João
print(conta.consultar_saldo()) #Saída: 1000

conta.depositar(500) #Depósito
print(conta.consultar_saldo())

conta.sacar(200)
print(conta.consultar_saldo())

#print(conta.__saldo) gera erro 

