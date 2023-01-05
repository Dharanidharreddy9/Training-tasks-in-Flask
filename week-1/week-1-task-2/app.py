from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
# import logging

# creating the record file to store all the errors and commands
# logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)

# Connecting the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:root@localhost:5432/fog'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate()
ma = Marshmallow(app)

# Creating a table with the students name
class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    city = db.Column(db.String(150))
    address = db.Column(db.String(150))
    pin = db.Column(db.Integer)

    def __init__(self,name,city,address,pin):
        self.name =name
        self.city = city
        self.address = address
        self.pin = pin


# Creating a schema
class studentsSchema(ma.Schema):
    class Meta:
        model = students.name,students.city,students.address,students.pin


# we are inserting the data into database and get the data
@app.route("/data/", methods=['POST', 'GET'])
def data():
    # Inserting the data into the table
    if request.method == 'POST':
        name = request.json.get('name','')
        city = request.json.get('city','')
        address =request.json.get('address','')
        pin =request.json.get('pin','')

        college = students(name,city,address,pin)

        db.session.add(college)
        db.session.commit()
        return jsonify({'Status':'Record added succesfully'}),201

    if request.method =='GET':    
        try:
            # Get all the data from database
            if request.method == 'GET':
                all_data = students.query.all()
                return jsonify(studentsSchema(many=True).dumps(all_data)),200
        except:
            print("somthing went Wrong")


# performing on individual records in database to get the data delete the data and modifying the data
@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):
    #GET a specific data by id
    if request.method == 'GET':
        college = students.query.get(id)
        print(college)
        return jsonify(studentsSchema.dump(college)),200
    else:
        return "somthing went Wrong"


    # DELETE the in the table
    if request.method =='DELETE':
        delData = students.query.get(id)
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status':'one id'+id+' is deleted'}),200
    else:
        return "somthing went Wrong"


    # Update the data in table
    if request.method == 'PUT':
         get_req = request.get_json()
         newName = get_req['name']
         newCity = get_req['city']
         newAddress = get_req['address']
         newPin = get_req['pin']

         editData = students.query.filter_by(id=id).first()

         editData.name = newName
         editData.city = newCity
         editData.address = newAddress
         editData.pin =  newPin
         db.session.commit()
         return jsonify({'status':'Data is Updated successfully'}),201
    else:
        return "somthing went Wrong"


if __name__ == '__main__':
    app.run(debug=True)
