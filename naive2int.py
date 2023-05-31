"""
naive solution 2 introduces randomness.  we add some padding (r) to the initial secret s.  
We add them together to get new value j.  Then Alice gets r and bob gets j and bob can 
reconstruct the secret by combining thier shares
"""

import random

# Initial secret
s = 867530991897891

# Generate a random value r
r = random.randint(10**(len(str(s))-1), 10**(len(str(s))))

j = r + s

alice_share = r
bob_share = j

reconstructed_secret = bob_share - alice_share

assert reconstructed_secret == s

print(f"reconstructed secret: {reconstructed_secret}")
