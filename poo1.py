

class Persoana():
	nr_persoane=0
	def __init__(self,nume,varsta):
		self.nume=nume
		self.varsta=varsta
		self.nr_persoane=self.nr_persoane+1
	def getNume(self):
		return self.nume
	def getVarsta(self):
		return self.varsta
p1=Persoana("Gabi",23)
p2=Persoana("Alex",22)
p3=Persoana("iuli",24)

print(p1.getNume()+ " "+str(p1.getVarsta()))
print(p2.getNume()+ " "+str(p2.getVarsta()))
print(p3.getNume()+ " "+str(p3.getVarsta()))
