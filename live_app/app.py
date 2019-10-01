import pandas as pd
from flask import Flask, request, render_template
# pd.set_option('colheader_justify', 'center')

app = Flask(__name__)
listing = pd.read_csv('data/listing.csv',keep_default_na=False)
recc = pd.read_csv('data/nmfullrecc.csv',keep_default_na=False)

@app.route('/')
def index():
    return render_template('index_demo.html')

@app.route('/result', methods=['POST','GET'])
def similar_routes():
    if request.method == 'POST':
        query = request.form
        i = str(query['myCountry'])
        ind = listing.loc[listing['listed']== i].index.to_list()[0]
        first = listing.loc[listing['route']== (recc['recc_0'].iloc[ind])].listed.to_list()[0]
        second = listing.loc[listing['route']== (recc['recc_1'].iloc[ind])].listed.to_list()[0]
        third = listing.loc[listing['route']== (recc['recc_2'].iloc[ind])].listed.to_list()[0]
        fourth = listing.loc[listing['route']== (recc['recc_3'].iloc[ind])].listed.to_list()[0]
        fifth = listing.loc[listing['route']== (recc['recc_4'].iloc[ind])].listed.to_list()[0]
    return render_template('new_result.html', first=first, second =second, third=third, fourth=fourth, fifth=fifth)

if __name__ == '__main__':
    app.run()
