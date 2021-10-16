if __name__ == "__main__":
    Bank = Register()
    print("Welcome")
    print("1. Login")
    print("2. Create a new Account ")
    user = int(input("Make Decision"))
    
    
    if user == 1:
        print("Logging in")
        name = input("Please Enter your Name")
        ph = str(input("Please Enter a phone number"))
        password = input("Enter a password")
        Register.login(name, ph, password)
        
        while True:
            
            if Register.login:
                
                print("1. Add amount")
                print("2. Check Balance")
                print("3. Edit Profile")
                print("Logout")
                login_user = int(input())
                
                
                if login_user == 1:
                    print("Balance = ", Register.cash)
                    amount = int(input("Enter the amount you want to deposit"))
                    Register.add_amount(amount)
                    print("\n1. Go Back to Main Menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break
                if login_user == 2:
                    print("Your Balnace is", Register.cash)
                    
                    print("\n1. Go Back to Main Menu")
                    print("2. Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break
                    
                    
    if user == 2:
        print("creating a new Account")
        name = input("Please Enter your Name")
        ph = str(input("Please Enter a phone number"))
        password = input("Enter a password")
        Register.register(name, ph, password)