from bs4 import BeautifulSoup 

html = """
<div class="school">
  <div class="classroom" id="class-1">
    <h2 class="class-name">Mathematics</h2>
    <div class="teacher">
      <span class="name">Mr. Smith</span>
    </div>
    <ul class="students">
      <li class="student">
        <span class="name">Alice</span>
        <span class="grade">A</span>
      </li>
      <li class="student">
        <span class="name">Bob</span>
        <span class="grade">B</span>
      </li>
    </ul>
  </div>

  <div class="classroom" id="class-2">
    <h2 class="class-name">Science</h2>
    <div class="teacher">
      <span class="name">Ms. Johnson</span>
      <span class="experience">8 years</span>
    </div>
    <ul class="students">
      <li class="student">
        <span class="name">Charlie</span>
        <span class="grade">A</span>
      </li>
      <li class="student">
        <span class="name">Diana</span>
        <span class="grade">C</span>
      </li>
    </ul>
  </div>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
for div in soup.select(".classroom"):
                      class_name = div.find("h2",class_="class-name").text
                      room = div.find("div",class_="teacher") 
                      teacher_name = room.find("span",class_="name").text
                      experience = room.find("span",class_="experience")
                      experience = experience.text if experience else "unknown"
                      students = div.find_all("li",class_="student")
                      print(f"\n Class : {class_name} \n Teacher : {teacher_name} ({experience}) \n Students : ")  
                      for student in students:
                                  name =  student.find("span",class_="name").text
                                  grade = student.find("span",class_="grade").text
                                  print(f"  -{name} | Grade : {grade}")
    