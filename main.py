import json 
import os 

def main():

    #data = "the"
    #print(data[0:3])
    #data_array = [[0 for j in range(2)] for i in range(4)]
    #data_array[1][0] = "true"
    #for row in data_array:
        #print(row)

    ## entry for data to learn from 
    sentence = input("enter the sentence: ")
    spaceCount = 0
    firstSpace = 0
    for foo in range(len(sentence)):
        if sentence[foo] == " ":
            spaceCount += 1
            

    cont = True
    whileCounter = 0
    while cont:
        whileCounter += 1
        if spaceCount > 1:
            if sentence[whileCounter] == " ":
                firstSpace = whileCounter
                cont = False

        else:
            print(" do something")
            cont = False




    print(f'{firstSpace} firstspace')
    print(f'{spaceCount} space count')

    data_multi_array = [[0 for j in range(2)] for i in range(spaceCount + 1)]

    #nullCount = 0
    counter = 0
    for j in range(len(data_multi_array)):
        if data_multi_array[j][j] == 0:
            print("empty")
            counter += 1


    firstSpaceStr = str(firstSpace)
    data_multi_array[counter - 1][1] = '0' + firstSpaceStr
    print(data_multi_array[counter - 1][1])
    print("test")
            
    

    print(f'{counter} counter')

    #for row in data_multi_array:
    #    print(row)
        
    print("----")

    for row in data_multi_array:
        print(row)

    file_size = os.path.getsize('json/main.json')


    print(f'{file_size} file size')

    if file_size > 0:
        print("file is above 0 bytes")
        with open('json/main.json') as f:
            data = json.load(f)
        
        start = int(data_multi_array[counter - 1][1][0])
        end = int(data_multi_array[counter - 1][1][1])
        new_data = {
            "the": sentence[start:end]
        }
        if 'the' in data:
            print(data['the'])

        with open('json/main.json', 'w') as f:
            json.dump(new_data, f)

    else:
        print("ERROR file is empty")
        




##
main()