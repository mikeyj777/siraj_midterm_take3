from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import paralleldots
import stripe

app = Flask(__name__)

pub_key = ''
secret_key = ''

stripe.api_key = secret_key

class Analyze:
    report_key = ''
    sentiment_key = ''

    def __init__(self, company):
        self.company = company
        self.url = 'https://datafied.api.edgar-online.com/v2/corefinancials/ann?primarysymbols=' + \
            self.company + '&appkey=' + self.report_key

    def get_fin_report(self):
        URL = self.url
        PARAMS = {}
        r = requests.get(url=URL, params=PARAMS)
        self.data = r.json()

        return None

    def sentiment_analysis(self):
        paralleldots.set_api_key(self.sentiment_key)
        self.response = paralleldots.sentiment(self.data, 'en')
        return None

    
    def predict(self):
        self.get_fin_report()
        self.sentiment_analysis()
        goodornot = self.response['sentiment']
        result = max(goodornot, key=goodornot.get)
        return result


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        return redirect(url_for('reallyobscurefilename'))
    return render_template('index.html', error=error, pub_key = pub_key)

@app.route('/reallyobscurefilename', methods=['POST', 'GET'])
def reallyobscurefilename():
    result = ''

    if request.method == 'POST': 
        company = request.form['company']
        new_analysis = Analyze(company=company)
        ans = new_analysis.predict()
        if ans in ['positive', 'neutral', 'negative']:
            result = 'Our expert professional guidance is that this is a ' + \
                ans + ' investment.'
    return render_template('reallyobscurefilename.html', result = result)

if __name__ == "__main__":
    app.run(debug=True)