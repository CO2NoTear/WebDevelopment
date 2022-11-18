from flask import Flask, request, redirect, abort

app = Flask('__name__')

@app.route('/')
def IndexPage():
    # simple request instance
    user_agent = request.headers.get('User-Agent')
    return '<p> Welcome back to server Qomolangma.\n \
            Your browser is \n%s, right?</p>' % user_agent

@app.route('/user/<name>')
#it gave a var name to func
def UserPage(name):
    #Here we test abort() for user validation checking
    if name != 'CO2NoTear':
        #Noticing that this would throw ERROR expection and quit
        #just like normally 404 NOT FOUND
        abort(404)
    return '<h1>Welcome, %s!</h1>' % name

@app.route('/jump')
def jumpToIndex():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)
