from flask import Flask, request, redirect, abort, \
        render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from MyForms import LoginForm

app = Flask('__name__')
app.config['SECRET_KEY'] = 'qomolangma'
bootstrap = Bootstrap(app)

#class NameForm(FlaskForm):
#   name = StringField("What's your name?", validators=[DataRequired()])
#   submit = SubmitField('Submit')
#所有表单放到MyForms.py文件里面，用Import导入



@app.route('/', methods=['POST', 'GET'])
def indexPage():
    ## simple request instance
    #user_agent = request.headers.get('User-Agent')
    #return '<p> Welcome back to server Qomolangma.\n \
    #        Your browser is \n%s, right?</p>' % user_agent
    if request.method == 'POST':
        session['UID'] = request.form['UID']
        session['UPassword'] = request.form['UPassword']
        return redirect(url_for('indexPage'))
    else:
        return render_template('Index.html',userid=session.get('UID'),password=session.get('UPassword'))

@app.route('/login', methods=['GET','POST'])
def loginPage():
    name = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('oops, looks like you just changed your name.')
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('loginPage'))

    return render_template('login.html', form = form, name=session.get('name'), password=session.get('password'))

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
