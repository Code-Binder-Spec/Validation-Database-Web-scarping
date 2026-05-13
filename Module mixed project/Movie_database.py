from pydantic import BaseModel,model_validator
import sqlite3


class EnsuringData(BaseModel):
     name : str
     year : int
     rating : float

     @model_validator(mode='after')
     def Ensuring(self):
               if self.name == "":
                     raise ValueError("Movie name cannot be empty")
               if self.rating <= 0 :
                     raise ValueError("Rating cant be less than or equal to zero")
               if self.year > 2026 or self.year < 1878:
                     raise ValueError("Movie year cant be future or early before movie existed ...")
               return self



conn = sqlite3.connect("Movies.db")
cur = conn.cursor()

cur.execute("""

            CREATE TABLE IF NOT EXISTs movies(
                    movie_name TEXT,
                    year INTEGER,
                    rating REAL
            )
    """)

conn.commit()

def checking_row_num():
        num = cur.execute("SELECT (*) FROM movies")
        row_count = num.fetchone()[0]
        return row_count

options = int(input("Please Choose an Option \n 1.Add movie \n 2.Show all movies \n 3.Show top movies \n 4.Update rating \n 5.Delete Movie "))

while True:

                 if options == 1:
                                        try:
                                                          movie_name = str(input("Enter movie name : "))
                                                          movie_year = int(input("Enter released year : "))
                                                          movie_rating = float(input("Enter movie rating : "))
                                                          EnsuringData(name=movie_name,year=movie_year,rating=movie_rating)
                                                          cur.execute("""
                                                                        INSERT INTO movies(movie_name,year,rating)
                                                                        VALUES(?,?,?)
                                                                           """,(movie_name,movie_year,movie_rating))
                                                          conn.commit()
             
                                        except Exception as e:
                                                                  print(f"Movie added failed . Reason : {e}") 

                 elif options == 2:
                                        row = checking_row_num()
                                        try:
                                               if row >= 1:
                                                           all_movies = cur.execute("SELECT movie_name,year,rating FROM movies")        
                                                           for i in all_movies.fetchall():
                                                                   for name,year,rating in i :
                                                                           print(f"Movie name : {name} \n Released Year : {year} \n Rating : {rating}")
                                               else :
                                                                    print("-----------No Movies Added Yet-----------")

                                        except Exception as e :
                                                                     print(f"Showing Movies failed . Reason : {e}") 

                 elif options == 3:
                                       row = checking_row_num()
                                       try :
                                               if row >=1 :
                                                            top_movies = cur.execute("SELECT movie_name,year,rating FROM movies ORDER BY rating DESC LIMIT 3")
                                                            for i in top_movies.fetchall():
                                                                   for name,year,rating in i :
                                                                           print(f"Movie name : {name} \n Released Year : {year} \n Rating : {rating}")
                                               else :
                                                                    print("-----------No Movies Added Yet-----------")

                                       except Exception as e :
                                                                     print(f"Showing Movies failed . Reason : {e}")
                 elif options == 4 :
                                      row = checking_row_num()
                                      try :
                                              if row >= 1 :
                                                                 changing_movie = str(input("Enter the movie name [rating changing movie] : "))
                                                                 new_rate = float(input("Enter the new rating : "))
                                                                 cur.execute(f'UPDATE movies SET rating = {new_rate} WHERE movie_name = {changing_movie} ')
                                                                 conn.commit()
                                                                 print("Rating Updated")

                                              else :
                                                         print("-----------No Movies Added Yet-----------")            
                                      
                                      except Exception as e :
                                                                   print(f"Showing Movies failed . Reason : {e}")               

                 elif options == 5 :
                                      row = checking_row_num()
                                      try : 
                                              if row >= 1:
                                                                 deleting_movie = str(input("Enter Movie name [Deleting movie] : "))        
                                                                 cur.execute(f'DELETE movies WHERE movie_name = {deleting_movie} ')    
                                                                 conn.commit()
                                                                 print("Movie deleted ")
                                              else  :                      
                                                                 print("-----------No Movies Added Yet-----------")
                                      except Exception as e :
                                                               print(f"Showing Movies failed . Reason : {e}") 

                 else :
                          print("Option not exist")  
                                
                
                 con_ex = str(input("Do you want to quit : "))
                 if con_ex.lower() == "yes":
                         break
                 elif con_ex.lower() == "no":
                         continue
                 else :
                         print("Since you typed wrong response we are defaulting to quit all Your changes are saved No worries ✅")
                 