from sqlalchemy import false, null
from m2m import db 
registrations = db.Table('registrations', 
      db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
      db.Column('class_id', db.Integer, db.ForeignKey('class.id')))
class Student(db.Model):
     
      id = db.Column(db.Integer(), primary_key=True)
      name = db.Column(db.String(100), nullable=false)
      classes = db.relationship('Class', secondary=registrations,
                               backref = db.backref('students', lazy='dynamic'),
                               lazy='dynamic')
      
      def __repr__(self):
         return f"<Student: {self.name}, class_id: {self.classes}>"
 
class Class(db.Model):
    
     id = db.Column(db.Integer(), primary_key=True)
     name = db.Column(db.String(100), nullable=false)
     def __repr__(self):
         return f"<Student: {self.name}>"
     
     
     

    
    

