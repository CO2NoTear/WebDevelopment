from flask import Flask, request, redirect, abort, \
        render_template, url_for

app = Flask('__name__')

@app.route('/')
def indexPage():
    # simple request instance
    user_agent = request.headers.get('User-Agent')
    return '<p> Welcome back to server Qomolangma.\n \
            Your browser is \n%s, right?</p>' % user_agent

@app.route('/user/<name>')
#it gave a var name to func
def userPage(name):
    #Here we test abort() for user validation checking
    if name != 'CO2NoTear':
        #Noticing that this would throw ERROR expection and quit
        #just like normally 404 NOT FOUND
        abort(404)
    return render_template('user.html', name = name)

@app.errorhandler(404)
def pageNotFound(e):
    #Here we test url_for func to generate dynamic url for Links
    #for html models.
    return render_template('404.html', url_for_CO2 = 'http://123.249.78.113:2333' + url_for('userPage', name='CO2NoTear', _external=False)), 404
    # WARNING!!!!!!
    # if you set _external as True, url_for func will give you
    # a absolute url, HOWEVER, its IP address is 0.0.0.0, namely
    # unable to use simply in the links.

@app.route('/jump')
def jumpToIndex():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)
