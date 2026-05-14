from pydantic import BaseModel,model_validator,field_validator
import sqlite3


class EnsuringData(BaseModel):
     name : str
     year : int
     rating : float

     @model_validator(mode='after')
     def Ensuring(self):
               if self.name.strip() == "":
                     raise ValueError("Movie name cannot be empty")
               if self.rating <= 0 or self.rating > 10:
                     raise ValueError("Rating cant be less than or equal to zero and more than 10")
               if self.year > 2026 or self.year < 1878:
                     raise ValueError("Movie year cant be future or early before movie existed ...")
               return self
     
class checking_rows(BaseModel):
        rows : int 
        @field_validator('rows')
        @classmethod
        def row_checking(clas,value):
                if value <= 0 :
                        raise ValueError("No Movies Added Yet")
                return value



conn = sqlite3.connect("Movies.db")
cur = conn.cursor()

cur.execute("""

            CREATE TABLE IF NOT EXISTS movies(
                    movie_name TEXT UNIQUE,
                    year INTEGER,
                    rating REAL
            )
    """)

conn.commit()

def checking_row_num():
        num = cur.execute("SELECT COUNT(*) FROM movies")
        row_count = num.fetchone()[0]
        return row_count


while True:
                 try:
                                   options = int(input(" Please Choose an Option \n 1.Add movie \n 2.Show all movies \n 3.Show top movies \n 4.Update rating \n 5.Delete Movie \n :  "))
                 except :
                             print("\n Sorry we couldnt recognise the input . Try again")
                             continue
                 if options == 1:
                                        try:
                                                          movie_name = str(input("\n Enter movie name : ")).lower()
                                                          movie_year = int(input(" Enter released year : "))
                                                          movie_rating = float(input(" Enter movie rating : "))
                                                          EnsuringData(name=movie_name,year=movie_year,rating=movie_rating)
                                                          cur.execute("""
                                                                        INSERT INTO movies(movie_name,year,rating)
                                                                        VALUES(?,?,?)
                                                                           """,(movie_name,movie_year,movie_rating))
                                                          conn.commit()
                                                          print("\n Movie added")
             
                                        except Exception as e:
                                                                  print(f"Movie added failed . Reason : {e}") 

                 elif options == 2:
                                        row = checking_row_num()
                                        try:
                                                           checking_rows(rows=row)
                                                           all_movies = cur.execute("SELECT * FROM movies")        
                                                           for i in all_movies.fetchall():
                                                                           print(f"\n Movie name : {i[0]} \n Released Year : {i[1]} \n Rating : {i[2]}")

                                        except Exception as e :
                                                                     print(f"\n Showing Movies failed . Reason : {e}") 

                 elif options == 3:
                                       row = checking_row_num()
                                       try :
                                                            checking_rows(rows=row)
                                                            top_movies = cur.execute("SELECT movie_name,year,rating FROM movies ORDER BY rating DESC LIMIT 3")
                                                            for i in top_movies.fetchall():
                                                                           print(f"\n Movie name : {i[0]} \n Released Year : {i[1]} \n Rating : {i[2]}")

                                       except Exception as e :
                                                                     print(f"\n Showing Movies failed . Reason : {e}")
                 elif options == 4 :
                                      row = checking_row_num()
                                      try:
                                                                 checking_rows(rows=row)
                                                                 changing_movie = str(input("\n Enter the movie name [rating changing movie] : ")).lower()
                                                                 changing_movie_year = cur.execute("SELECT year FROM movies WHERE movie_name = ? ",(changing_movie,))
                                                                 changing_movie_year = changing_movie_year.fetchone()
                                                                 if changing_movie_year:
                                                                                 cm_year = changing_movie_year[0]
                                                                                 new_rate = float(input(" Enter the new rating : "))
                                                                                 EnsuringData(name=changing_movie,year=cm_year,rating=new_rate)
                                                                                 cur.execute("UPDATE movies SET rating = ? WHERE movie_name = ? ",(new_rate,changing_movie))
                                                                                 conn.commit()
                                                                                 print("\n Rating Updated")
                                                                 else : 
                                                                         print("\n The movie nae you provided doesnt exist")            
                                      
                                      except Exception as e :
                                                                   print(f"\n Showing Movies failed . Reason : {e}")               

                 elif options == 5 :
                                      row = checking_row_num()
                                      try : 
                                                                 checking_rows(rows=row)
                                                                 deleting_movie = str(input("\n Enter Movie name [Deleting movie] : ")).lower()        
                                                                 cur.execute("DELETE FROM movies WHERE movie_name = ?",(deleting_movie,))    
                                                                 conn.commit()
                                                                 if cur.rowcount :
                                                                               print("\n Movie deleted ")
                                                                 else :
                                                                               print("\n Movie not exist in database")
                                                                         
                                      except Exception as e :
                                                               print(f"\n Showing Movies failed . Reason : {e}") 

                 else :
                          print("\n Option not exist")  

                 
                 con_ex = str(input("\n Do you want to continue to menu ? : "))
                 if con_ex.lower() == "yes":
                         continue
                 elif con_ex.lower() == "no":
                         break
                 else :
                         print("\n Since you typed wrong response we are defaulting to quit all Your changes are saved No worries ✅")
conn.close()