import  json
import os.path
from pathlib import Path
import Directerylist as dirs
print("*****************Freshworks  Task ***********************")
print("Choose Your Option")
print("1: Create file")
print("2: Read Data")
print("3: Delete Data")
option =int(input("Enter Your choice:\n "))


def DefaultFileCreate():
    userfilename=str(input("Enter Your File name"))
    keyname = str(input("Enter Your key"))
    valuename = str(input("Enter Your value"))
    dictionarydata = {keyname: valuename}
    filenames="{}.json".format(userfilename)
    if(True):
        with open(filenames, 'w') as json_files:
            filsize(filenames)
            json.dump(dictionarydata, json_files)

            print("File created Successfully ...")
    else:
        print("File size Exceed the limit")



def createfile():   #  This is the Main  Method for create a file
    status= str(input("Are Create own File path ? Yes or No"))
    if(status.lower()=="yes"):
                dirshow = dirs.diskdir()
                checkpath=[]
                print("Choose Your Directory")
                for i in range(len(dirshow)):
                    checkpath.append(dirshow[i][0])
                    print(dirshow[i][0])

                dirpath=str(input("Enter Your Directory name"))
                print("dir",checkpath)
                if(dirpath.upper() in checkpath):
                    print("Directory matched")
                    userfilename= str(input("Enter Your file name"))
                    keyname=str(input("Enter Your key"))
                    valuename=str(input("Enter Your value"))
                    dictionarydata= {keyname:valuename}
                    my_dir = '{}:'.format(dirpath.upper())
                    file_name='/{}.json'.format(userfilename)
                    fname = os.path.join(my_dir, file_name)
                    with open(fname,'w') as json_file:
                        filsize(fname)
                        json.dump(dictionarydata,json_file)
                        print("File created")
                else:
                    print("Directory not mathched")
    elif(status.lower()=="no"):
       DefaultFileCreate()    # Here create file without other directory....
    else:
        print("Sorry for inconveniant")


def readfilestootherdevice():
    dirshow = dirs.diskdir()
    checkpath = []
    print("Choose Your Directory")
    for i in range(len(dirshow)):
        checkpath.append(dirshow[i][0])
        print(dirshow[i][0])

    dirpath = str(input("Enter Your Directory name"))
    #print(checkpath)
    if (dirpath.upper() in checkpath):
        my_dir = '{}:'.format(dirpath.upper())
        userfilename=str(input("Enter Your existing File Name."))
        file_name = '/{}.json'.format(userfilename)
        searchkey=str(input("Enter Key which are want to search"))

        fname = os.path.join(my_dir, file_name)
        try:

            with open(fname,'r') as json_fils:
                jsondata= json.load(json_fils)
                if(searchkey in jsondata):
                    print(jsondata)
                else:
                    print(" data Not found")
        except:
            print("File not found in this Directory !!")

    else:
        print("Directory not found")


def defaultreaddata():
    userfilename=str(input("Enter your file name "))
    filedirs="{}.json".format(userfilename)
    keyname = str(input("Enter Your key Which are want to Search "))
    try:
        with open(filedirs, 'r') as json_files:
            jsondataread= json.load(json_files)
            if keyname in jsondataread:
                print(jsondataread)
            else:
                print("Oh no !. Key Not found..")

    except:
        print("File Not Found")

    pass




def readdata():
    options= str(input("Have your files in other drives ? yes or  No"))
    if(options.lower()=="yes"):
        readfilestootherdevice()
    elif(options.lower()=="no"):
       defaultreaddata()
    else:
        print("Your Enter Wrong Key.. Try Again..")


def deletefileFromotherdrive():
    dirshow = dirs.diskdir()
    checkpath = []
    print("Choose Your Directory")
    for i in range(len(dirshow)):
        checkpath.append(dirshow[i][0])
        print(dirshow[i][0])

    dirpath = str(input("Choose Your Directory name"))
    if (dirpath.upper() in checkpath):
        my_dir = '{}:'.format(dirpath.upper())
        userfilename=str(input("Enter Your File name Which  You saved ."))
        file_name = '/{}.json'.format(userfilename)
        deltekey=str(input("Enter Key which are want to Delete"))
        fname = os.path.join(my_dir, file_name)
        try:
            with open(fname,'r') as readjsonfile:
                jsonreaddata= json.load(readjsonfile)
                print(jsonreaddata)
                if(deltekey in jsonreaddata):
                    keyname =""
                    valuename =""
                    dictionarydata = {keyname: valuename}
                    with open(fname, 'w') as json_files:
                        json.dump(dictionarydata, json_files)
                        print("Data  Deleted Successfully ...")

                else:
                    print("Your Entered Key Not found")
        except:
            print("File Not Found ! Enter  Right file name..")
    else:
        print("Drive Not Found...Try Again!!")


def defaultdeletedata():
    userfilename = str(input("Enter your file name "))
    filedirs = "{}.json".format(userfilename)
    keyname = str(input("Enter Your key Which you are want to  Delete "))
    try:
        with open(filedirs, 'r') as json_files:
            jsondataread = json.load(json_files)
            if keyname in jsondataread:
                print(jsondataread)
                keyname = ""
                valuename = ""
                dictionarydata = {keyname: valuename}
                try:
                    with open(filedirs, 'w') as json_files:
                        json.dump(dictionarydata, json_files)
                        print("Data  Deleted Successfully ...")
                except:
                    print("File Not Found ,Something Wrong...!")
            else:
                print("Oh no !. Key Not found..")

    except:
        print("File Not Found")


def deletedata():
    options = str(input("Have your files in other drives ? yes or  No"))
    if (options.lower() == "yes"):
        deletefileFromotherdrive()
    if (options.lower() == "no"):
        defaultdeletedata()
    else:
        pass



def filsize(dirs):  # this function are use for the check the size of the file

    dirsize= os.path.getsize(dirs)
    # print("File size is {}".format(dirsize))
    # print("Size convert into Gb")
    # print( str(round(dirsize / (1024 * 1024 * 1024), 3)))
    if(dirsize>1.0):
        return  False
    else:
        return  True


if(option==1):
    createfile()
elif(option==2):
    readdata()
elif(option==3):
    deletedata()
else:
    print("Please Enter Valid key")
