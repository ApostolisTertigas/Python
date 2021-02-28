#(2) Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι. 
#Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p.
#Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.

import random

def fibo(x):
	i=1
	j=1
	for k in range (x-2):
		tmp=i
		i= i+j
		j=tmp
	return i

term= int(input("Type the term of the Fibonacci sequence: \n"))  #oros

if term==1:
	p=0
else:
	for i in range (term):
		p= (fibo(i))	#αυτός είναι ο αριθμός

print (p)

if p==1 or p==0:
	print (p, " isnt prime number") 
else:
	flag=True
	
	for i in range(20):
		a= random.randint(1,p) #1<a<p
		if ((a**p) % p == a%p) == False:	#Επειδή το a^p=a mod p δεν μου βγηκε, το εκανα (a**p) % p == a%p
			flag=False
			break
	
	if flag==False:
		print (p, "isnt prime number")
	else:
		print (p, "is prime")	
