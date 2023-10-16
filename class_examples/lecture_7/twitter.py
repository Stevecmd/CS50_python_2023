# Solution 1
# import re

# url = input("URL: ").strip()

# username = re.sub(r"^(https://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# # Solution 2
# import re

# url = input("URL: ").strip()
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username:", matches.group(2))

# # Solution 3
# import re

# url = input("URL: ").strip()
# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"Username:", matches.group(2))

# Notes:
# A|B either A or B
# (...) a group
# (?:...) non-capturing version

# Solution 4
import re

url = input("URL: ").strip()
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))