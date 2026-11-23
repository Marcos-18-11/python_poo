import csv
class Empleado:
    def __init__(self,nombre,edad,salario,departamento):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario
        self.departamento=departamento
        
class Gestor_Empleados:
    def __init__(self,dir):
        self.dir=dir
    def alta_empleado(self,empleado):
        with open(self.dir,"a",newline="") as f:
            csv.writer(f).writerow([empleado.nombre,empleado.edad,empleado.salario,empleado.departamento])

    def buscar_empleado(self,nombre):
       with open(self.dir,"r") as f:
            for e in csv.reader(f):
                if e[0]==nombre:
                    return Empleado(e[0],int(e[1]),float(e[2]),e[3])
            return None
    def empleados_departamento(self,departamento):
        with open(self.dir,"r") as f:
            datos=list(csv.DictReader(f))
            return [Empleado(e["empleado"],int(e["edad"]),float(e["salario"]),e["departamento"]) for e in datos if e["departamento"]==departamento]
        