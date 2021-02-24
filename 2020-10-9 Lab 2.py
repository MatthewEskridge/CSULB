tip_percent=.18 #sets the tip percentage
sales_tax=.09 #sets the sales tax

subtotal=float(input('Please enter the cost of your meal: $'))

tip=(subtotal*tip_percent) #calculate tip
tax=((subtotal+tip)*sales_tax) #calculate tax
total=(subtotal+tip+tax) #calculate total

print('{:>11}'.format("Subtotal: $"), format(subtotal, ',.2f'), sep='')
print('{:>11}'.format("Tip: $"), format(tip, ',.2f'), sep='')
print('{:>11}'.format("Tax: $"), format(tax, ',.2f'), sep='')
print('{:>11}'.format("Total: $"), format(total, ',.2f'), sep='')
