import random
import string

def generate_insulin_data():
    # Generate a random string sequence of length 10
    sequence = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    
    # Generate a random numeric weight between 0 and 100
    weight = random.uniform(0, 100)
    
    return sequence, weight

# Example usage:
sequence, weight = generate_insulin_data()
print(f"Sequence: {sequence}")
print(f"Numeric Weight: {weight}")

