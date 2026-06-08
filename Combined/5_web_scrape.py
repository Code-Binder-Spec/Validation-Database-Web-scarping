import aiohttp
import asyncio
import logging
from bs4 import BeautifulSoup
from pydantic import BaseModel,field_validator
import aiosqlite

logging.basicConfig(filename="5web.log",level=logging.INFO)

class flipkart_data_ensure(BaseModel):
        
        device : str
        features : str
        price : str

        @field_validator("features",mode="before")
        @classmethod
        def checking_feature(cls,v):
                print(v)
                if v.lower() == "description not found":
                        actual_v = None
                        return actual_v
                else :
                        return v
        @field_validator("price",mode="before")
        @classmethod
        def checking_price(cls,v):
                if v.lower() == "price not found":
                        actual_v = None
                        return actual_v
                else :
                        return v
                  
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
           return None
     
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
               return "price not found"

           
def description_scraper(box):
     flag = True
     try:
                       description_box = box.find_all("ul",class_="HwRTzP")
                       description_lis = []
                       for description in description_box:
                                       actual_description = checking_none(description)
                                       description_lis.append(actual_description.text)
                       full_des = ",".join(description_lis)
     except Exception as e :
             flag = False
             logging.error(f"Name scraping failed due to error : {e}")

     if flag :
             return full_des
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
          if not name :
                continue
          else :
                 full_data.append((name,description,price))
                 logging.info(f"Data fetched from url : {url} : succes ")
      
async def flipkart_sql_write(db,data):
        await db.execute("INSERT INTO flipkart(name,features,price) VALUES (?,?,?)",(data.device,data.features,data.price))
        await db.commit()


async def main():
    full_data = []
    validated_data = []
    async with aiosqlite.connect("5web.db") as db:
                    await db.execute("""
                         CREATE TABLE IF NOT EXISTS flipkart(
                                     id INTEGER PRIMARY KEY,
                                     name TEXT,
                                     features TEXT,
                                     price TEXT
                                       ) 
                                           """)
                    await db.commit()
                    async with aiohttp.ClientSession() as session:
                                   await asyncio.gather(
                                                    passing_soup_block_flipkart("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=2",session,full_data)
                                               )
                    for i in full_data:
                               ensure_data =  flipkart_data_ensure(device=i[0],features=i[1],price=i[2])
                               validated_data.append(ensure_data)
                    for data in validated_data:
                            await flipkart_sql_write(db,data)

                         
        
asyncio.run(main())
