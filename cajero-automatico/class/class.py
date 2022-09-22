


lista=[]


class Usuario:
    importeExtraccion=''
    def __init__(self,nombre,clave,prestamo=3000000,saldo=100000,CBU=3216591256):
        self.nombre=nombre
        self.clave=clave
        self.prestamo=prestamo
        self.saldo=saldo
        self.CBU=CBU
        
    def extraccion(self):
        print('Saldo disponible: ',f'{self.saldo}')
        importeExtraccion=int(input('Monto extracción'))
        while importeExtraccion>self.saldo:
             print('No posee ese monto de extracción')
             importeExtraccion=int(input('Monto extracción'))
             
         
        # saldoActual=self.saldo-importeExtraccion
        print(self.saldo-importeExtraccion)
        return self.saldo
        
    def transferencia(self):
        print(self.saldo)
        
            

            
            
            
usuario=Usuario(input('Ingrese nombre: '),int(input('Ingrese clave numérica: ')))
guardoUsuario=usuario.nombre, usuario.clave
lista.append(guardoUsuario)
print(lista)

opciones = int(input(
     'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir.\n '))
while opciones != 6:
       if opciones == 1:    
        usuario.extraccion()
        opciones = int(input(
             'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))
       elif opciones == 2:
            usuario.transferencia()
            opciones = int(input(
                'Que operaciones desea realizar: \n 1: Extracción. \n 2: Transferencia. \n 3: Consulta de saldo. \n 4: Crear cuenta. \n 5: Consulta de CBU. \n 6: Salir. \n '))

