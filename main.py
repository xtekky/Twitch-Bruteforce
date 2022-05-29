import requests

url = "https://passport.twitch.tv/login"

passw = ""
username = ""

payload = f"{\"client_id\":\"kd1unb4b3q4t58fwlpcbzcbnm76a8fp\",\"force_twitchguard\":false,\"password\":\"{passw}\",\"undelete_user\":false,\"username\":\"{username}\"}"

headers = {
    "content-type": "application/json; charset=UTF-8",
    "host": "passport.twitch.tv",
    "connection": "Keep-Alive",
    "accept-encoding": "gzip",
    "client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
    "accept": "application/vnd.twitchtv.v3+json",
    "accept-language": "en-us",
    "x-device-id": "7549bd7d0bf549159a556926aebf0c43",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
