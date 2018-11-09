
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
	 	cadena="Informacion de %s%s\n\t Cedula:%s"%(self.obtener_nombre(),self.apellido,self.obtener_cedula())
	 	return cadena