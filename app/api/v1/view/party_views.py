from flask import Flask,request
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


        response = {
            'message':'input on all fields is required',
            'status':417
            }
        if self.dt.valid (data['name']) ==  False:
            return response
        if self.dt.valid (data['abbreviations']) ==  False:
            return response
        if self.dt.valid (data['chairperson']) ==  False:
            return response
        if self.dt.valid (data['members']) == False:
            return response
        if self.dt.valid (data['address']) == False:
            return response
        if self.dt.valid (data['logoUrl']) == False:
            return response
        self.dt.save(party)
        return{
                'Message': 'Successfully saved',
                'status':201,
                'data':party
             }
    
    def get(self):
        if self.dt.all() == []:    
            return {
                    'Message':'Parties not found',
                    'status':400,
                }
        else:
            return{
            'Message':'Returned successfully',
            'status':200,
            'data':self.dt.all()
            }


class Party(Resource):
    #class and methods creates endpoints that apply to a single party only
    def __init__(self):
         self.dt = Partybase()
       
    def get(self, party_id):
        party = self.dt.find(party_id)
        if not party:
            return {
                'Message':'Party not found',
                'status':404
            }
        return{
            'Message':'The party has been returned successfully',
            'status':200,
            'data':party
        }


    def delete(self, party_id):
        party = self.dt.find(party_id)
        if party:
            self.dt.remove(party_id)
            return {
                'Message':'Party successfully deleted',
                'status':204,
            }
        return{
            'Message':'Party not found',
            'status':404,
        }

    def patch(self,party_id):
        data = parser.parse_args
        party = self.dt.find(party_id)
        if party:
            party.update(data)
            return{
                'Message':'party successfully updated',
                'status':200,
                'data':party
            }
        return{
            'Message':'Party not found',
            'status':404,
            }
 