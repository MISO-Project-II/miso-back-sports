from . import db 

class Sports(db.Model):
    idsports = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)

    def to_json(self):
        return{
            'idsports' : self.idsports,
            'name' : self.name,
            'description' : self.description
        }