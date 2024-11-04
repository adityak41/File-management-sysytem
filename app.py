import os
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File Name {filename}: Created successfully!")

    except FileExistsError:
        print(F'file name {filename}: already exists!')

    except Exception as E:
        print('An error occurred!') 

def view_all_files():
    files = os.listdir()
    if not files:
        print('No file found!')
    else:
        print('file in directory')

    for file in files:
        print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')

    except FileNotFoundError:
            print('file not found')

    except Exception as e:
            print('An error occurred!')

def read_file(filename):
    try:
        with open('Sample.txt', 'r')as f:
                Content = f.read()
                print(f"Content of '{filename}':\n{Content}")

    except FileNotFoundError:
            print(f"{filename} doesn't exist!")

    except Exception as e:
            print('An error occurred!')

def edit_file(filename):
    try:
        with open('Sample.txt', 'a') as f:
            Content = input('Enter data to add =')
            f.write(Content + "\n")
            print('Content added to {filename} successfully!')

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print('An error occurred!')

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exit')
        break

    choice = input('Enter your choice(1-6)=')
    if choice == '1':
        filename =input('Enter your file name to create =')
        create_file(filename)

    elif choice == '2':
        view_all_files()

    elif choice == '3':
        filename = input('Enter the name of the file you want to delete')
        delete_file(filename)

    elif choice == '4':
        filename = input('Enter filename to read=')
        read_file(filename) 

    elif choice == '5':
        filename = input('Enter filename to edit=')
        edit_file(filename)

    elif choice == '6': 
        print('closing the app....')
    
            
    else:
        print('In-valid syntax')
            

if __name__=="__main__":
    main()
    
    
              
