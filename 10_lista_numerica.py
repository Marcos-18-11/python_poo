#crear una subclase de list para el almacenamiento de números con las siguientes características:
#incluirá los métodos:
#sum(). Devuelve la suma de los números almacenados
#mean(). Devuelve la media de los números almacenados
#Además de esos métodos, el constructor recibirá un parámetro booleano que, en caso de ser true
#impedirá que repitan números


    
class Lista_Numerica(list):
    def __init__(self, unique):
        self.unique=unique
        super().__init__()
    def sum(self):
        return sum(self)
    def mean(self):
        if len(self)==0:
            return 0
        return sum(self)/len(self)
    def append(self, object):
        if not isinstance(object,(int,float)): #impide que se añadan datos no numéricos
            return None
        if self.unique and object in self:
            return None
        return super().append(object)

lst=Lista_Numerica(True)
lst.append(5.5)
lst.append(10)
lst.append(5)
lst.append("hello")
print(f"Suma total: {lst.sum()}")
print(f"Media: {lst.mean()}")
print(lst)