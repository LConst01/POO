class Carro:
    def __init__(self, ano, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.som_ligado = False
        self.velocidade = 0

    def buzinar(self):
        print(f"O {self.modelo} da cor {self.cor} está buzinando: BEEP BEEP!")
    
    def acelerar(self, incremento=10):
        self.velocidade += incremento
        print(f"O {self.modelo} acelera e está a {self.velocidade} km/h!")
        
    def cavalinho_de_pau(self):
        if self.velocidade > 0:
            print(f"O {self.modelo} fez um cavalinho de pau a {self.velocidade} km/h! OMG")
        else:
            print(f"O {self.modelo} está parado e não pode fazer um cavalinho de pau.")
        
    def ligar_som(self):
        if not self.som_ligado:
            self.som_ligado = True
            print(f"O som do {self.modelo} está ligado")
        else:
            print(f"O som do {self.modelo} já está ligado")
            
    
    def desligar_som(self):
        if self.som_ligado:
            self.som_ligado = False
            print(f"O som do {self.modelo} está desligado")
        else:
            print(f"O som do {self.modelo} já está desligado.")
            
meu_carro = Carro(2008, "Tempra", "Azul Goiaba")

meu_carro.buzinar()
meu_carro.acelerar(90)
meu_carro.ligar_som()
meu_carro.ligar_som()
meu_carro.desligar_som()
meu_carro.desligar_som()
meu_carro.cavalinho_de_pau