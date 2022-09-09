# mensajeNuevo=input("ingrese mensaje: ")
# print(mensajeNuevo)

# a = 10
# b = 20
# c = 3
# if a < b:
#     print('verdadero')
# else:
#     print('falso')

# if c != b:
#     print('si, es distinto \t\t jajjajaj')

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista2 = []
# for i in lista:
#     # print(i)
#     print(i)


# mensajeNuevo = int(
#     input('ingrese opción 1\ deposito, 2\extraccion, 3\transferencia, 4\ salir '))
# while mensajeNuevo != 4:
#     if mensajeNuevo == 1:
#         cargaDeposito = int(input('monto de carga: '))
#         print(cargaDeposito)
#         mensajeNuevo = int(
#             input('ingrese opción 1\ deposito, 2\extraccion, 3\transferencia, 4\ salir '))
#     elif mensajeNuevo == 2:
#         extraccion = int(input('monto de extraccion: '))
#         print(extraccion)
#         mensajeNuevo = int(
#             input('ingrese opción 1\ deposito, 2\extraccion, 3\transferencia, 4\ salir '))
#     elif mensajeNuevo == 3:
#         transferencia = int(input('monto de transferencia: '))
#         print(transferencia)
#         mensajeNuevo = int(
#             input('ingrese opción 1\ deposito, 2\extraccion, 3\transferencia, 4\ salir '))


# range==> recorre
# primer parámetro==>inicio
# segundo parámetro==> final
# tercer parámetro==> para hacer saltos.
lista=[]
for i in range(3):
    lista.append(int(input('ingrese numero: ')))
    print(lista)