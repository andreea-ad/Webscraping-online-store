from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup
def construireListaProduse(soupSite):
	productList=[]
	for containerProduct in soupSite.findAll("div",{"class":"Product"}):
		for containerTitle in containerProduct.findAll("a",{"class":"Product-name"}):
			productDict={}
			s=containerTitle.get("title")
			pos=s.find(",")
			if(pos<0):
				print("O eroare s-a produs la parsarea titlurilor produselor!")
				return 0
			productDict["Titlu"]=s[0:pos]
		for containerSale in containerProduct.findAll("div",{"class":"Badge"}):
			productDiscount=containerSale.find("div",class_="Badge-reducere")
			if(productDiscount==None):
				productDict["Are reducere"]="NU"
				productDict["Reducere"]=""
			else:
				productDict["Are reducere"]="DA"
				productDict["Reducere"]=productDiscount.get_text()[8:]
		if(containerProduct.find("div",class_="Badge")==None):
			productDict["Are reducere"]="NU"
		currentPrice=containerProduct.find(itemprop="price")
		s=currentPrice.get("content")
		productDict["Pret actual"]=s+" lei"
		productOldPrice=containerProduct.find("div",class_="Price-old")
		if(productOldPrice)==None:
			productDict["Pret vechi"]=""
		else:
			productDict["Pret vechi"]=productOldPrice.get_text()+" lei"
		productStock=containerProduct.find("div",class_="Status")
		productDict["Status produs"]=productStock.get_text()
		for containerLink in containerProduct.findAll("a",{"class":"Product-photoTrigger js-ProductClickListener"}):
			s=containerLink.get("href")
			productDict["Link produs"]=s
		for containerSpecs in containerProduct.findAll("a",{"class":"Product-photoTrigger js-ProductClickListener"}):
			s=containerSpecs.get("title")
			pos=s.find(", ")
			pos=pos+1
			productDict["Specificatii produs"]="Procesor"+s[pos:]
		productList.append(productDict)
	return productList
def scriereInFisierCSV(soupList):
	keys=soupList[0].keys()
	with open('laptopuri.csv','w') as outputFile:
		dict_writer=csv.DictWriter(outputFile,keys)
		dict_writer.writeheader()
		dict_writer.writerows(soupList)
def appendInFisierCSV(soupList):
	keys=soupList[0].keys()
	with open('laptopuri.csv','a') as outputFile:
		dict_writer=csv.DictWriter(outputFile,keys)
		dict_writer.writerows(soupList)
def produseReduse(soupList):
	s=0
	for item in soupList:
		if(item["Are reducere"]=="DA"):
			s+=1
	return s
def produseIntervalLei(soupList,startPrice,stopPrice):
	s=0
	for item in soupList:
		pret=item["Pret actual"]
		pos=pret.find("lei")
		pret=pret[:pos-1]
		if(float(pret)>startPrice and float(pret)<=stopPrice):
			s+=1
	return s
def pretMaximLista(soupList):
	maxim=0
	for item in soupList:
		pret=item["Pret actual"]
		pos=pret.find("lei")
		pret=pret[:pos-1]
		if(float(pret)>maxim):
			maxim=float(pret)
	return maxim
