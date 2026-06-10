import aiohttp
from curl_cffi import requests
import asyncio
import logging
from bs4 import BeautifulSoup
from pydantic import BaseModel,field_validator
import aiosqlite

logging.basicConfig(filename=".gitignore/log/5web.log",level=logging.INFO)

sem = asyncio.Semaphore(3)

class flipkart_data_ensure(BaseModel):
        
        device : str
        features : str | None
        price : str | None
        rating : float | None
        total_rating : int | None
        total_reviews : int | None
       
        @field_validator("rating",mode="before")
        @classmethod
        def checking_rating(cls,v):
                if v.lower() == "rating not found":
                        actual_v = None
                        return actual_v
                else :
                         real_v = v.replace(",","")
                         return float(real_v)
        @field_validator("total_rating",mode="before")
        @classmethod
        def checking_total_rating(cls,v):
                if v.lower() == "total rating not found":
                        actual_v = None
                        return actual_v
                else :
                        real_v = v.replace(",","")
                        return int(real_v)
        @field_validator("total_reviews",mode="before")
        @classmethod
        def checking_total_reviews(cls,v):
                if v.lower() == "total reviews not found":
                        actual_v = None
                        return actual_v
                else :
                        real_v = v.replace(",","")
                        return int(real_v)
        @field_validator("features",mode="before")
        @classmethod
        def checking_feature(cls,v):
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
            async with sem :
                       async with session.get(url) as response :
                                         response.raise_for_status()
                                         return await response.text()
       
def flipkart_name_scraper(box):
     flag = True
     try :
                   name = box.find("div",class_="RG5Slk")
                   actual_name = checking_none(name)
     except Exception as e :
               flag = False 
               logging.error(f"Name scraper in flipkart failed due to error : {e}")
     if flag:
           return actual_name.text
     else :
           return None
     
def flipkart_price_scraper(box):
       flag = True 
       try:
                        price = box.find("div",class_="hZ3P6w DeU9vF")
                        actual_price = checking_none(price)
       
       except Exception as e :
               flag = False
               logging.error(f"Price scraper in flipkart failed due to error . {e}")
       if flag :
               return actual_price.text
       else :
               return "price not found"

           
def flipkart_description_scraper(box):
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
             logging.error(f"description scraper in flipkart failed due to error : {e}")

     if flag :
             return full_des
     else :
            return "Description not found"
     
def flipkart_rating_scraper(box):
        flag = True
        try :
                rating = box.find("div",class_="MKiFS6")
                actual_rating = checking_none(rating)
        except Exception as e :
                flag = False
                logging.error(f"Rating scraper in flipkart failed due to error : {e}")
        if flag :
                return actual_rating.text
        else:
                return "rating not found"
        
def flipkart_total_rating_review_scraper(box):
        
         flag = True
         try :
                 rating_box = box.find("span",class_="PvbNMB")
                 actual_rate = checking_none(rating_box)
                 lis = actual_rate.text.split()
                 total_rating = lis[0]
                 total_reviews = lis[3]
         except Exception as e :
                 flag = False
                 logging.error(f"Total rating scraper in flipkart failed due to error : {e}")
         if flag :
                 return total_rating,total_reviews
         else :
                 return "total rating not found","total reviews not found"

def flipkart_scraper(box):
     name = flipkart_name_scraper(box)
     description =  flipkart_description_scraper(box)
     price = flipkart_price_scraper(box)
     rating = flipkart_rating_scraper(box)
     total_rating,total_review = flipkart_total_rating_review_scraper(box)
     return name,description,price,rating,total_rating,total_review

async def passing_soup_block_flipkart(url,full_data_flipkart,session,db,validated_data):
     source = await getting_source(url,session)
     soup = BeautifulSoup(source,"html.parser")
     boxes = soup.find_all("div",class_="lvJbLV col-12-12")
     await hadndling_and_database(boxes,db,full_data_flipkart,url,validated_data)

                               
async def hadndling_and_database(boxes,db,full_data_flipkart,url,validated_data):
        for box in boxes :
                            name,description,price,rating,total_rating,reviews = flipkart_scraper(box)
                            if not name :
                                                  continue
                            else :
                                                  full_data_flipkart.append((name,description,price,rating,total_rating,reviews))
                                                  logging.info(f"Data fetched from url : {url} : succes ")
        for i in full_data_flipkart:
                                        ensure_data =  flipkart_data_ensure(device=i[0],features=i[1],price=i[2],rating=i[3],total_rating=i[4],total_reviews=i[5])
                                        validated_data.append(ensure_data)
        for data in validated_data:
                               await db.execute("INSERT OR IGNORE INTO flipkart(name,features,price,rating,total_rating,total_reviews) VALUES (?,?,?,?,?,?)",(data.device,data.features,data.price,data.rating,data.total_rating,data.total_reviews))
                               await db.commit()


async def main():
    urls = [f"https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}" for i in range(1,31)]
    full_data_flipkart = []
    validated_data = []
    async with aiohttp.ClientSession() as session :
                    asyncio.sleep(4)
                    async with aiosqlite.connect(".gitignore/data/db/flipkart.db") as db:
                                       await db.execute("""
                                       CREATE TABLE IF NOT EXISTS flipkart(
                                                  id INTEGER PRIMARY KEY,
                                                  name TEXT,
                                                  features TEXT,
                                                  price TEXT,
                                                  rating REAL,
                                                  total_rating INTEGER,
                                                  total_reviews INTEGER,
                                                  UNIQUE(name,price)
                                       ) 
                                           """)
                                       await db.commit()
                                       for url in urls :
                                               print(url)
                                       task = [passing_soup_block_flipkart(url,full_data_flipkart,session,db,validated_data) for url in urls]
                                       await asyncio.gather(*task)
                                       for i in full_data_flipkart:
                                                     ensure_data =  flipkart_data_ensure(device=i[0],features=i[1],price=i[2],rating=i[3],total_rating=i[4],total_reviews=i[5])
                                                     validated_data.append(ensure_data)

                         
        
asyncio.run(main())
