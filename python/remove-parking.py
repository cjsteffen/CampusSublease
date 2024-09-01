from bs4 import BeautifulSoup

with open('src/html/links/parking.html', 'r', encoding="utf8") as file:
    content = file.read()
    houses = BeautifulSoup(content, 'html.parser')

target = houses.find(id="grid")

if target:
    target.clear()

with open('src/html/links/parking.html', 'w', encoding="utf-8") as file:
        file.write(str(houses))

print("clear")