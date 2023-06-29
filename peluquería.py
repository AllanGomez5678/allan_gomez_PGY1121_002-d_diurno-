class peluqueria:
    codigo_ate=''
    nombre=''
    fecha=''
    descr=''
    costo=0

    def __int__(self):
        self.codigo_ate='A-001'
        self.nombre='S/A'
        self.fecha='00/00/000'
        self.descr='S/A'
        self.costo=45000

    def setCodigo_ate(self,codigo):
        if len(codigo) == 5:
            if codigo[0:1].isalpha() and codigo[1:2] == '-' and codigo[2:5].isdigit():
                self.codigo_ate = codigo
                return True
            else:
                print('Formato incorrecto (ej: "A-001"')
                return False
        else:
            print("Larco incorrecto, debe ser minimo 5 caracteres")
            return False

    def setNombre(self,nombre):
        if len(nombre) >= 5:
            self.nombre = nombre
            return True
        else:
            print("Nombre muy corto, minimo 5 caracteres")
            return False

    def setDescr(self,desc):
        if len(desc) >= 5 and len(desc) <= 45:
            self.descr = desc
            return True
        else:
            print("Formato incorrecto, debe ser entre 5 a 45 caracteres")
            return False

    def setCosto(self,precio):
        if precio >= 20000:
            self.costo = precio
            return True
        else:
            print("Costo muy bajo, debe ser mayor a 20000")
            return False