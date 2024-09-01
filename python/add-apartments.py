import pandas as pd
from bs4 import BeautifulSoup

apt_df = pd.read_csv('data/apartments.csv')
def add_house(row):
    html_temp_apt = f"""
    
        <div class="apt" id={row['ID']}>
                <a href="/apt-view?id={row['ID']}" style="text-decoration: none; color: #333333;">{row['Address']}
                    <img src="../../images/profile-images/{row['ImagePath']}"class="apt-profile">
                </a>
            <div class="apt-info-cont">
                <a class="apt-info">{row['Bedrooms']} bed</a>
                <a class="apt-info">{row['Bathrooms']} bath</a>
                <a class="apt-info">{row['Roommates']} roommate</a>
                <a class="apt-info">${row['Price']} / m</a>
            </div>
        </div>
        
    """
    return html_temp_apt


with open('src/html/links/apartments.html', 'r', encoding="utf8") as file:
    content = file.read()
    houses = BeautifulSoup(content, 'html.parser')

target = houses.find(id="grid")

if target:
    for index, row, in apt_df.iterrows():
        content = add_house(row)
        new_house = BeautifulSoup(content, 'html.parser')
        target.append(new_house)

    with open('src/html/links/apartments.html', 'w', encoding="utf-8") as file:
        file.write(str(houses))

    print("done")

