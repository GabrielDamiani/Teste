from ..DatabaseConnection import db

class LogType(db.Model):
    __tablename__ = 'LogType'
    Id = db.Column(db.SmallInteger, primary_key=True)
    TypeName = db.Column(db.String(100), nullable=False)
