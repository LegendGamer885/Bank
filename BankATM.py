class ATM:
    def __init__(self,pinNumber,cardNumber):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
    
    def checkBalance(self):
        print("your balance is 50000")
    
    def cashWithdrawl(self,amount):
        NA = 50000 - amount
        print("you have withdrawn " + str(amount))
        print("your remaining balance is " + str(NA))

def main():
    pin = input("Please enter your pin : ")
    card = input("Please enter your card number: ")

    newUser = ATM(pin,card)
    print("Choose your activity- ")
    print("Press 1 for Balance Enquiry")
    print("Press 2 for Cash withdrawl")
    
    activity = int(input("Enter the activity number: "))
    if(activity == 1):
        newUser.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        newUser.cashWithdrawl(amount)
    else:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()