import pandas as pd
from bs4 import BeautifulSoup

room_df = pd.read_csv('data/roommates.csv')
def add_room(row):
    html_temp_room = f"""

        <div class="roommate">
            <a href="../profile-templates/roommate-pf.html" style="text-decoration: none; color: #333333;">
                <img src="../../images/{row['ImagePath']}" class="roommate-profile">
                <div class="roommate-info-cont">
                    <a class="roommate-info">{row['Name']}</a>
                    <a class="roommate-info">{row['Age']}</a>
                    <a class="roommate-info">{row['Hometown']}</a>
                </div>
            </a>
            <a class="roommate-about-me">{row['Bio']}</a>
        </div>
        
    """
    return html_temp_room

#generate a house object now
first = add_room(room_df.iloc[1])

with open('src/html/links/roommates.html', 'r', encoding="utf8") as file:
    content = file.read()
    room = BeautifulSoup(content, 'html.parser')

target = room.find(id="grid")

if target:
    for index, row, in room_df.iterrows():
        content = add_room(row)
        new_room = BeautifulSoup(content, 'html.parser')
        target.append(new_room)

    with open('src/html/links/roommates.html', 'w', encoding="utf-8") as file:
        file.write(str(room))

    print("done")

