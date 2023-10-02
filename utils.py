import re

def messageType(message):
    print(message)
    if re.search("#categories*", message.lower()):
        return 'categories'
    else:
        return 'unknown'
    
def parseCategories(message):
    return message.split("\n")[1:]