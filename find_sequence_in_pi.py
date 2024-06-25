import requests

def find_sequence_in_pi(target_numbers):
    url = "https://dn790004.ca.archive.org/0/items/Pi-1b-digit/pi1b.txt"
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a valid response

    pi_digits = response.text.replace(".", "")  # Remove the decimal point

    furthest_length = 0

    for number in target_numbers:
        found = pi_digits.find(str(number))
        if found == -1:
            raise ValueError(f"Number {number} not found in pi.")

        length = found + 1
        distance = length - furthest_length

        if length > furthest_length:
            advance_message = "Advanced"
            furthest_length = length
            print(f"Number {number}: {advance_message}, Length: {length}, Distance from last: {distance}")
            print(f"({number}, {length})")  # Fixed print statement here
        else:
            advance_message = "No Advance"

# Example usage
target_numbers = range(1, 100000)
find_sequence_in_pi(target_numbers)


# if you have the file locally just use
# with open("pi-billion.txt", "r") as file:
#        pi_digits = file.read().replace(".", "")  # Remove the decimal point