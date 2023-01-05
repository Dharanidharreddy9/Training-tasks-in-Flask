# from flask import request, jsonify

from application.goods.model import get_traindata,\
                                    get_recordby_id,\
                                    post_train_model,\
                                    update_traindata,\
                                    delete_traindata                                    


def get_validator_control():    
    return get_traindata()


def get_singleid_control(id):
    return get_recordby_id(id)


def post_validator_control():
        
    return post_train_model()


def put_validator_control(id):
    return update_traindata(id)    



def del_validator_control(id):
    return delete_traindata(id)    
