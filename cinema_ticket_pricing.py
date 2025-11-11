#CINEMA_TICKET_PRICING.  !!WRONG CODE!!
num_of_tickets =int(input("Enter no. of tickets:"))
age = int(input("Enter your age:"))

base_price = 200

a= ((base_price)*50/100)
b= ((base_price)*30/100)

disc_price1= (base_price - a)
disc_price2= (base_price- b)


GST_1 = (disc_price1 + ((a)*18/100)*num_of_tickets)
GST_2 = (disc_price2 + ((b)*18/100)*num_of_tickets)
GST_3 = (base_price + ((base_price)*18/100)*num_of_tickets)



if (age< 12):
    print("Congrats! you get 50% Discount!")
    print("Your discounted price is:", disc_price1)
    print("Your Total Amount is:",GST_1)
   
elif (age>60):
    print("Congrats! you get 30% Discount!")
    print("Your discounted price is:",disc_price2)
    print("Your Total Amount is:",GST_2)

else:
    print("Your Total Amount is:", GST_3)