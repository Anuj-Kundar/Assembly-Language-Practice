print('------Discount Calculator ----- ')
mrp = int(input('Enter MRP of product : '))
discount = int(input('Enter discount of product : '))
cost = mrp - (discount/100)*mrp
print('You have to pay ',cost)