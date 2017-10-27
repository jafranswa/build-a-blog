from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
#database conection string = 'mysqul+pymysql://user:password@location:port_number/db_name'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(139))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        task_name = request.form['new_post']
        new_task = Blog(task_name)
        db.session.add(new_task)
        db.session.commit()

    entry_title = Blog.query.all()
    #entry = Blog.query.all()
    return render_template('display.html',title="Why am I always crying!", 
        entry_titles = entry_title)


@app.route('/post', methods=['POST','GET'])
def add_post():


    if request.method == 'POST':    
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = Blog(post_title, post_content)

        if post_title == '':
            flash('Please title your troubles')
            return render_template('post.html',title='wipe away your tears', post_content=post_content, post_title=post_title)
        elif post_content == '':
            flash('Its ok tell me whats on your mind')
            return render_template('post.html',title='wipe away your tears', post_content=post_content, post_title=post_title)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
        #return render_template('display.html',title="Why am I always crying!", 
        #post_title = entry_title)
    #task_id = int(request.form['task-id'])
    #task = Task.query.get(task_id)
    #task.completed = True
    #db.session.add(task)
    #db.session.commit()

    return render_template('post.html',title='wipe away your tears')

@app.route('/view_post', methods=['POST','GET'])
def view_post():


    #entry_title = Blog.query.all()
    key = request.args.get('id')
    post_title = Blog.query.get(key).title
    body = Blog.query.get(key).body
        
    return render_template('view_post.html',title='wipe away your tears', post_title = post_title, body = body)
        
    #task_id = int(request.form['task-id'])
    #task = Task.query.get(task_id)
    #task.completed = True
    #db.session.add(task)
    #db.session.commit()



if __name__ == '__main__':
    app.run()


#python
#from main import db,Task
#db #will show the SQLAlchemy engine=
#db.create_all() #scans the classes and creates the associated tables in
                    #the database
#new_task = Task('finish ORM lesson 2')
#db.session.add(new_task)
#another_task = Task('post lesson video')
#db.session.add(another_task)
#db.session.commit() #sessions will not be added until you commit()
#Task.query.all() #select all query objects from the database
#tasks = Task.query.all()
#tasks #show objects hex number
#tasks[0].name #will display 'finish ORM lesson 2' 

#NEW COLMN WHEN CLASS CHANGES
#python
#from main import db,Task
#db.drop_all() #will destory all tables in database
#db.create_all() #will create new structure with new classes
                    #you would not want to do this if you wanted to
                    #keep all the data #flask-migrate docs can show you how to use this 

#FOR USER CLASS
#python
#import db,User
#db.create_all() #create the table structure in the database
#new_user = User('chris@launchcode.org', 'cheese')
#db.session.add(new_user)
#db.session.commit()