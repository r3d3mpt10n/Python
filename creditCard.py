def creditCard(balance, monthlyPaymentRate, annualInterestRate):
    i = 1
    total = 0
    while i <= 12:
        payment = balance*monthlyPaymentRate
        unpaidBalance = balance - payment
        balance = (unpaidBalance + (annualInterestRate/12.0) * unpaidBalance)
        ## print("Month " + str(i) + " Balance = " + str(b) )
        print("Month: %d \nMinimum monthly payment = %.2f \nRemaining Balance = %.2f \n " % (i, payment, balance))
        total += payment
        i += 1
    print("Total paid: %.2f" % (total))
    print("Remaining balance: %.2f" % (balance))

def main():
    balance = 5000
    unpaidBalance = 5000
    annualInterestRate = 0.18
    monthlyPaymentRate = 0.02
    creditCard(balance, monthlyPaymentRate, annualInterestRate)

main()





