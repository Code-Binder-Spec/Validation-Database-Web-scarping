from bs4 import BeautifulSoup 

html = """
<div class="blog">
  <article class="post" id="post-1">
    <h2 class="post-title">Learning Python</h2>
    <span class="author">by John</span>
    <span class="date">2024-01-15</span>
    <div class="tags">
      <a class="tag" href="/tags/python">Python</a>
      <a class="tag" href="/tags/coding">Coding</a>
    </div>
  </article>

  <article class="post" id="post-2">
    <h2 class="post-title">Web Scraping Guide</h2>
    <span class="author">by Sarah</span>
    <span class="date">2024-02-20</span>
    <div class="tags">
      <a class="tag" href="/tags/scraping">Scraping</a>
      <a class="tag" href="/tags/python">Python</a>
      <a class="tag" href="/tags/web">Web</a>
    </div>
  </article>
</div>
"""

soup = BeautifulSoup(html, "html.parser")
for div in soup.select(".post"):
    title = div.find("h2",class_="post-title").text
    author = div.find("span",class_="author").text
    author = author.replace("by","")
    date = div.find("span",class_="date").text
    for link in div.select("div.tags"):
         herf = link.find("a")["href"]
         print(f"\n Title : {title} \n Author : {author} \n Date : {date} \n Href : {herf}")


