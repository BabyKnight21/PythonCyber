import hashlib
import random

# Function to generate a random string of a given length
def generate_random_string(length):
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	return ''.join(random.choice(charset) for _ in range(length))

# Function to perform the Birthday Attack
def birthday_attack():
	hash_dict = {}
	num_attempts = 0

	while True:
		num_attempts += 1
		random_string = generate_random_string(10)
		hash_value = hashlib.md5(random_string.encode()).hexdigest()

		if hash_value in hash_dict:
			print(f"Collision found after {num_attempts} attempts!")
			print(f"Original String 1: {hash_dict[hash_value]}")
			print(f"Original String 2: {random_string}")
			break

		hash_dict[hash_value] = random_string

# Example usage
if __name__ == "__main__":
	birthday_attack()