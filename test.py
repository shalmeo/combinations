import requests

data = {
    "parameters": {
        "OS": ["Windows 7", "Windows 10", "Mac OS X"],
        "Browser": ["Google Chrome", "Safari", "Firefox"],
        "Resolution": ["1920*1080", "1600*900", "1366*768"],
    },
    "conditions": {
        "can": [{"Browser": "Safari", "OS": "Mac OS X"}],
        "cannot": [{"Browser": "Firefox", "OS": "Mac OS X"}],
    },
}

response = requests.post(
    url="http://127.0.0.1:8000/combinations/pair",
    json=data,
    headers={"Content-type": "application/json"},
)
print(response.status_code)
