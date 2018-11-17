from urllib.request import urlopen
import re
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
			productDict["titlu"]=s[0:pos]
		for containerSale in containerProduct.findAll("div",{"class":"Badge"}):
			productDiscount=containerSale.find("div",class_="Badge-reducere")
			if(productDiscount==None):
				productDict["are reducere"]="NU"
				productDict["reducere"]="-"
			else:
				productDict["are reducere"]="DA"
				productDict["reducere"]=productDiscount.get_text()[8:]
		if(containerProduct.find("div",class_="Badge")==None):
			productDict["are reducere"]="NU"
		currentPrice=containerProduct.find(itemprop="price")
		s=currentPrice.get("content")
		productDict["pret actual"]=s+" lei"
		productOldPrice=containerProduct.find("div",class_="Price-old")
		if(productOldPrice)==None:
			productDict["pret vechi"]="-"
		else:
			productDict["pret vechi"]=productOldPrice.get_text()+" lei"
		productStock=containerProduct.find("div",class_="Status")
		productDict["status produs"]=productStock.get_text()
		for containerLink in containerProduct.findAll("a",{"class":"Product-photoTrigger js-ProductClickListener"}):
			s=containerLink.get("href")
			productDict["link produs"]=s
		for containerSpecs in containerProduct.findAll("a",{"class":"Product-photoTrigger js-ProductClickListener"}):
			s=containerSpecs.get("title")
			pos=s.find(", ")
			pos=pos+1
			productDict["specificatii produs"]="Procesor"+s[pos:]
		productList.append(productDict)
	return productList
def scriereInFisierCSV(soupList):
	with open("laptopuri.csv","w")as f:
		for item in range(soupList):
			w=csv.DictWriter(f,soupList[item].keys())
			w.writeheader()
			for key in soupList[item].keys():
				w.writerow(soupList[item].get(key))
def mainFunction():
	html1 = urlopen("https://altex.ro/laptopuri/cpl")
	htmlCode1=html1.read()
	pageSoup1=BeautifulSoup(htmlCode1,"html.parser")
	list1=construireListaProduse(pageSoup1)
	scriereInFisierCSV(list1)