def mainFunction():
	#pagina 1
	html1=urlopen("https://altex.ro/laptopuri/cpl")
	htmlCode1=html1.read()
	pageSoup1=BeautifulSoup(htmlCode1,"html.parser")
	list1=construireListaProduse(pageSoup1)
	#pagina 2
	html2=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/2/")
	htmlCode2=html2.read()
	pageSoup2=BeautifulSoup(htmlCode2,"html.parser")
	list2=construireListaProduse(pageSoup2)
	#pagina 3
	html3=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/3/")
	htmlCode3=html3.read()
	pageSoup3=BeautifulSoup(htmlCode3,"html.parser")
	list3=construireListaProduse(pageSoup3)
	#pagina 4
	html4=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/4/")
	htmlCode4=html4.read()
	pageSoup4=BeautifulSoup(htmlCode4,"html.parser")
	list4=construireListaProduse(pageSoup4)
	#pagina 5
	html5=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/5/")
	htmlCode5=html5.read()
	pageSoup5=BeautifulSoup(htmlCode5,"html.parser")
	list5=construireListaProduse(pageSoup5)
	#pagina 6
	html6=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/6/")
	htmlCode6=html6.read()
	pageSoup6=BeautifulSoup(htmlCode6,"html.parser")
	list6=construireListaProduse(pageSoup6)
	#pagina 7
	html7=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/7/")
	htmlCode7=html7.read()
	pageSoup7=BeautifulSoup(htmlCode7,"html.parser")
	list7=construireListaProduse(pageSoup7)
	#pagina 8
	html8=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/8/")
	htmlCode8=html8.read()
	pageSoup8=BeautifulSoup(htmlCode8,"html.parser")
	list8=construireListaProduse(pageSoup8)
	#pagina 9
	html9=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/9/")
	htmlCode9=html9.read()
	pageSoup9=BeautifulSoup(htmlCode9,"html.parser")
	list9=construireListaProduse(pageSoup9)
	#pagina 10
	html10=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/10/")
	htmlCode10=html10.read()
	pageSoup10=BeautifulSoup(htmlCode10,"html.parser")
	list10=construireListaProduse(pageSoup10)
	#pagina 11
	html11=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/11/")
	htmlCode11=html11.read()
	pageSoup11=BeautifulSoup(htmlCode11,"html.parser")
	list11=construireListaProduse(pageSoup11)
	#pagina 12
	html12=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/12/")
	htmlCode12=html12.read()
	pageSoup12=BeautifulSoup(htmlCode12,"html.parser")
	list12=construireListaProduse(pageSoup12)
	#pagina 13
	html13=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/13/")
	htmlCode13=html13.read()
	pageSoup13=BeautifulSoup(htmlCode13,"html.parser")
	list13=construireListaProduse(pageSoup13)
	#pagina 14
	html14=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/14/")
	htmlCode14=html14.read()
	pageSoup14=BeautifulSoup(htmlCode14,"html.parser")
	list14=construireListaProduse(pageSoup14)
	#pagina 15
	html15=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/15/")
	htmlCode15=html15.read()
	pageSoup15=BeautifulSoup(htmlCode15,"html.parser")
	list15=construireListaProduse(pageSoup15)
	#Creare tabel
	scriereInFisierCSV(list1)
	appendInFisierCSV(list2)
	#appendInFisierCSV(list3)
	#appendInFisierCSV(list4)
	#appendInFisierCSV(list5)
	#appendInFisierCSV(list6)
	#appendInFisierCSV(list7)
	#appendInFisierCSV(list8)
	#appendInFisierCSV(list9)
	#appendInFisierCSV(list10)
	#appendInFisierCSV(list11)
	#appendInFisierCSV(list12)
	#appendInFisierCSV(list13)
	#appendInFisierCSV(list14)
	#appendInFisierCSV(list15)
	#Realizare statistica
	totalList=list1+list2+list3+list4+list5+list6+list7+list8+list9+list10+list11+list12+list13+list14+list15
	maxim=pretMaximLista(totalList)
	s1=produseReduse(totalList)
	s2=produseIntervalLei(totalList,0,1000)
	s3=produseIntervalLei(totalList,1000,2000)
	s4=produseIntervalLei(totalList,2000,3000)
	s5=produseIntervalLei(totalList,3000,4000)
	s6=produseIntervalLei(totalList,4000,5000)
	s7=produseIntervalLei(totalList,5000,maxim)
	print("----------------------Scurta statistica----------------------")
	print("Exista " + str(s1) + " laptopuri aflate la reducere pe site\n")
	print("Exista " + str(s2) + " laptopuri cu pretul mai mic de 1000 lei")
	print("Exista " + str(s3) + " laptopuri cu pretul cuprins intre 1001 si 2000 lei")
	print("Exista " + str(s4) + " laptopuri cu pretul cuprins intre 2001 si 3000 lei")
	print("Exista " + str(s5) + " laptopuri cu pretul cuprins intre 3001 si 4000 lei")
	print("Exista " + str(s6) + " laptopuri cu pretul cuprins intre 4001 si 5000 lei")
	print("Exista " + str(s7) + " laptopuri cu pretul mai mare de 5000 lei\n")
	print("Cel mai vandut laptop este " + list1[0].get("Titlu") + " avand pretul de " + list1[0].get("Pret actual"))

mainFunction()
