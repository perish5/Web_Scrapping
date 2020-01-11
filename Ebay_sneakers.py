
import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.ebay.com/b/Mens-Athletic-Shoes/15709/bn_57918"
response = requests.get(url )
soup = BeautifulSoup(response.content,"lxml")
product = soup.find_all("div",{"class":"s-item__wrapper clearfix"})
products = product[0]                
                     
                     
csv_file = open("sneakers.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Price", "Shipping_Charge", "Brand"])


                     
for products in product:

    name = products.find_all("h3") 
    Name = name[0].text
                     
    price = products.find_all("div",{"class":"s-item__detail s-item__detail--primary"})  
    Price = price[0].text
    
    shipping = products.find_all("span",{"class":"s-item__shipping s-item__logisticsCost"})  
    Shipping = shipping[0].text.replace("shipping","")    
    
    brand = products.find_all("span",{"class":"s-item__dynamic s-item__dynamicAttributes1"})       
    brandd = brand[0].text.replace("Brand:","")  
    

    
    print("Name:" + Name)
    print("Price:" + Price)
    print("Shipping:" + Shipping)
    print("Brandd:" + brandd)
    
    csv_writer.writerow([Name, Price, Shipping , brandd])
    
csv_file.close()

