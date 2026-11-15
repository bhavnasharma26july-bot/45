
def totalbill(billamount, tip):
    
    total = (billamount/100*tip)+billamount
    total = (total)
    print("Please pay $",total)
    return total
 

totalbill(150, 20)
 
 

def seatingarrangements(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
 
   
    if guests == 0 or guests == 1:
        return 1
 
  
    else:
        return guests * seatingarrangements(guests - 1)
 

print(seatingarrangements.__doc__)
 

print("Seating arrangements for 1 guest:", seatingarrangements(1))
print("Seating arrangements for 2 guests:", seatingarrangements(2))
print("Seating arrangements for 3 guests:", seatingarrangements(3))

