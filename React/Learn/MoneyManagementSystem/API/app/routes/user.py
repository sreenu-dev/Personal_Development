from flask import Blueprint, jsonify, request
import uuid;
from ..models import User

user_bp=Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/<int:user_id>',methods=['GET'])
def getUserWithId(user_id):
    user_data={
        'id':user_id,
        'name':'John Doe',
        'email':'john.doe@example.com'
    }
    return jsonify(user_data)

@user_bp.route('/adduser',methods=['POST'])
def add_user():
    data=request.get_json()

    new_user={
        'id':str(uuid.uuid4()),
        'name':data.name,
        'email':data.email
    }

    return 'User added Successfully', 200

@user_bp.route('/users',methods=['GET'])
def getAllUsers():
    users=User.query.all()
    userlist=[]
    for user in users:
        # tuser={
        #     'userid':user.userid,
        #     'name':user.name,
        #     'email':user.email
        # }
        userlist.append({
            'userid':user.userid,
            'name':user.name,
            'email':user.email
        })
        # print(user.userid)
    print(userlist)
    return jsonify(userlist)