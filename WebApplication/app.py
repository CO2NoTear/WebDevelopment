from flask import Flask, request, redirect, abort, \
        render_template, url_for, session, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, logout_user, login_user
#初始化flask-login
login_manager = LoginManager()
login_manager.session_protection = 'basic'
login_manager.login_view = 'indexPage'


from InitTablesORM import session as sqlsession
#所有表单放到MyForms.py文件里面，用Import导入
from MyForms import LoginForm, RegisterForm
from BuildConnection import SQL_URI
from InitTablesORM import User, Passage, Comment, Tool
app = Flask('__name__')

#设置session私钥
app.config['SECRET_KEY'] = 'qomolangma'
#设置sqlalchemy连接路径
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#初始化bootstrap
bootstrap = Bootstrap(app)
#初始化sqlalchemy
db = SQLAlchemy(app)

#login_manager 回调函数

@login_manager.user_loader
def load_user(user_id):
    return sqlsession.query(User).get(int(user_id))
login_manager.init_app(app)

#导航站
@app.route('/', methods=['POST', 'GET'])
def indexPage():
    form = LoginForm()
    if form.validate_on_submit():
        user = sqlsession.query(User).filter(User.UName==form.name.data).first()
        #新用户
        if user is None:
            session['feedback']='用户名不存在！'
        else:
            if user.UPassword == form.password.data:
                login_user(user, False)
                return redirect(request.args.get('next') or url_for('userPage', name=user.UName))
            else:
                session['feedback'] = '用户名或密码错误'
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('indexPage'))
    else:
        return render_template('Index.html', form=form, feedback=session.get('feedback'))

#登录界面
@app.route('/login', methods=['GET','POST'])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        user = sqlsession.query(User).filter(User.UName==form.name.data).first()
        #新用户
        if user is None:
            session['known'] = False
            flash('User not exists!')
        else:
            session['known'] = True
            if user.UPassword == form.password.data:
                return redirect(url_for('userPage', name=form.name.data))
            else:
                flash('Wrong password')
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('loginPage'))

    return render_template('login.html', form = form, name=session.get('name'), password=session.get('password'), known = session.get('known'))

#登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you\'ve already logged out.')
    return redirect(url_for('indexPage'))

#注册界面
@app.route('/register', methods=['POST', 'GET'])
def registerPage():
    form = RegisterForm()
    if form.validate_on_submit():
        user = sqlsession.query(User).filter(User.UName==form.name.data).first()
        if user is None:
            #新建用户类
            user = User(UName=form.name.data, 
                    UPassword = form.password.data, 
                    UIntro='new user signed up')
            sqlsession.add(user)
            sqlsession.commit()
            flash('注册成功！请返回登录界面登录。')
        else:
            flash('用户已存在！')
    return render_template('register.html', form = form)
#用户界面
@app.route('/user/<name>')
#it gave a var name to func
@login_required
def userPage(name):
    #Here we test abort() for user validation checking
    #if name != 'CO2NoTear':
    #   #Noticing that this would throw ERROR expection and quit
    #   #just like normally 404 NOT FOUND
    #   abort(404)
    return render_template('usrpage.html', name = name)

#自定义404界面
@app.errorhandler(404)
def pageNotFound(e):
    #Here we test url_for func to generate dynamic url for Links
    #for html models.
    return render_template('404.html', url_for_CO2 = 'http://123.249.78.113:2333' + url_for('userPage', name='CO2NoTear', _external=False)), 404
    # WARNING!!!!!!
    # if you set _external as True, url_for func will give you
    # a absolute url, HOWEVER, its IP address is 0.0.0.0, namely
    # unable to use simply in the links.


#测试跳转界面
@app.route('/jump')
def jumpToIndex():
    return redirect('http://www.baidu.com')


if __name__ == '__main__':
    app.run(debug=True)
