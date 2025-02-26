e = ""  
p = ""  

def su():
    global e, p  
    e = input("Enter email: ")
    p = input("Enter password: ")
    print("Signup successful!")

def si():
    if input("Enter email: ") == e and input("Enter password: ") == p:
        print("Login successful!")
    else:
        print("Invalid email or password.")

def main():
    while True:
        c = input("\n1. Sign Up\n2. Sign In\n3. Exit\nEnter choice: ")
        if c == '1':
            su()
        elif c == '2':
            si()
        elif c == '3':
            print("Goodbye!")
            break
        else:
            print("Enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
