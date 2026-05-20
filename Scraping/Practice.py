from bs4 import BeautifulSoup 

html = """
<html>
  <body>
    <div class="store">
      <h1 id="store-name">TechShop</h1>

      <div class="product" id="p1">
        <h2 class="title">Wireless Mouse</h2>
        <p class="price">$25.99</p>
        <a href="/products/mouse" class="link">View</a>
      </div>

      <div class="product" id="p2">
        <h2 class="title">Mechanical Keyboard</h2>
        <p class="price">$89.99</p>
        <a href="/products/keyboard" class="link">View</a>
      </div>

      <div class="product featured" id="p3">
        <h2 class="title">4K Monitor</h2>
        <p class="price">$399.99</p>
        <a href="/products/monitor" class="link">View</a>
      </div>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
all_things = soup.select("p.price")
for i in all_things:
    print(i.text)
# Write your code below and run it to test!