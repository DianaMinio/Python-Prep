#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable_uno = 23
print(variable_uno)

# In[7]:




# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]
print(type(8.5))
#Float




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(variable_uno))



# 4) Crear una variable que contenga tu nombre

# In[2]:
variable_nombre = 'Diana minio'



# 5) Crear una variable que contenga un número complejo

# In[3]:
variable_dos = 6.8j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(variable_dos))




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

variable_ocho = 'True'
variable_nueve = True
#Se trata de dos tipos de datos diferentes, 'True' es string y True es un tipo de dato booleano.

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(variable_ocho))
print(type(variable_nueve))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

variable_diez = 2 + 9.2



# 11) Realizar una operación de suma de números complejos

# In[2]:

x = 1 + 1j
y = 2 + 2j
print(x + y)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

a = 1 + 1
b = 2 + 2j
print(a + b)



# 13) Realizar una operación de multiplicación

# In[5]:

print(a * 2)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
d = 27 / 4
print(d)




# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
print(int(d))
print(27 // 4)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
print(27 % 4)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print(3 + 4 * 6)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

vuno= 'hola '
vdos = 'mundo' 
print(vuno + vdos)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print('2' == 2)



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(not('2') == 2)
print(int('2') == 2)


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


#porque lo toma como texto, str y no como numero.



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

var_tres = 3
var_tres -= 1
print(var_tres)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1 << 2)

#El resultado obtenido se genera a través de la operación ya que traduce a los números en su código binario y desplaza de izq a derecha o viceversa al código binario de dicho numero.
# en este caso: 1 = 0001 y al desplazar 2 bits a la izquierda "<<", queda como resultado 0100 agregando a su derecha los 0 correspondientes para completar el código binario.
#Dicho código binario representa al número 4.
#El sistema de numeración binario se compone de dos estados, apagado o encendido que por lo general se simbolizan con los número 0 y 1.
#Dichos números, 0 y 1, generan combinaciones que indican diferentes tipos de información, entre ellas; instrucciones que debe seguir un procesador y en la codificación de datos (carácteres, textos, números, etc.). 


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
#No está permitido ya que son dos datos de diferentes tipos, 2 es un número entero y '2' es un string.  
print(float(2) + float('2')) 
print(int(2) + int('2'))
print(str(2) + str('2'))





# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

variable_26 = 'Termineeee '
variable_27 = 'la tarea '


print((variable_26 + variable_27) * 2)


