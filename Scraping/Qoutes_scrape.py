import requests
from bs4 import BeautifulSoup
import tracemalloc
import json

def url_creation():
            for i in range(1,11):
                       url = f"http://quotes.toscrape.com/page/{i}/"
                       yield url

def getting_response(urls):
        for url in urls :
             try:
                      response = requests.get(url,timeout=5)
                      response.encoding = "utf-8"
                      response.raise_for_status()
                      yield response.text

             except requests.RequestException:
                      continue

def extracting_quotes(blocks):
        for block in blocks :
                 quotes = block.find("span",class_="text").text
                 author = block.find("small",class_="author").text
                 yield quotes,author
                

def parsing_data(responses):
        for response in responses :
                soup = BeautifulSoup(response,"html.parser")
                quote_block = soup.find_all("div",class_="quote")
                for quote,author in extracting_quotes(quote_block):
                        yield quote,author

def main():
            
            tracemalloc.start()
            data = []
            total_quotes_fetched = 0
            total_url_fetched = 0 
            total_request_accepted = 0
            for url in url_creation():
                    total_url_fetched += 1
                    responses = getting_response([url])
                    for response in responses:
                               total_request_accepted += 1
                               parsed = parsing_data([response])
                               for quote,author in parsed:
                                           total_quotes_fetched += 1
                                           data.append({
               
                                                      "quote":quote,
                                                      "author":author
               
                                                                      })

            with open("quotes.json","w",encoding = "utf-8") as f:  
                                json.dump(data,f,indent = 4)         

            print(f"\n Total url fetched : {total_url_fetched}")
            print(f"\n Total url requests accepted : {total_request_accepted} ")
            print(f"\n Total quotes fetched : {total_quotes_fetched}")
            current,peak = tracemalloc.get_traced_memory()
            print(f"\n The peak ram usage is {peak/1024/1024:.2f} mb")
            tracemalloc.stop()




if __name__ == "__main__":
                    main()



    