from selenium import webdriver
import random as rd
import selenium.webdriver.support.ui as ui
import time 

name=[]
email=[]
uni=set()

#this Following commented code is to get the names and email for the form, Please use your own source.

# with open("NDLI.csv","r") as file:
# 	allist=file.readlines()
# 	for x in allist:
# 		a,b=x.split(',')
# 		if b in uni:
# 			print("Not unique")
# 		else:
# 			uni.add(b)
# 			name.append(a.strip('\n'))
# 			email.append(b.strip('\n'))

op1=rd.choices(["A","B","C","D","E","F"],[50,20,17,0,11,2],k=len(name))# the numbers are the biased distribution i wanted
op2=rd.choices(["A","B","C","D","E","F"],[48,4,8,20,10,10],k=len(name))
op3=rd.choices(["A","B","C","D","E","F"],[23,8,28,13,21,7],k=len(name))
op4=rd.choices(["A","B","C","D","E","F"],[64,2,7,7,15,5],k=len(name))
op5=rd.choices(["A","B","C","D","E","F"],[14,0,7,3,71,5],k=len(name))
op6=rd.choices(["A","B","C","D","E","F"],[35,5,33,9,12,6],k=len(name))

driver = webdriver.Chrome()
for x in range(len(name)):
	print("Start : "+str(x))
	params=[name[x],email[x],op1[x],op2[x],op3[x],op4[x],op5[x],op6[x]]#Parameters that needs to be filled.
	url="https://docs.google.com/forms/d/e/1FAIpQLSeBip304dj4LvwXPu_hOoFvsrypcq1G-PpAY9gTipvZpgFE9g/viewform?usp=pp_url&entry.1309997169="+params[0]+"&entry.167817104="+params[1]+"&entry.213569411="+params[2]+"&entry.189181074="+params[3]+"&entry.1969424105="+params[4]+"&entry.276339815="+params[5]+"&entry.576870097="+params[6]+"&entry.124413627="+params[7]
	driver.get(url)
	for y in range(0,6):
		time.sleep(2)
		elem=driver.find_element_by_css_selector("div[jsname='OCpkoe']")#Selecting according to page
		elem.click()
	
	time.sleep(3)# total time delay is 6*2(Per page 2 Delay)+3 For the Final submission.

	elem=driver.find_element_by_css_selector("div[jsname='M2UYVd']")#Selecting according to page
	elem.click()
	print("Done upto "+str(x))
