####### Esse outro esquema funciona a mesma maneira do arquivo aula_property

class MinhaClasse:
    def __init__(self, valor):
        self._atributo = valor
    
    @property
    def atributo(self):
        return self._atributo
    
    @atributo.setter
    def atributo(self, valor):
        self._atributo = valor
        
obj = MinhaClasse(10)
# O atributo trabalha como uma função
obj.atributo = 20 # (set)
# Saída semelhante a uma variável
print(obj.atributo) # (get)