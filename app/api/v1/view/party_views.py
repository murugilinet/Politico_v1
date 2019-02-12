from flask import Flask,request,make_response,jsonify
from flask_restful import Resource,reqparse
from app.api.v1.model.models import Model


partydb = []

parser = reqparse.RequestParser()
parser.add_argument(
    "name",type = str,required = True,help = "Name field is required"
)
parser.add_argument(
    "abbreviations",type = str,required =True,help = "abbreviation field required"
)
parser.add_argument(
    "chairperson",type = str,required =True,help = "chairperson field required"
)

parser.add_argument(
    "members",type = str,required =True,help = "members field required"
    )
parser.add_argument(
    "address",type = str,required =True,help = "address field required"
    )
parser.add_argument(
    "logoUrl",type = str,required =True,help = "logo field required"
    )


class Partybase(Model):
    #initiates class that stores party


    def __init__(self):
        #initialises the class that contains reference to party
        super().__init__(partydb)


class Parties(Resource):
    #This class and methods creates endpoints that work on several offices
    def __init__(self):
        self.dt = Partybase()

    def post(self):
        data = parser.parse_args()

        party = {
            'name': data['name'],
            'abbreviations':data['abbreviations'],
            'chairperson':data['chairperson'],
            'members':data['members'],
            'address':data['address'],
            'logoUrl':data['logoUrl'],
               } 


        response = make_response(jsonify({
            'Message':'Correct input required',
            }),400)
        if self.dt.party_exists(data['name']) ==  False:
            return make_response(jsonify({
                'Message': 'Party already exists'
             }),401)
        if self.dt.valid_type(data['name']) ==  False:
            return response
        if self.dt.valid_type(data['abbreviations']) ==  False:
            return response
        if self.dt.valid_type(data['chairperson']) ==  False:
            return response
        if self.dt.valid_digits(data['members']) == False:
            return response
        if self.dt.valid(data['address']) == False:
            return response
        if self.dt.valid_type(data['logoUrl']) == False:
            return response
        elif self.dt.length_long(data['name']) == False:
            return make_response(jsonify({
                'Message':'Name field too short'
            }),411)
        elif self.dt.length_short(data['abbreviations']) ==False:
            return make_response(jsonify({
                'Message':'abbreviations too long'
             }),411)
        self.dt.save(party)
        return make_response(jsonify({
                'Message': 'Successfully saved',
                'data':party
             }),201)
    
    def get(self):
        if self.dt.all() == []:    
            return make_response(jsonify({
                    'Message':'Successfully returned',
                    'data': self.dt.all
                }),404)
        else:
            return make_response(jsonify({
            'Message':'Returned successfully',
            'data':self.dt.all()
            }),200)


class Party(Resource):
    #class and methods creates endpoints that apply to a single party only
    def __init__(self):
         self.dt = Partybase()
       
    def get(self, party_id):
        party = self.dt.find(party_id)
        if not party:
            return make_response(jsonify({
                'Message':'Party not found'
            }),404)
        return make_response(jsonify({
            'Message':'The party has been returned successfully',
            'data':party
        }),200)

    def delete(self, party_id):
        party = self.dt.find(party_id)
        if party:
            self.dt.remove(party_id)
            return make_response(jsonify({
                'Message':'Party successfully deleted',
                'data':party
            }),200)
        return make_response(jsonify({
            'Message':'Party not found',
           }),404)

    def patch(self,party_id):
        data = parser.parse_args
        party = self.dt.find(party_id)
        if party:
              party.update(data)
              return make_response(jsonify({
                'Message':'party successfully updated',
                'data':party
            }),200)
        return make_response(jsonify({
            'Message':'Party not found'
            }),404)
 