TICKET_PRICE = 10
tickets_remaining = 100
# Run this code continously until we run out of tickets
while tickets_remaining >= 1:
    # Output how many tickets are remainig using the tickets_remaining variabe    
    print("There are {} tickets remaining.".format(tickets_remaining))
    #Gather the user's name and assign it to a new variable
    name = input ("What is your name?")
    # Prompt the user by name and ask how many tickets they would buy
    num_tickets = input("How many tickets would you like, {}".format(name))
    # Expect av ValueError to happend and handle it appropriately
    try:
        num_tickets = int(num_tickets)   
        # Raise a ValueError if the request for more tickets than are avaiable 
        if num_tickets > tickets_remaining:
            raise ValueError("There is only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no. We ran into an issue. Please try again.".format(err))
    else:
        # Calculate the price (number of tickets)
        amount_due = num_tickets * TICKET_PRICE
        print("The total due is ${}".format(amount_due))  
        # Prompt user if they want to proceed Y/N
        should_proceed = input("Do you want to proceed? Y/N")
        # if they wnt to proceed
        if should_proceed.lower() == "y" :
            #print out to the scren "SOLD" to confirm purchase
            # TODO: Gather credit card information
            print("SOLD!")
            # and then decrement the ticket remaining by the number of tickets
            tickets_remaining -= num_tickets
        #otherwise
        else:
            #Thank them
            print("Thank you anyway, {}!".format(name)) 
#Notify user that the tickets are sold out
print("Sorry the tickets are sold out.")    