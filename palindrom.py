pal1=input("Va rog introduce-ti un palindrom(Un palindrom este un sir de caractere care citi de la stanga la deapta sau de la dreapta la stanga ramane neschimbat): ")
pal2=pal1[::-1]
if pal1==pal2:
	print("Cumvantul este palindrom!")
else :
	print("Cumvantul NU este palindrom!")