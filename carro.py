class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f'O {self.modelo} está acelerando!')

    def frear(self):
        print(f'O {self.modelo} está freando!')

meu_carro = Carro('Vermelho', 'Ferrari', 2022)
outro_carro = Carro('Azul', 'BMW', 2020)

meu_carro.acelerar() # Saída: O Ferrari está acelerando!
outro_carro.frear() # Saída: O BMW está freando!