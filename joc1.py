import random
t=["piatra","hartie","foarfeca"]
comp=random.choice(t)
n=int(input("Cate runde vrei?: "))
i=0
while i<n:
	util=input("piatra, hartie sau foarfeca? 3....2...1....ALEGE:")
	print("%s" %(comp))
	if util==comp:
		print("REMIZA")
	elif util=="piatra":
		if comp=="hartie":
			print("AI PIERDUT!")
		else :
			print("AI CASTIGAT!!")
	elif util=="hartie":
		if comp=="foarfeca":
			print("AI PIERDUT!!")
		else :
			print("AI CASTIGAT!!")
	elif util=="foarfeca":
		if comp=="piatra":
			print("AI PIERDUT!!")
		else :
			print("AI CASTIGAT!!")

	else :
		print("Nu ai scris cum trebuie ce ai ales!")
	comp=random.choice(t)
	i=i+1	
