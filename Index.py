#Sirve para saber en que posicion esta determinado cada caracter
mi_texto = 'Esta es una prueba'
resultado = mi_texto [-4]
print (resultado)

 #--------------------------------------------

 #con el METODO index podemos buscar un caracter o letra como en el ej.
mi_texto = 'tambien sirve para buscar caracteres como palabras y posiciones'
resultado = mi_texto.index("a")
print (resultado)

#------------------------------------------



mi_texto = 'Esta es una prueba'
resultado = mi_texto.index ('a',5) #Lo que hace es buscar desde la posicion 5 la tra 'a'
print (resultado)

#------------------------------------------

             #rindex

mi_texto = 'Esta es una prueba'
resultado = mi_texto.rindex('e') #El metodo llamado RINDEX que este busca ahora de derecha a izquierda.
print(resultado)

#------------------------------------------
datos = input("dime tu edad ")
print ("tu edad es " + datos)

datos_generales = input("dime tu nombre ")
print("tu nombre es: " + datos_generales)


#---holaa--
cambio realizado por Nayeli
