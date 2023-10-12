import webtop as w
from random import randint
from time import strftime
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    text = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def user_detail():
    form = ReusableForm(request.form)
    linksDict = {}
    linksDict["links"] = []
    linksDict['no_of_links'] = 0
    linksDict['no_of_keywords'] = 0
    linksDict['keywords'] = []
    if request.method == 'POST':
        text=request.form['text']
        
        if form.validate() > 0:
            links = []
            if len(text) > 0:
                links = w.outlinks(text)
                keywords = w.keywords(text)

            if len(links)>1  & len(links)<500:
                linksDict['links'] = links
                linksDict['no_of_links'] = len(links)
                linksDict['no_of_keywords'] = len(keywords)
                linksDict['keywords'] = keywords

            flash('Success')
        else:
            flash('Error: Address is Required')

    return render_template('mainPage.html', form=form,linksDict = linksDict)

if __name__ == "__main__":
    app.run()
