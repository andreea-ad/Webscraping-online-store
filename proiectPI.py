from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup, Tag
def construireListaProduse(soupSite):
	productList=[]
	i=0
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
def mainFunction():
	s1,s2,s3,s4,s5,s6,s7=0,0,0,0,0,0,0
	#pagina 1
	html1=urlopen("https://altex.ro/laptopuri/cpl")
	htmlCode1=html1.read()
	pageSoup1=BeautifulSoup(htmlCode1,"html.parser")
	list1=construireListaProduse(pageSoup1)
	scriereInFisierCSV(list1)
	s1+=produseReduse(list1)
	s2+=produseIntervalLei(list1,0,1000)
	s3+=produseIntervalLei(list1,1000,2000)
	s4+=produseIntervalLei(list1,2000,3000)
	s5+=produseIntervalLei(list1,3000,4000)
	s6+=produseIntervalLei(list1,4000,5000)
	s7+=produseIntervalLei(list1,5000,30000)
	#pagina 2
	html2=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/2/")
	htmlCode2=html2.read()
	pageSoup2=BeautifulSoup(htmlCode2,"html.parser")
	list2=construireListaProduse(pageSoup2)
	appendInFisierCSV(list2)
	s1+=produseReduse(list2)
	s2+=produseIntervalLei(list2,0,1000)
	s3+=produseIntervalLei(list2,1000,2000)
	s4+=produseIntervalLei(list2,2000,3000)
	s5+=produseIntervalLei(list2,3000,4000)
	s6+=produseIntervalLei(list2,4000,5000)
	s7+=produseIntervalLei(list2,5000,30000)
	#pagina 3
	html3=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/3/")
	htmlCode3=html3.read()
	pageSoup3=BeautifulSoup(htmlCode3,"html.parser")
	list3=construireListaProduse(pageSoup3)
	appendInFisierCSV(list3)
	s1+=produseReduse(list3)
	s2+=produseIntervalLei(list3,0,1000)
	s3+=produseIntervalLei(list3,1000,2000)
	s4+=produseIntervalLei(list3,2000,3000)
	s5+=produseIntervalLei(list3,3000,4000)
	s6+=produseIntervalLei(list3,4000,5000)
	s7+=produseIntervalLei(list3,5000,30000)
	#pagina 4
	html4=urlopen("https://altex.ro/laptopuri/cpl/filtru/p/4/")
	htmlCode4=html4.read()
	pageSoup4=BeautifulSoup(htmlCode4,"html.parser")
	list4=construireListaProduse(pageSoup4)
	appendInFisierCSV(list4)
	s1+=produseReduse(list4)
	s2+=produseIntervalLei(list4,0,1000)
	s3+=produseIntervalLei(list4,1000,2000)
	s4+=produseIntervalLei(list4,2000,3000)
	s5+=produseIntervalLei(list4,3000,4000)
	s6+=produseIntervalLei(list4,4000,5000)
	s7+=produseIntervalLei(list4,5000,30000)
	print("----------------------Scurta statistica----------------------")
	print("Exista " + str(s1) + " laptopuri aflate la reducere pe site")
	print("Exista " + str(s2) + " laptopuri cu pretul mai mic de 1000 lei")
	print("Exista " + str(s3) + " laptopuri cu pretul cuprins intre 1001 si 2000 lei")
	print("Exista " + str(s4) + " laptopuri cu pretul cuprins intre 2001 si 3000 lei")
	print("Exista " + str(s5) + " laptopuri cu pretul cuprins intre 3001 si 4000 lei")
	print("Exista " + str(s6) + " laptopuri cu pretul cuprins intre 4001 si 5000 lei")
	print("Exista " + str(s7) + " laptopuri cu pretul mai mare de 5000 lei")
	print("Cel mai vandut laptop este " + list1[0].get("Titlu") + " avand pretul de " + list1[0].get("Pret actual"))

mainFunction()
