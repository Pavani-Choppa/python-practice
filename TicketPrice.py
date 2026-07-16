# Read age from input
age = int(input())

# Determine ticket type and price based on age
if age < 12:
  ag = "Child"
  price = 5
elif age <= 64:
  ag = "Adult"
  price = 15
else :
  ag = "Senior"
  price = 8
# Print results
print(ag)
print(f"${price}")
