import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title" : "Agentic AI",
    "body" : "The new wave of Agentic AI, transforming the future.",
    "image" : "robot.jpg",
    "User Id" : 1
}

r = requests.post(url, data=payload)
print(r.json())

response = requests.get(url)
print(response.json())