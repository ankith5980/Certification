days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# first three days
print("First three days:")
for i in range(3):
    print(days[i])

print("\n")

# print weekend
print("Weekend days:")
for i in range(5, 7):
    print(days[i])

print("\n")

# Check the existence of Friday in the tuple
print("Check for Friday:")
if "Friday" in days:
    print("Friday is in the tuple.")
else:
    print("Friday is not in the tuple.")
