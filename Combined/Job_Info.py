from pydantic import BaseModel,model_validator
import requests
from bs4 import BeautifulSoup
import json

class Ensuring_Data(BaseModel):

    Job_name : str
    Company : str
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

def extracting_everything(name,company,location):
         for job in name :
                    job_name = job.find("h2").next_sibling.strip()
                    print(job_name)
         company_name = company[0].find("br").next_sibling.strip()
         print(company_name)
         loc = location[0].find("a").text
         return job_name,company_name,loc

def parsing_data(responses):
         for response in responses :
             
             soup = BeautifulSoup(response,"html.parser")
             job_name = soup.select("div.job-description")
             print(job_name)
             company_name = soup.select("span.company-name")
             print(company_name)
             job_loc = soup.select("span.listing-location")
             print(job_loc)
             job_date = soup.select("time")[0].text
             print(job_date)
             r_name,r_com,r_loc = extracting_everything(job_name,company_name,job_loc)

             yield Ensuring_Data(Job_name=r_name,Company=r_com,Job_location=r_loc,Job_posted_date=job_date)

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

        

        
