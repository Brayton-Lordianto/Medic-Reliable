from auth_util import *

def printAllRecords():
    print(list(get_db().find({})))
    
def deleteAllRecords():
    get_db().delete_many({})

def test_signup():
    status = signup('Jack', 'myPassword')
    print(f'should print true {status} and Jack and myPassword')
    printAllRecords()

def test_login():
    first, _ = login('Jack', 'none')
    print(f'should print false {first}')
    
    second, _ = login('J', 'myPassword')
    print(f'should print false {second}')
    
    third1, third2 = login('Jack', 'myPassword')
    print(f"should print true {third1} and Jack, myPassword {third2}")
    
def main():
    deleteAllRecords()
    test_signup()
    test_login()
    
main()