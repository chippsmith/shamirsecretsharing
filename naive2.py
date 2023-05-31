import random
import os

print("---- Naive Solution 2: Introducing Randomness ----\n")

print("Approach 1: Integer Level")
print("In this approach, Dealer Dave will introduce some randomness while sharing his secret between Alice and Bob at an integer level. Dave uses a secret 's' and a random value 'r' such that 's' + 'r' = 'j'.\n")

# Initial secret
s = 867530991897891
print(f"Initial secret (s): {s}\n")

# Generate a random value r
r = random.randint(10**(len(str(s))-1), 10**(len(str(s))))
print(f"Random value (r): {r}\n")

# Calculate j
j = s + r
print(f"Calculate 'j' such that 's' + 'r' = 'j' : {j}\n")

# Assign shares
alice_share = r
bob_share = j
print(f"Alice's share: {alice_share}")
print(f"Bob's share: {bob_share}\n")

# Alice and Bob combine their shares
reconstructed_secret = bob_share - alice_share
print(f"Reconstructed secret: {reconstructed_secret}\n")

# Check that the reconstructed secret is the same as the original secret
assert reconstructed_secret == s, "The reconstructed secret does not match the original secret."
print("Reconstructed secret matches the original secret.\n")

print("----\n")
print("Approach 2: Byte Level")
print("In this approach, Dealer Dave introduces some randomness at the byte level while sharing his secret between Alice and Bob.\n")

# Initial secret
s = b'secret'
print(f"Initial secret (s): {s.decode()}\n")

# Generate a random value r
r = os.urandom(len(s))
print(f"Random value (r): {r}\n")

# Calculate j (byte-wise addition modulo 256)
j = bytes((s_byte + r_byte) % 256 for s_byte, r_byte in zip(s, r))
print(f"Calculate 'j' (byte-wise addition modulo 256) : {j}\n")

# Assign shares
alice_share = r
bob_share = j
print(f"Alice's share: {alice_share}")
print(f"Bob's share: {bob_share}\n")

# Alice and Bob combine their shares (byte-wise subtraction modulo 256)
reconstructed_secret = bytes((j_byte - r_byte) % 256 for j_byte, r_byte in zip(bob_share, alice_share))
print(f"Reconstructed secret: {reconstructed_secret.decode()}\n")

# Check that the reconstructed secret is the same as the original secret
assert reconstructed_secret == s, "The reconstructed secret does not match the original secret."
print("Reconstructed secret matches the original secret.")
