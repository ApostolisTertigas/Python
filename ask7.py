#7)Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python για να βρείτε τον αριθμό που 
#εμφανίζεται συχνότερα στο ΚΙΝΟ κάθε μέρα του τρέχοντα μήνα.

import json
import urllib.request
from datetime import datetime


date= datetime.now()

stDate= date.strftime("%Y-%m")
day= date.strftime("%d")


lst=[]
for i in range(81):
	lst.append(0)


for i in range (1,int(day)):
	if i<10:
		i= '0'+ str(i)

	url='https://api.opap.gr/draws/v3.0/1100/draw-date/'+stDate+'-'+str(i)+'/'+stDate+'-'+str(i)
	r= urllib.request.urlopen(url)
	html= r.read()
	html= html.decode()
	data= json.loads(html)
	

	for draw in data["content"]:
		for i in range(20):
			k= draw["winningNumbers"]["list"][i] #len=20
			lst[k]+=1 #Βάζω και το 0 σαν αριθμό, αν και δεν υπάρχει στο ΚΙΝΟ
mx= max(lst)
print ("Ο αριθμός που εμφανίζεται συχνότερα τον τρέχοντα μήνα, είναι ο",lst.index(mx),"\nπου βρέθηκε",mx,"φορές")