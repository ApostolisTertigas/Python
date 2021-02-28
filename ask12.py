#12)Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει
#τον κάθε χαρακτήρα του στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες είναι αυτοί των οποίων
#το άθροισμα είναι 255. Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.


lst=[]
stringLike=[]
text= input("Δώσε μου ένα κείμενο: \n")
text= text[::-1] #kanw reverse to keimeno


error=False
for letter in text:
	if ord(letter)<=128:
		lst.append(chr(128-(ord(letter)))) #128 'h 255?
	else:
		print ("Error\nΔεν μπορώ να κατανοήσω τους συγκεκριμένους χαρακτήρες. Δοκίμαστε ξανά!")
		error=True
		break

if error==False:
	stringLike.append(' '.join(lst)) #kanw th lista na moiazei me string
	print (stringLike)