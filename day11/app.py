# Simple example app
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == "__main__":
    data = fetch_data()
    print("Fetched Data:", data)
