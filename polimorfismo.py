class Carro:
    def __init__(self,motor, rodas):
        self.motor = motor
        self.rodas = rodas
    
    def acelerar(self):
        return "O carro está acelerando normalmente"
    
class CarroEsportivo(Carro):
    def __init__(self, motor, rodas , turbo ):
        super().__init__(motor, rodas)
        self.turbo = turbo
    
    def acelerar(self):
        if self.turbo:
            return "O carro esportivo está acelerando com turbo! Vruum"
        else:
            return super().acelerar()
carro_normal = Carro("V6", 4)
carro_esportivo_com_turbo = CarroEsportivo("V8", 4, True)
carro_esportivo_sem_turbo = CarroEsportivo("V8", 4, False)

#lista de polimorfismo
veiculos = [carro_normal, carro_esportivo_com_turbo, carro_esportivo_sem_turbo]
for veiculo in veiculos:
    print(veiculo.acelerar)