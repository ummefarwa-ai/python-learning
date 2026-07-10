from pathlib import Path
import os
PROGRAM_FILE = Path(__file__).resolve()

def is_protected_file(p):
    try:
        return p.resolve() == PROGRAM_FILE
    except Exception:
        return False


def readFileandFolder():
    p= Path(".")
    items=list(p.rglob("*"))
    print("\nAvailable Files/Folders:")
    for i,item in enumerate(items):
        print(f"{i+1} :  {item}")
        
def creatfile():
    try:
        readFileandFolder()
        filename = input("Enter the name of new file : ").strip()
        p = Path(filename)
        if p.name == PROGRAM_FILE.name:
            print("❌ Reserved filename.")
            return
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Enter the data in this new file :  ")
                fs.write(data)
            
            print("✅FILE CREATED SUCCESSFULLY!")
        else:
            print("❌File already existed!")
    except Exception as err:
        print(f"An error occured as {err}")   
        
def readfile():
    try:
        readFileandFolder()
        filename = input("Enter the name of file to read : ").strip()
        p = Path(filename)
        if is_protected_file(p):
            print("❌ Access denied! Program file is protected.")
            return
        if p.exists() and p.is_file():
            with open(p , "r") as fs:
                data = fs.read()
                print("\n----- FILE CONTENT -----")
                print(data)
            print("✅ FILE READ SUCCESSFULLY")
        else:
            print("❌File not existed!")
        
    except Exception as err:
        print(f"An error occured as {err}")
    

def updatefile():
    try:
        readFileandFolder()
        filename = input("Enter the name of file to update : ").strip()
        p = Path(filename)
        if is_protected_file(p):
             print("❌ Access denied! Program file is protected.")
             return
        if p.exists() and p.is_file():
            print("Press 1 for changing file name. ")
            print("Press 2 for overwriting a file. ")
            print("Press 3 for entering new data to file. ")
            num = int(input("Select a number : "))
            
            if num==1:  
                    new_name = input("Enter new name : ").strip()
                    p2 = Path(new_name)
                    if p2.name == PROGRAM_FILE.name:
                        print("❌ Reserved filename.")
                        return
                    if p2.exists():
                        print("❌ A file with this name already exists.")
                    else:
                        p.rename(p2)
                        print("✅Name Changed Successfully!")
                    
                    readFileandFolder()
                
            elif num ==2:
               
                data = input("What you want to write? (△old content will be deleted!) : ")
                with open(p, "w") as fs:
                    fs.write(data)
                print("✅ File updated successfully!")
                        
                
            elif num==3:
                data = input("What you want to write? : ")
                with open(p,"a") as fs:
                    fs.write(" " + data)
                print("✅ Data appended successfully!") 
            else: 
                print("❌ Invalid option!")
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An error occured as {err}")
    
def deletefile():
    try:
        readFileandFolder()
        Rfile = input("Enter the name of file to delete : ").strip()
        p = Path(Rfile)
        if is_protected_file(p):
            print("❌ Access denied! Program file is protected.")
            return
     
        if p.exists() and p.is_file():
            confirm = input("Are you sure? (y/n): ").lower()

            if confirm != "y":
                print("Deletion cancelled.")
                return
            else:
                 os.remove(p)
                 print("File deleted Successfully!")
        else:
            print("No such file existed")
        
    except Exception as err:
        print(f"An error occured as {err}")
        
        
        
#  ===========================
# Main Program Loop
# ===========================   



while True:
    print("\n===== FILE MANAGER =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Update File")
    print("4. Delete File")
    print("5. Exit")
    try: 
        num = int(input("Enter your choice: ")) 
        if num == 1: 
            creatfile() 
        elif num == 2: 
            readfile() 
        elif num == 3: 
            updatefile() 
        elif num == 4: 
            deletefile() 
        elif num == 5: 
            print("👋 Thank you for using File Manager!") 
            break 
        else: 
            print("❌ Please enter a number between 1 and 5.") 
    except ValueError: 
        print("❌ Please enter a valid number.")

    
