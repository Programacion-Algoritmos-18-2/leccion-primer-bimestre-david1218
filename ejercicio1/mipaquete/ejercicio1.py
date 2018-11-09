
class Empleado (object):
    def __int__(self):
        self.nombre=""
        self.apellido=""
        self.cedula+""
        self.comision.fija=0

    def agregar_comision_fija(self , comision):
        self.comision_fija=comision
    
    def obtener_comision_fija(self):
        return self.comision_fija

    def agregar_nombre(self, no):
        self.nombre=no
    def agregar_apellido(self,  ape):
        self.apellido=ape
    def agregar_cedula(self,ced):
        self.cedula=ced
    def obtener_nombre(self):
        return self.nombre
    def obtener_apellido(self):
        return self.apellido
    def obtener_cedula(self):
        return self.cedula
    def presentar_datos(self):
        cadena="Informacion de %s %s\n\t Cedula:%s"%(self.obtener_nombre(),self.apellido,self.obtener_cedula())
        return cadena

class EmpleadoPorHoras(Empleado):
    def __int__(self):
        super(EmpleadoPorHoras,self).__int__()
        self.numero_horas=0
        self.valor_horas=0
    def agregar_numero_horas(self, n):
        self.numero_horas=n
    def agregar_valor_horas(self,  v):
        self.valor_horas=v
    def obtener_numero_horas(self):
        return self.numero_horas
    def obtener_valor_horas(self):
        return self.valor_horas
    def calcular_valor_sueldo(self):
        calcular_valor_sueldo = (self.obtener_numero_horas * self.obtener_valor_horas) + (self.obtener_comision_fija)
        return calcular_valor_sueldo
    def presentar_datos(self):
        cadena="%s\n Numerohoras:%s\n valorhoras:%s\n Sueldo final:%s"%(super(EmpleadoPorHoras, self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas(),
         self.calcular_valor_sueldo())
        return cadena
"""
 class EmpleadoPorSemana(Empleado):
    def __int__(self):
         super(EmpleadoPorSemana,self).__int__()
         self.numero_semanas=0
         self.valor_semanal=0
    def agregar_numero_semanas(self, n):
         self.numero_semanas=se
    def agregar_valor_semanal(self,  v):
         self.valor_semanal=sem
    def obtener_numero_semanas(self):
         return self.numero_semanas
    def obtener_valor_semanal(self):
         return self.valor_semanal
    def calcular_sueldo_final;(self):
         calcular_valor_sueldo= (self.obtener_numero_horas)+(self.obtener_valor_horas)+(self.comision_fija)
         return calcular_valor_sueldo
    def presentar_datos(self):
        cadena="%s\n Numerohoras:%s\n valor_horas:%s\n Sueldo final:%s"%(super(EmpleadoPorHoras, self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas()
            self.calcular_valor_sueldo_final())
"""
class EmpleadoFijo(Empleado):
    def __int__(self):
        super(EmpleadoFijo,self).__int__()
        self.sueldo_fijo=0
        self.Descuento_seguro=0
    def agregar_sueldo_fijo(self, sf):
        self.sueldo_fijo=sf
    def agregar_Descuento_seguro(self,  ds):
        self.Descuento_seguro=ds
    def obtener_sueldo_fijo(self):
        return self.sueldo_fijo
    def obtener_Descuento_seguro(self):
        return self.Descuento_seguro
    def calcular_sueldo_final(self):
        sueldo_final=(self.obtener_sueldo_fijo()+self.obtener_comision_fija()-self.obtener_Descuento_seguro()/100)
        return sueldo_final

    def presentar_datos(self):
        cadena="%s\n Sueldo fijo:%s\n Descuento Seguro:%s\n Sueldo final:%s"%(super(EmpleadoFijo, self).presentar_datos(),self.obtener_sueldo_fijo(),self.obtener_Descuento_seguro(),
        self.calcular_sueldo_final())