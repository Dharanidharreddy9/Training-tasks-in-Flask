from application import db, ma
from flask import request,jsonify


# Creating the table using the class
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50),unique = False, nullable = False)
    password = db.Column(db.String(50), nullable = False)


class UserSchema(ma.ModelSchema):
    class Meta:
        model =User


#This will print all records in the data
def get_traindata():
    try:
        trained_app = User.query.all()        
        get_alldata = UserSchema(many=True).dump(trained_app)
        if not get_alldata.data:
            return "Data is not fetching", 404
        else:    
            return get_alldata.data, 200
    except:
        return dict(Unsuccessful="somthing went wrong"), 500


# It will print the single record based on id
def get_recordby_id(id):
    try:
        single_rec = User.query.get(id)
        print(single_rec)
        user_schema = UserSchema().dump(single_rec)
        if not user_schema.data or id:
            return "Data not found", 404
        else:    
            return user_schema.data, 200
    except:
        return "server not responding" , 500


# This will insert the data into database
def post_train_model():
    try:
        user = User(name=request.json['name'],
                    email=request.json['email'],
                    password=request.json['password'])
        if not user:
            return "Data is not getting from the user", 404  
        else:              
            db.session.add(user)
            db.session.commit()
            return {'message':'Data added to the database'}, 201
    
    except:
        return dict(Unsuccessful="somthing went wrong"), 500        


# This will modify the data
def update_traindata(id):
    try:
        user = User.query.get(id)
        user.name = request.json['name']
        user.email = request.json['email']
        user.password = request.json['password']           
        db.session.commit()
        return {'message':'Data updated succesfully'}, 201
    except:
        return dict(Unsuccessful="somthing went wrong"), 500    


# This is delete the single record using id
def delete_traindata(id):
    try:
        user = User.query.get(id)
        if not user:
            return "Id is not there"
        else:    
            db.session.delete(user)
            db.session.commit()
            return {'message':'Data deleted successfully'}, 200
    except:
        return dict(Unsuccessful="somthing went wrong"), 304



