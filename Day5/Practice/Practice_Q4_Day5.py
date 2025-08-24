import numpy as np

# An array of random temperature values
temp_c = np.random.uniform(5, 50, 365)
print("Temperatures :: ", temp_c)

print("\n")

# Finding the hottest day
hot_temp_c = temp_c.max() # hottest temp
hot_day_c = temp_c.argmax() # hottest day
print(f"Hottest Day :: {hot_day_c + 1}, Temperature :: {hot_temp_c:.2f}°C")

print("\n")

# Calculating Average Temperature
avg_temp = temp_c.mean()
print(f"Average Temperature :: {avg_temp}")

print("\n")

# Converting all the temperature into fahrenhiet
temp_f = (temp_c * 9/2) + 32
print(temp_f)

print("\n")

# hottest day in fahrenhiet
hot_temp_f = temp_f.max() # hottest temp
hot_day_f = temp_f.argmax() # hottest day
print(f"Hottest Day :: {hot_day_c + 1}, Temperature :: {hot_temp_c:.2f}°F")

print("\n")
print("========================")
print("\n")

# Simulating coin tosses
coin_tosses = np.random.choice(["H", "T"], 10)
print(f"Tosses :: {coin_tosses}")

print("\n")

# counting the number of heads and tails
coin_head = np.count_nonzero(coin_tosses == "H")
coin_tail = np.count_nonzero(coin_tosses == "T")
print(f"Heads :: {coin_head}, Tails :: {coin_tail}")

print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
