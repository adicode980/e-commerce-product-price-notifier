#website price tracker 
import requests
from bs4 import BeautifulSoup
import smtplib
def send_email():
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("gmail-Id","password")
    message ="hi , you can check the new price"
    s.sendmail("sender's ID","receiver's Id'",message)
    s.quit()
#product url
page_url="https://www.amazon.in/dp/B07DJ8K2KT?pf_rd_p=fa25496c-7d42-4f20-a958-cce32020b23e&pf_rd_r=CFVBZ07NZBQ4MJWJ4BMN"
browser_agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
product_page=requests.get(page_url,headers=browser_agent)
soup=BeautifulSoup(product_page.content,'html.parser')
page_title=soup.find(id="productTitle")
product_price=soup.find(id="priceblock_dealprice")
product_price=str(product_price)
print(page_title)
print(product_price)
result=''.join([i for i in product_price if i.isdigit()])
print(result)
result=int(result)
price_you_want=int(input())
if price_you_want<result
    send_email()





