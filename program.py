from PIL import Image
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys
import numpy
import os
import time
df = pd.read_csv('modified.csv')
x = input("1.Weekly Data Analysis \n2.Yearly Data Analysis\n3.Monthly Data Analysis\n4.Analysis of Medium used to interact\n5.Customer Satisfaction Analysis\n6.Product issue Analysis\n7.Duration Analysis\n0.Exit\nPlease Enter your choice : ")
while(x!=0):
	if x==1:
		print df.Day.value_counts()
		df.Day.value_counts().plot.bar()
		plt.ylabel('Number of Complaints')
		plt.xlabel('Day of the Week')
		plt.title('Number of Complaints registered among different days of the week')
		fig = plt.gcf()
		plt.show()
#plt.savefig('foo.png')
#img = Image.open('foo.png')
#img.show()
	elif x==2:
		print df.Year.value_counts().sort_index()
		df.Year.value_counts().sort_index().plot.bar()
		plt.ylabel('Number of Complaints')
		plt.xlabel('Years')
		plt.title('Number of Complaints registered through different years')
		fig = plt.gcf()
		plt.show()
	elif x==3:
		print df.Month.value_counts().sort_index()
		df.Month.value_counts().sort_index().plot.pie()
		plt.ylabel('Number of Complaints')
		plt.xlabel('Months of the year')
		plt.title('Number of Complaints registered among different months of the year')
		fig = plt.gcf()
		plt.show()
	elif x==4:
		print df.SubmittedVia.value_counts().sort_index()
		df.SubmittedVia.value_counts().sort_index().plot.bar()
		plt.ylabel('Number of Complaints')
		plt.xlabel('Medium of Complaints')
		plt.title('Analysis of Medium used')
		fig = plt.gcf()
		plt.show()
	elif x==5:
		S=df['Consumer disputed?']=="No"
		N=df['Consumer disputed?']=="Yes"
		Sat=0
		Not=0
		for i in range(0,len(S)):
			if S[i]==True:
				Sat+=1
			else:
				Not+=1
		satisfaction=[Sat,Not]
		bars=('Satisfied','Not Satisfied')
		plt.bar(bars,satisfaction)
		plt.xlabel('Satisfaction')
		plt.ylabel('Number of Complaints')
		fig=plt.gcf()
		plt.show()
	elif x==6:
		plt.tight_layout()
		df.Product.value_counts().sort_index().plot.bar()
		plt.xlabel('Type of product')
		plt.ylabel('Number of Complaints')
		plt.title('Product Analysis')
		fig=plt.gcf()
		plt.show()
	elif x==7:
		dt=df.Time.value_counts().sort_index().plot()
		fig=plt.gcf()
		plt.show()
	else:
		break
	z=input("Do you want to export it as an jpg file? \n1.Yes\n2.No \n")
	if(z==1):
		fig.savefig('figure.jpg')
		print "Exported as pdf named Figure.jpg"
	else:
		print "Sure"
	os.system('cls')
	x = input("1.Weekly Data Analysis \n2.Monthly Data Analysis\n3.Yearly Data Analysis\n4.Analysis of Medium used to interact\n5.Customer Satisfaction Analysis\n6.Product issue Analysis\n7.Duration Analysis\n0.Exit\nPlease Enter your choice : ")
os.system('cls')
print "Thank you for using this Analyser"
time.sleep(20)

