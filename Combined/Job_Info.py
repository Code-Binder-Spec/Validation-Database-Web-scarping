from pydantic import BaseModel,model_validator
import requests
from bs4 import BeautifulSoup
import json

class Ensuring_Data(BaseModel):

    Job_location : str 
    Job_posted_date : str

    @model_validator(mode='after')
    def PreventingBugs(self):
        if any ([self.Job_name.strip() == "", self.Job_location.strip() == "" , self.Job_posted_date.strip() == "" , self.Company.strip() == ""]):
            raise ValueError("Missing field.")
        return self
        
def creating_url():
    for i in range(8044,8085):
        url = f"https://www.python.org/jobs/{i}/"
        yield url

def getting_response(urls):
    for url in urls:
        try :
                     response = requests.get(url,timeout=4)
                     response.raise_for_status()
                     yield response.text
        except Exception as e :
                     print(f"Url request failed . Reason : {e}")

def extracting_everything(loc,dat):
      location = loc.find("a")["title"]
      date = dat.find("time")["datetime"]
      return location,date

def parsing_data(responses):
      for response in responses:
             soup = BeautifulSoup(response,"html.parser")
             blocks = soup.find("div",class_="container")
             job_name_company_block = blocks.find("span",class_ = "company-name")
             location_block = blocks.find("span",class_="listing-location")
             date_block = blocks.find("span",class_ = "listing-posted")
             if not blocks:
                   print("its block missing")
                   continue
             elif not location_block:
                   print("Location missing") 
                   continue
             elif not date_block:
                   print("Date missing")
                   continue
             location,date = extracting_everything(location_block,date_block)
             yield Ensuring_Data(Job_location=location,Job_posted_date=date)

urls = creating_url()
response = getting_response(urls)
parse = parsing_data(response)

with open("Job.json","w",encoding="utf-8") as f :
      f.write("[\n")
      first = True

      for job in parse:
            
            if not first :
                  f.write(",\n")
            
            json.dump(job.model_dump(),f)
            
            first = False 
            
      f.write("\n]")

        

        
