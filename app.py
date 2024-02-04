from flask import Flask, render_template

app = Flask(__name__)

@app.route('/movierulz')
def movierulz():
    movie_id = '123'  # Example movie ID
    return render_template('movie_details.html', movie_id=movie_id)

if __name__ == '__main__':
    app.run(debug=True)
