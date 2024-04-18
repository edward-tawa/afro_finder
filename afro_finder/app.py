from flask import Flask, render_template, url_for, jsonify
from sqlalchemy.orm import sessionmaker
from readdb import scholarship


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', scholarship=scholarship)
    



@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')






if __name__ == '__main__':
    app.run(debug=True)