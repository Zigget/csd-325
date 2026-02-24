'''
Samuel Sidzyik
CSD-325
Module8.2
2/23/26

This program works on a JSON file'''

import json
from os import path

def main():
    'Get JSON Data'
    filename = 'C:/Users/ssidz/Git/csd-325/module-8/Student.json'
    listObj = []

    if path.isfile(filename) is False:
        raise Exception("File not found")
    
    with open(filename) as fp:
        listObj = json.load(fp)

    'Print JSON data'
    printJSON(listObj)
    print("This is the original JSON")

    'Update JSON data'
    listObj = addUser(listObj)
    printJSON(listObj)
    print("This is the updated JSON data")
    
    'Update JSON file'
    with open(filename, 'w') as fp:
        updateJSON(fp, listObj)
    print("the JSON file has been updated")

    

def updateJSON(fp, listObj):
    json.dump(listObj, fp)  

def addUser(listObj):
    'I spent an hour screwing this up so many different ways, lol'
    fName = input(f"\nEnter first name > ").title()
    lName = input("Enter last name > ").title()
    sID = input("Enter student ID > ")
    eMail = input("Enter Email > ").lower()
    student = {f'F_Name': fName, 'L_Name': lName,
                f'Student_ID': sID, 'Email': eMail}
    listObj.append(student)
    return listObj

def printJSON(listObj):
    ''
    for lists in listObj:
        print(f"i. {lists['F_Name']}, {lists['L_Name']}"
              f": ID = {lists['Student_ID']}, Email = {lists['Email']}")


if __name__ == "__main__":
    main()