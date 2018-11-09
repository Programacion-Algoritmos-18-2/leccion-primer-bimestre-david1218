#crear Empelado
from mipaquete.ejercicio1 import *
e=Empleado()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("213126")
print(e.presentar_datos())

y=EmpleadoPorHoras()
nombre= input("Ingrese su nombre:\n")
y.agregar_nombre(nombre)
y.agregar_apellido("Andrade")
y.agregar_cedula ("1102478965")
y.agregar_numero_horas("20.2")
y.agregar_valor_horas(15)
y.agregar_comision_fija(5)
print(y.presentar_datos())


t=EmpleadoFijo()
t.agregar_sueldo(300.2)
t.agregar_Descuento_seguro=10
comision= input("Ingrese comision:\n")
comision= float(comision)
t.agregar_comision_fija(comision)
t.nombre="Ana"
t.apellifo="Diaz"
print(t.presentar_datos())
