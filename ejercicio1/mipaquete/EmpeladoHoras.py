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
        calcular_valor_sueldo= (self.obtener_numero_horas * self.obtener_valor_horas) + self.obtener_comision_fija
        return calcular_valor_sueldo
    def presentar_datos(self):
        cadena="%s\n Numerohoras:%s\n valorhoras:%s\n Sueldo final:%s"%(super(EmpleadoPorHoras, self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas(),
            self.calcular_valor_sueldo())
        return cadena