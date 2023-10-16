import sys

from sayings import hello
# We are importing fucntions defined in the file sayings.py

if len(sys.argv) == 2:
    hello(sys.argv[1])

# Run as python say.py <name>
