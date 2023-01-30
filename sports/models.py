from . import db 

class Sports(db.Model):
    idsport = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)

    def to_json(self):
        return{
            'idsport' : self.idsport,
            'name' : self.name,
            'description' : self.description
        }