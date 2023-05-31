Following along https://replit.com/@Kody/Tutorial-Shamir-Secret-Sharing-and-DKG

White paper on secret sharing: https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf


Shamir secret sharing is defining a random polynomial where the y intercept is the secret and picking points on it to give out as the shares.  The power of the polynomial has to be one less than the number of shares you want to recover.  The number of shares(points) is the pool from which the shares can be taken from to recover 
the secret.  Any n number of points where n is one more than the power of the polynomial can reconstruct the curve and find the y intercept which is the secret