"""
A naive solution would split the scret in half between the two parties.  
This has multiple problems
"""
import threading
from concurrent.futures import ThreadPoolExecutor


s = 86753299189
s = str(s)

half = len(s) // 2

alice_half = s[:half]
bob_half = s[half:]

print(f"alice: {alice_half} bob: {bob_half}")

secret = int(alice_half + bob_half)

assert secret == int(s)

"""
The first problem with this is the knowledge one party or an attacker gains by knowing half the secret.

"""
# Let's say an attacker has got Alice's share
attacker_share = alice_half

print("Guessing through possible bobs half")

counter = [0] # using mutable object for updating inside closure???  What does this mean??

lock = threading.Lock() # to avoid race condition  ## What does this mean??

def try_key(i):
    possible_share = str(i).zfill(len(bob_half))
    secret_guess = int(attacker_share + possible_share)
    with lock:  # only one thread an increment counter at a time
        counter[0] += 1
        # Every 10000 guesses print how many guesses hav been tries
        if counter[0] % 10000 == 0:
            print(f"Trying {counter[0]}...")
        if secret_guess == int(s):
            print("\n attacker has guess the secret: {secret_guess}")
            return True
        return False

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(try_key, i) for i in range(10**len(bob_half))}
    for future in futures:
        if future.done() and future.result():
            print("Attacker has guessed the secret!")
            for f in futures:
                f.cancel()
            break
        


'''
This approach also is not zero knowledge meaning each key holder gets knowledge of the completed key
they would not get if the wernt share holders.  

This approach has dependence on order of shares

And this approach has no fault tolerence meaning if alice loses her half the secret cannot be reconstructed
'''