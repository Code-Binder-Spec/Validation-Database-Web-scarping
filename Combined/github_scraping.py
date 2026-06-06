import asyncio
from bs4 import BeautifulSoup
from pydantic import BaseModel,field_validator
import aiohttp
import aiosqlite
import logging

logging.basicConfig(filename="Github.logger",level=logging.INFO)

class Cleaning_data(BaseModel):
       
        username : str
        reponame : str
        description : str | None
        total_stars : int
        total_stars_today : int
        total_fork : int
        programing_language : str | None
        time_period : str

        @field_validator("description",mode="before")
        @classmethod
        def checking_none(cls,v):
                if v.lower() == "no description found":
                        actual_des = None
                        return actual_des
                else :
                        return v

        @field_validator("total_stars","total_fork",mode="before")
        @classmethod
        def cleaning_stars_fork(cls,v):
                actual_data = v.replace(",","")
                return int(actual_data)
        @field_validator("total_stars_today",mode="before")
        @classmethod
        def cleaning_today_stars(cls,v):
                splitted_data = v.split()
                stars = splitted_data[0].replace(",","")
                return int(stars)
        @field_validator("programing_language",mode="before")
        @classmethod
        def cleaning_language(cls,v):
                if v.lower() == "no language added":
                         actual_language = None
                         return actual_language
                else :
                        return v

        

sem = asyncio.Semaphore(3)



async def getting_source(url,session):
            async with sem :
                    async with session.get(url) as response :
                            return await response.text()
                    

def user_repo_scraper(box):
      
        try :
                    user_and_repo_block = box.find("h2")
                   
                    if user_and_repo_block:
                               data_row = user_and_repo_block.text.strip()
                               data_list = data_row.split()
                               data_list.remove("/")
                               username = data_list[0]
                               reponame = data_list[1]

                               return username,reponame
                    
                    else :
                            raise Exception("Didnt find user_and_repo_block")
        except Exception as e :
                                  raise ValueError(f"Scraping repo and user name failed due to error {e}")

def description_scraper(box):
     
        try:
                     description = box.find("p",class_="col-9 color-fg-muted my-1 tmp-pr-4")
                     if description:
                                  cleaned_description = description.text.strip()
                                  return cleaned_description
                     else :
                                  description = "No description found"
                                  return description
        except Exception as e :
                            raise ValueError(f"Scraping description failed due to error {e}")


def star_fork_scraper(box):
      
        try :
                star_fork_block = box.find_all("a",class_="tmp-mr-3 Link Link--muted d-inline-block") 
                if star_fork_block:
                           total_star = star_fork_block[0].text.strip()
                           total_fork = star_fork_block[1].text.strip()
                           return total_star,total_fork  
                else :
                        raise Exception("Didnt find star_fork_block ")

        except Exception as e :
                               raise ValueError(f"Scraping star and fork failed due to error {e}")
                  

def total_stars_today_scraper(box):
       
        try :
                  today_star_block = box.find("span",class_="d-inline-block float-sm-right")
                  if today_star_block:
                               today_stars = today_star_block.text.strip()
                               return today_stars
                  else :
                               today_stars = "0 stars"
                               return today_stars
        except Exception as e :
                                raise ValueError(f"Scraping todays star failed due to error {e}")


def language_scraper(box):
        try:
                 language_block = box.find("span",itemprop="programmingLanguage")
                 if language_block:
                              programming_language = language_block.text.strip()
                              return programming_language
                 else :
                              programming_language = "No language added"
                              return programming_language
        except Exception as e :
                                raise ValueError(f"Language scraping failed due to error {e}")
                 

def exctracting_caller(box,time):
     
        user_name,reponame = user_repo_scraper(box)
        description = description_scraper(box)
        total_star,total_fork = star_fork_scraper(box)
        total_today_star = total_stars_today_scraper(box)
        programming_language = language_scraper(box)

        return {"username":user_name , "reponame" : reponame , "description" : description , "total_stars" : total_star , "total_stars_today" : total_today_star , "total_fork" : total_fork , "programing_language" : programming_language , "time_period" : time }
        

async def passing_blocks(url,session,full_data,time):
          source = await getting_source(url,session)
          soup = BeautifulSoup(source,"html.parser")
          boxes = soup.find_all("article",class_="Box-row")
          succes = True
          for box in boxes:
                      try:
                                data = exctracting_caller(box,time)
                                full_data.append(data)
                      except Exception as e:
                                succes = False
                                
          if succes:
                  logging.info(f"{url} Fetched : succes")
          else :
                logging.error(f"Data failed due to error {e}")  
                  

async def sql_writing(db,data):
         await db.execute("INSERT INTO github_trend(username,reponame,description,total_stars,total_fork,total_stars_today,programming_language,time_period) VALUES (?,?,?,?,?,?,?,?)",(data.username,data.reponame,data.description,data.total_stars,data.total_fork,data.total_stars_today,data.programing_language,data.time_period))
         await db.commit()
         return db

async def main():
    full_data = []
    validated_data = []
    async with aiohttp.ClientSession() as session:
             async with aiosqlite.connect("githubdata.db") as db:
                           await db.execute("""

                                     CREATE TABLE IF NOT EXISTS github_trend(
                                           id INTEGER PRIMARY KEY,   
                                           username TEXT,   
                                           reponame TEXT,
                                           description TEXT,
                                           total_stars INTEGER,
                                           total_fork INTEGER,
                                           total_stars_today INTEGER,
                                           programming_language TEXT,
                                           time_period TEXT
                                           )              
                                                 """)
                           await db.commit()

                           await asyncio.gather(
                                    passing_blocks("https://github.com/trending",session,full_data,"Daily"),
                                    passing_blocks("https://github.com/trending?since=weekly",session,full_data,"Weekly"),
                                    passing_blocks("https://github.com/trending?since=monthly",session,full_data,"Monthly")
                                                )
                           for dict in full_data:
                                try :
                                        t1 = Cleaning_data(**dict)
                                        validated_data.append(t1)
                                except Exception as e :
                                        logging.error(f"The data unpacking failed due to error . {e}")
                           for data in validated_data:
                                            await sql_writing(db,data) 



asyncio.run(main())
    