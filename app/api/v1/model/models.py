class Model():
    '''Includes functions of requests on both political parties and offices'''
    def __init__(self,items):
        self.items = items

    def all(self):
        return self.items
    
    def  save(self, data):
        data['id']=self._generate_id()
        self.items.append(data)  
    
    def _generate_id(self):
        if len(self.items):    
            return self.items[-1]['id']+1
        else:
            return 1
    
    def find(self, id):
        for item in self.items:
            if item['id'] == id:
                return item
    
    def remove(self, id):
        item = self.find(id)
        if item:
            return self.items.remove(item)
    
    def valid(self,data):
        if data.isalnum:
            return True
        return False
    
    def valid_type(self,data):
        if data.isalpha():
            return True
        return False
    
    def valid_digits(self,data):
        if data.isdigit():
            return True
        return False
        
    def length_long(self,data):
        if len(data) < 5:
            return False
    def length_short(self,data):
        if len(data) > 4:
            return False
    def valid_officetype(self,data):
        if data['office_type'] == 'state' or  data['office_type'] == 'federal' or data['office_type'] =='legislature' or data['office_type'] =='local-community':
            return True
        return False
    def party_exists(self, data):
        for item in self.items:    
            if data == item['name']:
                return False