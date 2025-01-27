cadena = "XGCLKPHEUL GPFQYYWHST YIYHFENYIG HFYIGHQASY DQWGTHGWYC SLQWYLXYWC EIISTQCGHQ ETWTSIYLQA SYW"

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Compter les lettres
lista = 26*[0]

for letra in cadena:
	pos = abc.find(letra)
	if pos != -1:
		lista[pos] += 1

print(lista)
		
# Déchiffrer le message en essayant toutes les possibilités
for a in range(26):
	for b in range(26):
		lista2 = []
		for i in range(26):
			#letra = abc[i]
			nueva_letra = abc[(a*i+b) % 26]
			#print(letra, nueva_letra)
			lista2.append(nueva_letra)
		
		cadena2 = ""
		
		for letra in cadena:
			if letra in lista2:
				pos = lista2.index(letra)
				cadena2 += abc[pos]
			else:
				cadena2 += " "
		print(a, b)
		print(cadena2)
