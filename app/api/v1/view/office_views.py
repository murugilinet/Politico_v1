from flask import Flask,request,make_response,jsonify
from flask_restful import Resource,reqparse
from app.api.v1.model.models import Model

Officedb = []

parser = reqparse.RequestParser()
parser.add_argument(
    "name",type = str,required = True,help = "Name field is required"
)
parser.add_argument(
    "age",type = str, required =True,help = "age field required"
)
parser.add_argument(
    "office_type",type = str, required =True,help = "type field required"
)
parser.add_argument(
    "education",type = str,required =True,help = "education field required"
)

class Officebase(Model):
    #Initiates class for storing offices
    def __init__(self):
    #Initialises the class 'Model' that contains references for offfice
        super().__init__(Officedb)


class Offices(Resource):
#This class and methods creates endpoints that work on several offices
    def __init__(self):
        self.dt = Officebase()
 
    def post(self):
        data = parser.parse_args()

        office = {
            'name': data['name'],
            'age':data['age'],
            'office_type':data['office_type'],
            'education':data['education'],
                }

        response = make_response(jsonify({
            'Message': 'Correct input required',
        }),400) 
        if self.dt.valid_type(data['name']) == False: 
            return response
        if self.dt.valid_digits(data['age']) == False: 
            return response
        if self.dt.valid_type(data['office_type']) == False:
            return response
        if self.dt.valid_type(data['education']) == False: 
            return response
        elif self.dt.length_long(data['name']) ==False:
            return make_response(jsonify({
                'Message':'Name field too short'
                 }),411)
        elif self.dt.valid_officetype(data) == False:
            return make_response(jsonify({
                'Message':'Invalid office'
                 }),422)
        else:        
            self.dt.save(office)
            return make_response(jsonify({
                'Message': 'Successfully saved',
                'Data': office
                }),201)

    def get(self):
        if self.dt.all() == []:    
            return make_response(jsonify({
                    'Message':'Successfully returned',
                    'Data':self.dt.all()
                }),200)
        else:
            return make_response(jsonify({    
                   'Message':'Returned successfully',
                   'Data':self.dt.all()
                }),200)


class Office(Resource):
    #class and its methods creates endpoints that act on a single office
    def __init__(self):
        self.dt = Officebase()

    def get(self, office_id):
        office = self.dt.find(office_id)
        if not office:
            return make_response(jsonify({
                'Message':'Office not found',
            }),404)
        return make_response(jsonify({
            'Message':'The office has been returned successfully',
            'Data':office
            }),200)

    def delete(self, office_id):
        office = self.dt.find(office_id)
        if office:
            self.dt.remove(office_id)
            return make_response(jsonify({
                'Message':'Office successfully deleted',
                'Data':office
            }),200)
        return make_response(jsonify({
            'Message':'The office not found',
           }),404)



    
