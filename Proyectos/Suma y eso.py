# Operadores aritmeticos
print(1 + 1)
print(2 - 1)
print(4 * 2)
print(3 ** 3) # potenciacion
print(4 / 2) # division que queda con decimales
print(4 // 2) # Flor, division de parte entera
print(5 % 2) # Se divide y el restante es el resultado
# Trabajando con Letras
print('Hola' + 'Mundo')
print('Hola' + '6')
print('Hola' * 6)
# Peeero si yo pongo
A = 6
print('Hola' + 'A')
print('Hola' + str(A)) # Aca funciona con la variable. STR

#Operadores compararivos/ relacionales
print(4 < 8)
print(4 > 8)
print(4 == 8)
print(4 <= 8)
print(4 >= 8)
print(4 != 8) # pregunto si es diferente !=



#Ahora a letras
print('aba' < 'aaa')
print('aaa' < 'aba') #se cuenta la posicion en el abc

#Operadores logicos
print( 4 < 1 and 5 < 2) #and, con que haya uno falso, es falso
print( 4 > 1 and 5 > 2)
print( 4 < 1 or 5 > 2) #or, con que haya un true devuelve true a pesar del falso
print( 4 < 1 or 5 < 2)

#Operadores de asignacion
r = 1
r = r + 3 #version larga
r += 3 #version corta, operadores de asignacion
r -= 3


print(type(r))


#Cadenas
my_str = 'Hello, world!'    # Creamos una cadena

len(my_str)                 # Consultamos por su longitud
13

my_str[0]                   # Con slicing consultamos por el 1er caracter.
'H'

my_str[1]                   # Consultamos por el 2do caracter.
'e'

my_str[2]                   # Consultamos por el 3er caracter.
'l'

my_str[2:]                  # Traemos desde el 3er caracter hasta el final.
'llo, world!'



