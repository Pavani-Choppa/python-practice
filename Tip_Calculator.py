# Tip Calculator

def calculate_tip(bill, tip_percent):
    # Calculate tip and total
    tip = (bill*tip_percent)/100
    total = bill+tip
    # Print formatted results
    print("Bill: $"+format(bill,".2f"))
    print("Tip: $"+format(tip,".2f"))
    print("Total: $"+format(total,".2f"))
    

# Read input
bill = float(input())
tip_percent = int(input())

calculate_tip(bill, tip_percent)
