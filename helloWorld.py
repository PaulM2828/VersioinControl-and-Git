# wildBearProject.py
from datetime import datetime

# Collect information about a wild Romanian bear
bear_location = input("Enter the location where the wild bear was spotted: ")
bear_descriptions = input("Describe the wild bear's appearance and behavior: ")

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display the gathered information with timestamp
print("\nWild Bear Information:")
print("Timestamp: ", timestamp)
print("Location: ", bear_location)
print("Description: ", bear_descriptions)
