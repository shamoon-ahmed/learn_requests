import requests

# EXAMPLE 1: creating a new blog post

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title" : "Agentic AI",
    "body" : "The new wave of Agentic AI, transforming the future.",
    "image" : "robot.jpg",
    "User Id" : 1
}

r = requests.post(url, data=payload)
# print(r.json())

r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(r.status_code)

response = requests.get(url)
# print(response.json())

# EXAMPLE 2: creating a new user account

url = "https://reqres.in/api/register"

headers = {
    "x-api-key" : "reqres-free-v1"
}
payload = {
    "email" : "eve.holt@reqres.in",
    "password" : "pistol"
}

res = requests.post(url, data=payload, headers=headers)
# print(res.json())

# EXAMPLE 3: Uploading a file 

url = "https://httpbin.org/post"

files = {
    "file" : ("test.txt", open("test.txt", "rb"))
}

resp = requests.post(url, files=files)
print(resp.json())
print(resp.status_code)