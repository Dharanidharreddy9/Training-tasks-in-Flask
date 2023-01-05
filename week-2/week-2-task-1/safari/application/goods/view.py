from flask import jsonify, request, Blueprint,json
from flask_restplus import Api, Resource, fields
from application.goods.control import get_validator_control,\
                                      get_singleid_control,\
                                      post_validator_control,\
                                      put_validator_control,\
                                      del_validator_control
                                        

#creating the documentation
train_application = Blueprint('trained_app', __name__)
trained_app = Api(train_application)

# Giving a model for posting and modifying the data
app_model = trained_app.model('demo',{
    'name':fields.String('Enter Name'),
    'email':fields.String('Enter Email'),
    'password':fields.String('Enter Password')
})


# print all the records and give proper resonce to the user 
@trained_app.route('/getdata')
class Get_train_data(Resource):
    def get(self):        
        """Fetch all the data """
        return get_validator_control()


# print a single record using id 
@trained_app.route('/getsingledata/<int:id>')
class Get_single_data(Resource):
    def get(self,id):
        """Fetch a single record"""
        return get_singleid_control(id)


# Inserting the new data and show response to the suer
@trained_app.route('/postdata')
class Post_train_data(Resource):
    @trained_app.expect(app_model)
    def post(self):
        """Insert the data"""
        if request.method == 'POST':
             return post_validator_control()


# Modifies the data 
@trained_app.route('/put/<int:id>')
class Put_train_data(Resource):
    @trained_app.expect(app_model)
    def put(self,id):
        """Update the data using id"""
        return put_validator_control(id)


# Deleting the single user using id
@trained_app.route('/delete/<int:id>')
class Delete_train_data(Resource):
    def delete(self,id):
         """Delete the record using id"""
         return del_validator_control(id)








