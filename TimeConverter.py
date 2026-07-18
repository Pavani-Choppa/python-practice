import datetime
# Read total seconds
total = int(input())

# Calculate hours, minutes, seconds
#t = str(datetime.timedelta(seconds = total))
#print(t)
hours = total // 3600
mi = (total % 3600) // 60
se = total % 60
# Print the result
print(f"{hours}h {mi}m {se}s")
