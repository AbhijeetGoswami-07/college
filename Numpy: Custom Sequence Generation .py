import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# Generate the sequence
sequence = np.arange(start, stop, step)

# Print the sequence
print(sequence)
