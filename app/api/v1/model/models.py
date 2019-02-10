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
    
    def update(self, id):
        item = self.find(id)
        if item:
            data = self.items.update(item)
            response = self.items.save(data) 
            return response
    
    def valid(self,data):
        if data.isspace() or data == "":
            return False
    def length(self,data):
        if len(data) < 5:
            return False
            