import random



class adivinador:
    def __init__(self):
        self.respuesta = [0, 1, 2, 3]
        self.intentos = 0
        self.picas = 0
        self.fijas =0
        self.combinations = []
        for num1 in range(10):
            for num2 in range(10):
                for num3 in range(10):
                    for num4 in range(10):
                        if len(set([num1, num2, num3, num4])) == 4:  # Ensure all digits are different
                            self.combinations.append([num1, num2, num3, num4])
    
    
    def eliminar(self):
        self.combinations = [comb for comb in self.combinations if self.calcular(comb) == (self.picas, self.fijas)]


    
    def calcular(self,combinacion):
        aux_picas = 0
        aux_fijas = 0
        i = 0
        for i in range(len(combinacion)):
            if combinacion[i] == self.respuesta[i]:
                aux_fijas += 1
            elif combinacion[i] in self.respuesta:
                aux_picas += 1
            
        return (aux_picas, aux_fijas)
        
    
    def seleccionar(self):
        
        mejor_score = float('inf')
        mejor_guess = None
        for code in self.combinations:
            scores = [0] * len(self.combinations)
            for guess in self.combinations:
                response = self.calcular(guess)
                if response != self.calcular(code):
                    scores[self.combinations.index(guess)] += 1
            score = max(scores)
            if score < mejor_score:
                mejor_score = score
                mejor_guess = code
        self.respuesta = mejor_guess

    def adivinar(self, picas, fijas):
        self.picas = picas
        self.fijas = fijas
        self.eliminar()
        self.seleccionar()
        print(len(self.combinations))
        return self.respuesta
            
            




intentos = 1
adivinador = adivinador()
print([0, 1, 2, 3])
gano = False
while gano == False:
    picas = int(input("picas: "))
    fijas = int(input("fijas: "))
    if fijas == 4:
        print("Gané")
        print("intentos: ", intentos)
        break
    if (fijas > 4) or (picas > 4):
        print("no son numeros validos, por favor ingresa numeros validos")
    
    if (fijas+picas > 4):
        print("no son numeros validos, por favor ingresa numeros validos")
    
    else:
        print(adivinador.adivinar(picas, fijas))
    
    intentos+=1

