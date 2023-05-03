import json
import os
def checkForValueJSON(name):
    file_size = os.path.getsize('json/main.json')
    if file_size > 0:
        print('file is here [func print]')
        with open('json/main.json', 'r') as f:
            data = json.load(f)

        if name in data:
            print('key exists')

        else: 
            print('key does not exist')

    else:
        print('file is not here')

def main():
    #data = {
        #"address": "the",
        #"other": 120,
        #"why": "new david"
    #}
    #with open('json/main.json', 'w') as f:
        #json.dump(data, f)

    #f.close
    checkForValueJSON('david')
    file_size = os.path.getsize('json/main.json')
    print(file_size)
    if file_size > 0:
        print("file is here")
        with open('json/main.json', 'r') as f:
            data = json.load(f)
            
        
        if 'name' in data:
            print('key exists')
        else:

            print('key did not exist')
            data['name'] = "the"
        #data.append(new_data)

        with open('json/main.json', 'w') as d:
            json.dump(data, d)

           


    else: 
        print("file is not here")
        data = { 
            "test": "test"
        }
        with open('json/main.json', 'w') as f:
            json.dump(data, f)

        f.close()
        

    
    


main()