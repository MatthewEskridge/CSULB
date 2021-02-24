#M.D.E.
#Introducing variables
customer_gwu = 0
customer_bill = 0
invalid_code = False #Invalid customer Code
meter_or = False #Meter Out of Range

#Taking inputs from user + converting numbers to integers
customer_code = input("Please input the customer's code: ")
customer_bmr = int(input("Please enter the customer's beginning meter reading: "))
customer_emr = int(input("Please enter the customer's ending meter reading: "))

#Calculating gallons used by the customer
customer_gwu = (customer_emr - customer_bmr) / 10
if customer_gwu < 0:
    customer_gwu += 100000000

#Using the customer's code to calculate the appropriate water bill
if customer_code == "r" or customer_code == "R":
    customer_code = "R"
    customer_bill = 5 + (.0005 * customer_gwu)
elif customer_code == "c" or customer_code == "C":
    customer_code = "C"
    if customer_gwu <= 4000000:
        customer_bill = 1000
    elif customer_gwu > 4000000:
        customer_bill = 1000 + (.00025 * (customer_gwu - 4000000))
elif customer_code == "i" or customer_code == "I":
    customer_code = "I"
    if customer_gwu <= 4000000:
        customer_bill = 1000
    elif customer_gwu <= 10000000:
        customer_bill = 2000
    elif customer_gwu > 10000000:
        customer_bill = 2000 + (.00025 * (customer_gwu - 10000000))
else: #Error Check - Checking to see if an invalid customer code was input
    invalid_code = True
    customer_bill = 0

#Error Check - Checking to see if an invalid meter value was input
if customer_bmr < 0 or customer_emr < 0 or customer_bmr > 999999999 or customer_emr > 999999999:
    meter_or = True
    customer_gwu = 0
    customer_bill = 0

#Printing the summary of information
print("\nCustomer Code:", customer_code)
print("Beginning Meter Reading: {:0>9}".format(customer_bmr))
print("Ending Meter Reading: {:0>9}".format(customer_emr))
if meter_or == True: #Error - Activates if an incorrect meter value was input
    print("!Invalid Meter Value(s)")
print("Gallons of Water Used: {:.1f}".format(customer_gwu))
if invalid_code == True: #Error - Activates if an incorrect customer code was input
    print("!Invalid Customer Code")
print("Amount Billed: ${:.2f}".format(customer_bill))
