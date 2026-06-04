import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel,model_validator
import json
import tracemalloc

tracemalloc.start()

class EnsuringData(BaseModel):
    
    Book_name : str
    Book_price : float
    Book_type : str

    @model_validator(mode='after')
    def prevent_bug(self):
        if self.Book_name.strip() == "" or self.Book_type.strip() == "":
            raise ValueError("Data cannot be empty")
        if self.Book_price <= 0 :
            raise ValueError("The price should be greater than zero")
        return self
    
def url_creation():
    
    for i in range(1,51):
        url = f"http://books.toscrape.com/catalogue/page-{i}.html"
        yield url

def response_of_url(urls):
    
    for url in urls:
                  try :
                              response = requests.get(url,timeout=8)
                              response.encoding = "utf-8"
                              response.raise_for_status()
                              yield response.text
                  except requests.RequestException as e:
                              print(F"URL : {url} Fetched failed . Reason : {e}")
                              continue
                         

def extracting_title_price(blocks):
     
     for block in blocks:
           title = block.find("h3").find("a")["title"]
           price = block.find("p",class_="price_color").text
           price = float(price.replace("£",""))
           price_type = "expensive" if price>20 else "cheap"
           yield title,price,price_type

def parsing_data(sources):
    
     for source in sources :
          soup = BeautifulSoup(source,"html.parser")
          big_block = soup.find_all("article",class_="product_pod")
          for title,price,price_type in extracting_title_price(big_block):
                      yield  EnsuringData(Book_name=title,Book_price=price,Book_type=price_type)

urls = url_creation()
response = response_of_url(urls)
parsed = parsing_data(response)

with open("books.json","w",encoding="utf-8") as f :
       
       f.write("[\n")
       
       first = True

       for book in parsed:
                  
                  if not first:
              
                       f.write(",\n")
                     
                  json.dump(book.model_dump(),f)

                  first = False

       f.write("\n]")


      

current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f" Fetch complete . The total ram usage was {peak/1024/1024:.2f} Mb")



    
 


            
