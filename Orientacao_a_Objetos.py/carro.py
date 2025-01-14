# Classe: instruções de como funciona
# Carro.py

# Para criar a classe siga os passos:
# -> class (nome da classe):
# -> def __init__ (self):
        # pass 

class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0


    def ligar(self):
        if self.ligado:
            print("Carro já ligado. Nada acontece!")
        
        else:
            print(f"{self.modelo} ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print(f"{self.modelo} desligado")
            self.ligado = False
                   
        else:
            print("Carro já desligado. Nada acontece!")

    def acelerar(self):
        if self.ligado:
             self.velocidade += 1    
             print(f"{self.velocidade}km/h")  
        else:
            print("Não é possível acelerar, carro desligiado!")

    def frear(self):
        if self.ligado:
             self.velocidade -= 1    
             print(f"{self.velocidade}km/h")  
        else:
            print("Não é possível frear, carro desligiado!")