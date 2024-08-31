from flask import Flask, render_template, request, url_for, flash, redirect
import os

app = Flask(__name__)
print(os.environ.get('SECRET_KEY'))
print("after")
# Don't Do this in production. 
# In Project IDX Need to update to use Google Secrets Manager
app.config['SECRET_KEY'] = 'SuperSecretKey'

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('create.html')