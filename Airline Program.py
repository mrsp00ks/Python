seats_fullplane = 100 #saying plane has 100 seats
fullfare_wel = discountfare_wel = 200.00 #full un discounted price of flight
fullfare_rot = discountfare_rot = 150.00 
fullfare_auck = discountfare_auck = 99.90 
seats_wel = seats_rot = seats_auck = 0 
discountclass_wel = discountclass_rot = discountclass_auck = "undefined" 
banner = "Thanks for flying Air Waikato, These saver fares for tomorrow only!" 
ok = False 
while not ok:
    try:
        seats_wel = int(input('Enter number of seats on Wellington Flight :\n')) #Question to the cusomers
        ok = True
        if seats_fullplane < seats_wel or seats_wel <0:
            ok = False
        seats_rot = int(input('Enter number of seats on Rotorua Flight :\n'))
        ok = True
        if seats_fullplane < seats_rot or seats_rot <0:
            ok = False
        seats_auck = int(input('Enter number of seats on Auckland Flight :\n')) 
        ok = True
        if seats_fullplane < seats_auck or seats_auck <0:
            ok = False
        if seats_fullplane > seats_wel > 70:
            seats_wel = 70
        if seats_fullplane > seats_rot > 70:
            seats_rot = 70
        if seats_fullplane > seats_auck > 70:
            seats_auck = 70

        if seats_fullplane < seats_rot or seats_rot < 0 or seats_fullplane < seats_auck or seats_auck < 0 or seats_fullplane < seats_wel or seats_wel < 0:
            ok = False
            print ('There was an invalid input, please re-enter all integer values between 0 and',seats_fullplane)
        
    except ValueError:
        print ('please enter valid integer values between 0 and ',seats_fullplane)
        ok = False

if (seats_wel < 10) and (seats_auck < 10) and (seats_rot < 10):
    print("NO EMAIL TODAY - Insuficiant Discounts")

else: 
    print ("*** Email Start", "\n")
    print (banner, "\n") # Emailing process
    discountfare_wel = fullfare_wel - (seats_wel/seats_fullplane*fullfare_wel) 
    ok = False
    if 0.1 <=(1 - discountfare_wel/fullfare_wel) <0.2 : #saver type for wellington
        discountclass_wel = "Quick Saver"
        ok = True 
    if 0.2 <=(1 - discountfare_wel/fullfare_wel) <0.5 :
        discountclass_wel = "Smart Saver"
        ok = True
    if 0.5 <=(1 - discountfare_wel/fullfare_wel) :
        discountclass_wel = "Super Saver"
        ok = True
    if 0.1 >= (1 - discountfare_wel/fullfare_wel) :
        ok = False 
    if ok:
        print("Regular fare to Wellington is $", fullfare_wel)
        print("Discounted fare to Wellington is a", discountclass_wel," = $", "%.2f" % discountfare_wel, "\n")
    discountfare_rot = fullfare_rot - (seats_rot/seats_fullplane*fullfare_rot) 
    ok = False 
    if 0.1 <=(1 - discountfare_rot/fullfare_rot) <0.2 : #saver type for wellington
        discountclass_rot = "Quick Saver"
        ok = True
    if 0.2 <=(1 - discountfare_rot/fullfare_rot) <0.5 :
        discountclass_rot = "Smart Saver"
        ok = True
    if 0.5 <=(1 - discountfare_rot/fullfare_rot) :
        discountclass_rot = "Super Saver"
        ok = True
    if 0.1 >= (1 - discountfare_rot/fullfare_rot) :
        ok = False
    if ok:
        print("Regular fare to Rotorua is $", fullfare_rot)
        print("Discounted fare to Rotorua is a", discountclass_rot," = $", "%.2f" % discountfare_rot, "\n")
    discountfare_auck = fullfare_auck - (seats_auck/seats_fullplane*fullfare_auck)
    ok = False 
    if 0.1 <=(1 - discountfare_auck/fullfare_auck) <0.2 : #saver type for wellington
        discountclass_auck = "Quick Saver"
        ok = True
    if 0.2 <=(1 - discountfare_auck/fullfare_auck) <0.5 :
        discountclass_auck = "Smart Saver"
        ok = True
    if 0.5 <=(1 - discountfare_auck/fullfare_auck) :
        discountclass_auck = "Super Saver"
        ok = True
    if 0.1 >= (1 - discountfare_auck/fullfare_auck) :
        ok = False
    if ok:
        print("Regular fare to Auckland is $", fullfare_auck)
        print("Discounted fare to Auckland is a", discountclass_auck," = $", "%.2f" % discountfare_auck, "\n")
    print("For more information follow the link www.waikatoair.co.nz/dailydeals or free call 0800-999999", "\n")
    print("*** Email End", "\n", "\n")
    print("Dispatch Email to Group: loyaltycustomers@waikatoair.co.nz")
    print("Email has been dispatched to all prior customers enrolled")
