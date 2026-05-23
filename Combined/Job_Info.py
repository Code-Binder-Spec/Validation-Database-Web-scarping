from pydantic import BaseModel,model_validator
import requests
from bs4 import BeautifulSoup
import json

class Ensuring_Data(BaseModel):

    Job_name : str
    Company : str
    Job_location : str 
    Job_posted_date : str
    Job_description : str

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

def extracting_everything(name,company,location,jobdes):
         description = ""
         h2 = name[0].find("h2") if name else None
         job_name = h2.next_sibling.strip() if h2 else "missing"
         for p in jobdes:
                description = description + "\n" + p.text
         br = company[0].find("br") if company else None
         company_name = br.next_sibling.strip() if br else "missing"
         a = location[0].find("a") if location else None
         loc = a.text if a else "missing"
         return job_name,company_name,loc,description

def parsing_data(responses):
        
         for response in responses :
             
             soup = BeautifulSoup(response,"html.parser")
             job_name = soup.select("div.job-description")
             job_description = soup.select("div.job-description p")
             company_name = soup.select("span.company-name")
             job_loc = soup.select("span.listing-location")
             job_date = soup.select("time")
             real_date = job_date[0].text if job_date else "missing"
             r_name,r_com,r_loc,r_description = extracting_everything(job_name,company_name,job_loc,job_description)
             try:
                       yield Ensuring_Data(Job_name=r_name,Company=r_com,Job_location=r_loc,Job_posted_date=real_date,Job_description=r_description)
             except ValueError as e:
                       print(f"Data parsing failed . reason : {e}")
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

        

        
