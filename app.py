from tkinter import *
from tkinter.messagebox import showinfo

def computeMortgage():
    global loanAmountEntry
    global interestRateEntry
    global loanTermsEntry
    global computedMortgageEntry
    
    loanAmount = 0
    interestRate = 0
    loanTerms = 0
    
    try:
        loanAmount = float(loanAmountEntry.get())
        interestRate = float(interestRateEntry.get())
        loanTerms = float(loanTermsEntry.get())
        
        computedMortgageEntry.insert(0,string(loanAmount + interestRate + loanTerms))
    except:
        showinfo(message = "Please enter valid numbers")    
    

root = Tk()

loanAmountLabel = Label(root, padx=10, text='Loan Amount')
loanAmountLabel.grid(row=0, column=0)

loanAmountEntry = Entry(root)
loanAmountEntry.grid(row=0, column=1)

interestRateLabel = Label(root, padx=10, text='Interest Rate')
interestRateLabel.grid(row=1, column=0)

interestRateEntry = Entry(root)
interestRateEntry.grid(row=1, column=1)

loanTermsLabel = Label(root, padx=10, text='Loan Terms')
loanTermsLabel.grid(row=2, column=0)

loanTermsEntry = Entry(root)
loanTermsEntry.grid(row=2, column=1)

computeButton = Button(root, text = 'Compute mortgage', command = computeMortgage)
computeButton.grid(row = 3, column = 0)

computedMortgageEntry = Entry(root)
computedMortgageEntry.grid(row=3, column=1)

root.mainloop()

