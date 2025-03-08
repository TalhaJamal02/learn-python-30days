import multiprocessing
import requests
import threading
import time
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# Task 1:
# List of API endpoints:
urls = [
    "https://official-joke-api.appspot.com/random_joke",
    "https://api.agify.io?name=John",
    "https://api.nationalize.io?name=John"
]

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(f"Data from {url}: {response.json()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

start_time = time.time()

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(
    f"Execution Time with Multithreading: {end_time - start_time:.2f} seconds")

# What Happens above ^ ?
# We use multiple threads to send requests simultaneously.
# The main program waits for all threads to complete using .join().
# This improves performance by handling multiple API calls at the same time.


# Task 2:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to compute factorial using multiprocessing
def compute_factorial(n):
    print(f"Factorial of {n}: {factorial(n)}")

if __name__ == "__main__":
    numbers = [500, 600, 700, 800]

    # Start timing
    start_time = time.time()

    # Create processes
    with multiprocessing.Pool(processes=4) as pool:  # Use 4 parallel processes
        pool.map(compute_factorial, numbers)

    # End timing
    end_time = time.time()
    print(
        f"Execution Time with Multiprocessing: {end_time - start_time:.2f} seconds")


# Task 3: Comparing Single-threaded, Multithreaded, and Multiprocessing Performance
def sum_of_primes(n):
    total = 0
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            total += num
    return total

if __name__ == '__main__':
    n = 10000

    # Single-threaded execution
    start = time.time()
    result = sum_of_primes(n)
    end = time.time()
    print(f"Single-threaded Result: {result}")
    print(f"Single-threaded Execution Time: {end - start:.2f} seconds\n")

    # Multithreading execution (Using ThreadPoolExecutor)
    start = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(sum_of_primes, [n, n]))  # Running twice

    end = time.time()
    print(f"Multithreading Results: {results}")
    print(f"Multithreading Execution Time: {end - start:.2f} seconds\n")

    # Multiprocessing execution (Using ProcessPoolExecutor)
    start = time.time()
    processes = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(sum_of_primes, [n, n]))  # Running twice

    end = time.time()
    print(f"Multithreading Results: {results}")
    print(f"Multiprocessing Execution Time: {end - start:.2f} seconds")