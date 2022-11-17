from flask import Flask

app = Flask('__name__')

@app.route('/')
def IndexPage():
    return '<h1> Welcome back to server, again.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
