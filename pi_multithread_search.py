import requests
from concurrent.futures import ThreadPoolExecutor

# Define the function to read Pi digits from URL
def read_pi_digits_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a valid response
    return response.text.replace(".", "")  # Remove the decimal point

# Define the function to check if a number is in Pi
def is_number_in_pi(number, pi_digits):
    return str(number) in pi_digits

# Function to search a range of numbers and return those not found in Pi
def search_range(start, end, pi_digits):
    missing_numbers = []
    for number in range(start, end + 1):
        if not is_number_in_pi(number, pi_digits):
            missing_numbers.append(number)
    return missing_numbers

# Main function to manage multithreading
def main():
    url = "https://dn790004.ca.archive.org/0/items/Pi-1b-digit/pi1b.txt"
    pi_digits = read_pi_digits_from_url(url)
    range_start = 1
    range_end = 1000000
    num_threads = 24  # Adjust based on your system's capabilities

    # Calculate the range each thread will search
    step = (range_end - range_start + 1) // num_threads
    futures = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start = range_start + i * step
            end = start + step - 1 if i < num_threads - 1 else range_end
            futures.append(executor.submit(search_range, start, end, pi_digits))

    # Collect and combine results from all threads
    all_missing_numbers = []
    for future in futures:
        all_missing_numbers.extend(future.result())

    print("Numbers not found in Pi:", all_missing_numbers)

if __name__ == "__main__":
    main()
