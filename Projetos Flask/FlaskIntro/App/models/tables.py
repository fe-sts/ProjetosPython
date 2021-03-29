from app import db

class User(db.Model):
    __table__name = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self): #representação
        return "<User %r" % self.username


class Post(db.Model):
    __table__name = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id) #campo de relacionamento | 

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def Follow(db.Model):
        __table__name = "follow"

        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

        user = db.relationship('User', foreign_keys=user_id)
        follower = db.relationship('User', foreign_keys=follower_id)
        
        