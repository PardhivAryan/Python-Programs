class EmptyFileError(Exception):
    def __init__(self, message = "File is empty"):
        self.__message = message # This line stores the message in an attribute of your custom exception class,
        super().__init__(self.__message) # It allows Python to show the error message when the exception is raised
        
    def get_message(self): # We are accessing private variable(self.__message) using get() method
        return self.__message
 
# Reading a file   
def read_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        if not content.strip():
            raise EmptyFileError() # Raise custom exception if file is empty
        print("File Opened")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} doesn't exist")
    except EmptyFileError as efe:
        print(f"Error: {efe}")
    except Exception as e:
        print(f"An unexpected error : {e}")
    finally:
        try:
            file.close()
            print(f"The file is closed Successfully")
        except:
            print(f"The file was never opened so it can't be closed.")

# Usage Example         
filename = input("Enter file name : ")
read_file(filename)
        
        
        
        
