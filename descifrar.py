from palabra_secreta import ingresoSecreto
from palabra_secreta_ordenada import creaDiccionario

def descifra():
	clave=ingresoSecreto()
	numeroSecreto=creaDiccionario(clave)
	mensajeFinal=input("Ingrese msj: ").upper()
	#['L', 'T', 'M', 'A', 'H', 'U', 'C', 'S', 'A', 'A', 'O', 'S', 'Q', 'L', 'E', '@', 'O', 'E', 'O', 'T']
	#LTMAHUCSAAOSQLE@OEOT
	desde=0
	hasta=int(len(mensajeFinal)/len(clave))
	descifrado={}

	for num in range(1,len(clave)+1):
		descifrado[num]=mensajeFinal[desde:hasta*num]
		desde=hasta*num
		
	for c,v in numeroSecreto.items():
		#print(decifrado[numeroSecreto[c]])
		#print("↓" * hasta)
		#se mejora la forma de mostrar el mensaje descifrado
		linea = descifrado[numeroSecreto[c]]
		if (c == 1):
			print("↓   ".join(linea) + "↓" )
			print("")
		else:	
			print("    ".join(linea))
			print("")

		'''
		
		H↓   U↓   C↓   S↓

		O    E    O    T

		L    T    M    A

		A    A    O    S

		Q    L    E    @

		'''
	
	


	
	
