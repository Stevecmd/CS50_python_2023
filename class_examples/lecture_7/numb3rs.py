import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to match valid IPv4 address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    return bool(re.search(pattern, ip))

if __name__ == "__main__":
    main()

# Notes
# Regular Expression Pattern:
# pattern = r'^...$': The caret (^) and dollar sign ($) ensure that the pattern matches the entire string from start to end, respectively.

# ((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}:
# This is the core of the regex, and it matches a segment of an IP address.
# This segment is repeated {3} times, meaning it matches the first three segments of the IP address, including their trailing dots.

# 25[0-5]: Matches numbers 250-255.
# 2[0-4][0-9]: Matches numbers 200-249.
# [01]?[0-9][0-9]?: Matches numbers 0-199. The [01]? matches 0 or 1 (or none),
# and the subsequent [0-9][0-9]? matches one or two digits. This combination covers all numbers from 0 to 199.
# The \. at the end matches the dot that separates segments in an IP address.
# (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$: This matches the last segment of
# the IP address. It's essentially the same as the prior segment match, but without the trailing dot.
# The dollar sign $ ensures this is the end of the string.