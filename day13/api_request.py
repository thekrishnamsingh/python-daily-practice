import requests

def fetch_post(post_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data. Status:", response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print("API request error:", e)
        return None


if __name__ == "__main__":
    post = fetch_post(1)
    print("Fetched Post:", post)
