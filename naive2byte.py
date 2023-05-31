"""
We can make naive2 implementation more elegant by working at the byte level
"""

import os

s = b'secret'

r = os.urandom(len(s))

# Calculate j (byte-wise addition modulo 256)
# I dont know what this is
j = bytes((s_byte + r_byte) % 256 for s_byte, r_byte in zip(s, r))

# Assign shares
alice_share = r
bob_share = j

# Alice and Bob combine their shares (byte-wise subtraction modulo 256)
# This part is confusing
reconstructed_secret = bytes((j_byte - r_byte) % 256 for j_byte, r_byte in zip(bob_share, alice_share))

# Check that the reconstructed secret is the same as the original secret
assert reconstructed_secret == s, "The reconstructed secret does not match the original secret."

print(f"Reconstructed secret: {reconstructed_secret.decode()}")

"""
still have problems.  the secret is still know by the constructer of the secret
The order is significant
No fault tolerance
not t/n as both shares are required to reconstruct the secret
"""