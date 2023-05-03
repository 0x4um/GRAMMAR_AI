import json
import os


def main():
    file_size = os.path.getsize('json/main.json')
    print('main')
    sentence = input('enter a sentence: ')
    #print(len(sentence))

    #with open('json/main.json', 'r') as file:
        #data = json.load(file)

    #for y in range(len(sentence)):
        #new_data = {y: y}
        #data.append(new_data)        


    #with open('json/main.json', 'w') as file:
        #json.dump(data, file)

    for x in range(len(sentence)):
        if sentence[x] == " ":
            print('space')
        else:
            print(sentence[x])

    if file_size > 0:
        with open('json/main.json') as file:
            data = json.load(file)

        for x in range(len(sentence)):
            data[x] = sentence


        with open('json/main.json', 'w') as file:
            json.dump(data, file)


    else:
        print('file not here')
        data = {
            "Test": "Test"
        }
        with open('json/main.json', 'w') as file:
            json.dump(data, file)
            


main()