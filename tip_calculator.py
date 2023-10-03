# tip_calculator.py

def tip_calculator():
    try:  #DO NOT MODIFY
        total_cost = float(input("Enter the cost of the meal (without tax): "))
        num_people = int(input("Enter the number of people splitting the bill: "))
        tip_percentage = float(input("Enter the tip percentage: "))

        tip_percentage = tip_percentage/100
        sales_tax = (total_cost*0.10)
        total_tip = (total_cost*tip_percentage)
    
        total_bill = (total_cost + total_tip + sales_tax)
        each_pays = total_bill/num_people
    
        print(f'Total bill: ${total_bill:.2f}')
        print(f'Each person should pay: ${each_pays:.2f}')
    
    except ValueError:
        print("Invalid Input")

# TODO: Create a function named calculate_tip
 
# TODO:
    # Get these user inputs 
    # total_cost (float): The cost of the meal (without tax) 
    # num_people (int): The number of people splitting the bill 
    # tip_percentage (float): The tip percentage

# TODO:
    # Calculate the total bill including tip and sales tax (10%).
    # Convert to float: The total bill (including tip and sales tax).

# NOTE: Calculate the tip and tax separately. 
     
# TODO: 
    # Calculate how much each person should pay.
    # Convert to float: The amount each person should pay.   
    
# TODO:
    # Using an f-string, print two different statements 
    # Total bill: $0.00
    # Each person should pay: $0.00

# NOTE: The amounts are displayed with 2 decimals only
        
    # TODO: modify this except to include a Built-in Exception
    # TODO: Print an statement telling the user their input is invalid
    
if __name__ == "__main__": # DO NOT MODIFY
#    tip_calculator() # DO NOT MODIFY