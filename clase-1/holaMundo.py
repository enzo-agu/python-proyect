# print('mundo')
# print(2+5)
# # comentarios=> primera letra en mayúscula
# # t==> tabulación
# print('mundo\tnuevo' )
# # sep==> une como el join de js
# print('Hola','Mundo','nuevo',sep='-')
# # end==> 
# print('uniendo',end='==>')
# print('con end')

# # ------------------------------

# # input y variables
# # input ==>siempre devuelve string

# # variable_ejemplo=input('ingrese un mensaje: ')
# # print(variable_ejemplo)

# # ------------------------------

# # int==> parsea string a numero

# # numero1=int(input('ingrese primer numero'))
# # numero2=int(input('ingrese segundo numero'))
# # resultado=numero1+numero2
# # print(resultado)
# # print(type(numero1)) 

# # -------------------------------

# x='x'
# c='cadena nueva'
# print(len(c))
# print(c.replace(c,x))
# print(x)


# # Lista==> array de js
# # Tupla==> igual que una lista, pero no se puede cambiar.
# lista=['viejaLista',1,True,False]
# print(type(lista))
# lista.append('nuevaLista')
# print(lista)
# print(lista.index('nuevaLista'))
# # insert==>dos parámetros: 
# # indice donde va el nuevo elemento, elemento a insertar
# lista.insert(1,'nuevaInsercion')
# print(lista)

# # Diccionario==>Objeto Json
# diccionario={
#     'id':1,
#     'nombre':'enzo',
#     'edad':34,
#     'hobbie':['jiu jitsu'],
#     'mascota':False
# }
# print(diccionario['hobbie'])
# # get==> si no encuentra se puede
# # aplicar valor por defecto
# print(diccionario.get('comida', 'no hay comida' ))
# print(diccionario.keys())
# keysDiccionario=list(diccionario.keys())
# print(diccionario.get(keysDiccionario[3]))
# print(diccionario.values())
mensaje1=input('ingrese arbol: ')
print(mensaje1)
print(len(mensaje1))






