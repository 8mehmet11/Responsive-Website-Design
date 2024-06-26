from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Responsive-Website-Design.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)













