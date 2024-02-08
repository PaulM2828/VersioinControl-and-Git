wildBearProject.py

# Collect information about a wild Romanian bear
bear_location = input("Enter the location where the wild bear was spotted: ")

# Check if the input is empty
while not bear_location.strip():
    print("Location cannot be empty. Please enter a valid location.")
    bear_location = input("Enter the location where the wild bear was spotted: ")

bear_descriptions = input("Describe the wild bear's appearance and behavior: ")

# Check if the input is empty
while not bear_descriptions.strip():
    print("Description cannot be empty. Please enter a valid description.")
    bear_descriptions = input("Describe the wild bear's appearance and behavior: ")

# Display the gathered information
print("\nWild Bear Information:")
print("Location: ", bear_location)
print("Description: ", bear_descriptions)
