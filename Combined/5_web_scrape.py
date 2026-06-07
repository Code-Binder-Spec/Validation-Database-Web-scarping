import aiohttp
import asyncio
import logging
from bs4 import BeautifulSoup
import aiosqlite

logging.basicConfig(filename="5web.log",level=logging.INFO)

headers =   {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def checking_none(value):
     if not value :
          raise ValueError("The value is none")
     else :
          return value


async def getting_source(url,session):
       async with session.get(url,headers=headers) as response:
            return await response.text()
       
def name_scraper(box):
     flag = True
     try :
                   name = box.find("div",class_="RG5Slk")
                   actual_name = checking_none(name)
     except Exception as e :
               flag = False 
               logging.error(f"Name scraper failed due to error : {e}")
     if flag:
           return actual_name.text
     else :
           return "Name not found"
     
def price_scraper(box):
       flag = True 
       try:
                        price = box.find("div",class_="hZ3P6w DeU9vF")
                        actual_price = checking_none(price)
       
       except Exception as e :
               flag = False
               logging.error(f"Price scraping failed due to error . {e}")
       if flag :
               return actual_price.text
       else :
               return "Flag not found"

           
def description_scraper(box):
     flag = True
     try:
                       description_box = box.find_all("ul",class_="HwRTzP")
                       description_lis = []
                       for description in description_box:
                                       actual_description = checking_none(description)
                                       description_lis.append(actual_description.text)
     except Exception as e :
             flag = False
             logging.error(f"Name scraping failed due to error : {e}")

     if flag :
             return description_lis
     else :
            return "Description not found"
     
       
def flipkart_scraper(box):
     name = name_scraper(box)
     description =  description_scraper(box)
     price = price_scraper(box)
     return name,description,price
     
     

async def passing_soup_block_flipkart(url,session,full_data):
     source = await getting_source(url,session)
     soup = BeautifulSoup(source,"html.parser")
     boxes = soup.find_all("div",class_="lvJbLV col-12-12")
     for box in boxes :
          name,description,price = flipkart_scraper(box)
          if not name or not description:
                continue
          else :
                 full_data.append((name,description,price))
      



async def main():
    full_data = []
    async with aiohttp.ClientSession() as session:
         await asyncio.gather(
             passing_soup_block_flipkart("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2",session,full_data)
         )
         for i in full_data:
                print(f" \n Device : {i[0]} \n Features : {i[1][0]} \n Price : {i[2]}")
        
asyncio.run(main())
