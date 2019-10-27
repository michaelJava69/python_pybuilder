#!/home/michael/MyPythonProject/env/bin/python2
import sys

from example_primes import first_N_primes

N = 10
print("The first",N,"primes are:")

for n in first_N_primes(N):
    print(n)
print()
