college_clubs = {
    "Coding Club": {("CS2301", "Alice"), ("EC2345", "Bob")},
    "Music Club": {("CS2301", "Alice"), ("ME2310", "Charlie")}
}

print("--- Initial State of Clubs ---")
print(college_clubs)
print("="*30)



print("\n--- Feature 1: Adding a new club ---")
print("Action: Creating 'Robotics Club' and adding David.")


college_clubs["Robotics Club"] = set() 


new_member = ("EE2315", "David")
college_clubs["Robotics Club"].add(new_member)

print("Clubs after adding 'Robotics Club':")
print(college_clubs)
print("="*30)



print("\n--- Feature 2: Adding and Removing Members ---")
print("Action: Adding Ivy to Coding Club, then removing Alice.")


college_clubs["Coding Club"].add(("ME2399", "Ivy")) 


college_clubs["Coding Club"].remove(("CS2301", "Alice"))

print("Coding Club after changes:")
print(college_clubs["Coding Club"])
print("="*30)



print("\n--- Feature 3: Finding Common Members ---")

college_clubs["Music Club"].add(("CS2301", "Alice")) 
college_clubs["Coding Club"].add(("CS2301", "Alice")) 

print("Finding members in BOTH 'Coding Club' AND 'Music Club'.")


common_members = college_clubs["Coding Club"] & college_clubs["Music Club"]

print("Common Members:")
print(common_members)
print("="*30)



print("\n--- Feature 4: Finding Unique Members ---")
print("Finding members in 'Coding Club' but NOT in 'Music Club'.")


unique_members = college_clubs["Coding Club"] - college_clubs["Music Club"]

print("Unique to Coding Club (compared to Music Club):")
print(unique_members)
print("="*30)



print("\n--- Feature 5: Final Club Roster and Counts ---")


for club, members in college_clubs.items():

    print(f"- Club: {club}, Member Count: {len(members)}") 
    print(f"  Members: {members}")

print("="*30)