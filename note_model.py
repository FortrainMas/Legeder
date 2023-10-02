class User():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.categories = ['unsorted']
    def addCategory(self, category):
        self.categories.append(category)



class Note():
    def __init__(self, content, name='unnamed', type='unsorted'):
        self.name = name
        self.content = content
        self.type = type