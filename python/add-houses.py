import pandas as pd
from bs4 import BeautifulSoup

houses_df = pd.read_csv('data/houses.csv')
def add_house(row):
    html_temp_house = f"""

        <div class="house" id={row['ID']}>
                <a href="/house-view?id={row['ID']}" style="text-decoration: none; color: #333333;">{row['Address']}
                    <img src="../../images/profile-images/{row['ImagePath']}"class="house-profile">
                </a>
            <div class="house-info-cont">
                <a class="house-info">{row['Bedrooms']} bed</a>
                <a class="house-info">{row['Bathrooms']} bath</a>
                <a class="house-info">{row['Roommates']} roommate</a>
                <a class="house-info">${row['Price']} / m</a>
            </div>
        </div>
        
    """
    return html_temp_house

#generate a house object now
first = add_house(houses_df.iloc[1])

with open('src/html/links/houses.html', 'r', encoding="utf8") as file:
    content = file.read()
    houses = BeautifulSoup(content, 'html.parser')

target = houses.find(id="grid")

if target:
    for index, row, in houses_df.iterrows():
        content = add_house(row)
        new_house = BeautifulSoup(content, 'html.parser')
        target.append(new_house)

    with open('src/html/links/houses.html', 'w', encoding="utf-8") as file:
        file.write(str(houses))

    print("done")

