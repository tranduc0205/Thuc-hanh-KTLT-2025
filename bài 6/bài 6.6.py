print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

class StringManipulator:
    def __init__(self):
        self.user_string = ""  

    def get_String(self):
        self.user_string = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())
manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()