import requests

r = requests.get("https://www.linkedin.com/in/shamoon-ahmed-496a6231b/")
# print(r.text)
print(r.status_code)