class EmpleadoFijo(Empleado):
	def__int__(self):
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
		cadena="%s\n Sueldo fijo:%s\n Descuento Seguro:%s\n Sueldo final:%s"%(super(EmpleadoFijo, self).presentar_datos(),self.obtener_sueldo_fijo(),self.obtener_Descuento_seguro()
			self.calcular_sueldo_final())
