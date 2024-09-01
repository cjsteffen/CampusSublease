import pandas as pd
from bs4 import BeautifulSoup

parking_df = pd.read_csv('data/parking.csv')
def add_parking(row):
    html_temp_parking = f"""

        <div class="parking"><a href="../profile-templates/parking-pf.html" style="text-decoration: none; color: #333333;">{row['Address']}
            <img src="../../images/{row['ImagePath']}" class="parking-profile">
            </a>
            <div class="parking-info-cont">
                <a class="parking-info">${row['Price']} / m</a>
                <a class="parking-info">{row['Covered']}</a>
            </div>
        </div>
        
    """
    return html_temp_parking

#generate a house object now
first = add_parking(parking_df.iloc[1])

with open('src/html/links/parking.html', 'r', encoding="utf8") as file:
    content = file.read()
    parking = BeautifulSoup(content, 'html.parser')

target = parking.find(id="grid")

if target:
    for index, row, in parking_df.iterrows():
        content = add_parking(row)
        new_parking = BeautifulSoup(content, 'html.parser')
        target.append(new_parking)

    with open('src/html/links/parking.html', 'w', encoding="utf-8") as file:
        file.write(str(parking))

    print("done")

