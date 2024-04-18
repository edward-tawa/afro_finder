import requests


sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format("rules"),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
if sub_info.status_code >= 300:
    print(0)
print(sub_info.json().get("data"))
print(sub_info.json().get("data").get("subscribers"))