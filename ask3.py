#3)Χρησιμοποιήστε το API του ΟΠΑΠ (https://www.opap.gr/web-services) από την Python για να εμφανίσετε τα στατιστικά 
#των αριθμών που κερδίζουν την πρώτη κλήρωση της ημέρας για το ΚΙΝΟ τον τρέχον μήνα.

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

	#gia na vrw to draw id
	url='https://api.opap.gr/draws/v3.0/1100/draw-date/'+stDate+'-'+str(i)+'/'+stDate+'-'+str(i)+'/draw-id'
	r= urllib.request.urlopen(url)
	html= r.read()
	html= html.decode()
	data= json.loads(html)
	fDrawId= data[0]
	
	#gia ta statistika
	url2= 'https://api.opap.gr/draws/v3.0/1100/'+str(fDrawId)
	r= urllib.request.urlopen(url2)
	html= r.read()
	html= html.decode()
	data= json.loads(html)
	
	
	for number in data["winningNumbers"]["list"]:
		lst[number]+=1 #Βάζω και το 0 σαν αριθμό, αν και δεν υπάρχει στο ΚΙΝΟ
	
	
for number in range(1,81):		
	print ("Ο αριθμός: "+str(number)+" εμφανίστηκε: "+str(lst[number])+" φορές.")