import requests
import json
import os
import re
import random
from getuseragent import UserAgent
import os
import re
import sys
import time
import json
import random
import datetime
import requests
from rich import print as rich_print
import sys
import os
import requests
import threading
import time

__AUTHOR__ = 'Pham Dinh Quoc '
__CONTACT__ = 'fb.com/PhDinhQuoc '
def jovan(): 
    print("""\033[1;31m
                  ███████╗███╗   ███╗███╗   ███╗
                  ██╔════╝████╗ ████║████╗ ████║
                  ███████╗██╔████╔██║██╔████╔██║
                  ╚════██║██║╚██╔╝██║██║╚██╔╝██║
                  ███████║██║ ╚═╝ ██║██║ ╚═╝ ██║
                  ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝
\033[1;37m──────────────────────────────────────────────────────────────\033[1;37m
          \033[1;31mOWNER    \033[1;32m: \033[1;37mSMM BOOSTING 
          \033[1;31mCODED IN \033[1;32m: \033[1;37mPYTHON
          \033[1;31mVERSION  \033[1;32m: \033[1;37m4.1
          \033[1;31mTOOL     \033[1;32m: \033[1;37mAUTO BOOST FACEBOOK
\033[1;37m──────────────────────────────────────────────────────────────\033[1;37m""")




def ban():
   print("""
\033[1;38;2;255;105;180m   

╔═╗╦ ╦╔╦╗╔═╗  ╔═╗╦ ╦╔═╗╦═╗╔═╗
╠═╣║ ║ ║ ║ ║  ╚═╗╠═╣╠═╣╠╦╝║╣ 
╩ ╩╚═╝ ╩ ╚═╝  ╚═╝╩ ╩╩ ╩╩╚═╚═╝

\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m
Coded By: Jovan
Programming Language use: Python
 Multithread: NO
\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m
\033[0m""")

def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')

gome_token = []

def tokz(input_cookies):
    for cookie in input_cookies:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
def shar():
    input_cookies = input("\x1b[38;2;173;255;47mEnter Cookie:  \x1b[38;2;233;233;233m").split(',')
    id_share = input("\x1b[38;2;173;255;47mEnter Post ID: \x1b[38;2;233;233;233m")
    total_share = int(input("\x1b[38;2;173;255;47mHow Many Share: \x1b[38;2;233;233;233m"))
    delay = int(input("\x1b[38;2;173;255;47m Delay Share: \x1b[38;2;233;233;233m"))
    print('\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m')
    print('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mwaiting...', end='\r')

    all = tokz(input_cookies)
    total_live = len(all)
    print(f'\x1b[38;2;173;255;47mLive: \x1b[38;2;233;233;233m{total_live} \x1b[38;2;173;255;47mCookies')
    
    if total_live == 0:
        sys.exit()

    print('\x1b[38;2;173;255;47m════════════════════════════════════\x1b[38;2;233;233;233m')
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            print(f'\x1b[38;2;173;255;47mShare: + \x1b[38;2;233;233;233m{stt}', end='\r')
            time.sleep(delay)
        if stt > total_share:
            break

    gome_token.clear()
    input('\x1b[38;2;173;255;47m[*] \x1b[38;2;233;233;233mEnter^^\033[0m')


    

def Load_data_alot():
    """Load data from a JSON file."""
    try:
        with open('Eaau.json', 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return {"access_tokens": []}  # Assuming only personal account tokens are stored
    except FileNotFoundError:
        return {"access_tokens": []}
    except json.decoder.JSONDecodeError:
        print("Error: Failed to decode JSON from Eaau.json. File might be corrupted.")
        return {"access_tokens": []}

def saving_data(data):
    """Save data to a JSON file."""
    with open('Eaau.json', 'w') as file:
        json.dump(data, file, indent=4)
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def Auto_react_comment_fast(post_id, reaction_type, reactor_type, num_reactions):
    """Perform reactions on a Facebook post/comment."""
    access_tokens_data = Load_data_alot()
    access_tokens = access_tokens_data.get("access_tokens", [])

    total_reactions_sent = 0

    def react_with_token(access_token, reactor_type):
        nonlocal total_reactions_sent  # Allows modifying total_reactions_sent inside the inner function
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                pages = token_info.get("pages", [])
                for page in pages:
                    page_access_token = page.get("access_token", "")
                    page_name = page.get("name", "")
                    try:
                        if not has_reacted(post_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                total_reactions_sent += 1
                                print(f"Successfully reacted using Page '{page_name}' ✅")
                                if total_reactions_sent >= num_reactions:
                                    return True
                            else:
                                print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        print(f"Exception occurred while reacting using Page '{page_name}': {error}")

            elif reactor_type == "ACCOUNT":
                try:
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print("Successfully reacted using Personal Profile ✅")
                            if total_reactions_sent >= num_reactions:
                                return True
                        else:
                            print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                except requests.exceptions.RequestException as error:
                    print(f"Exception occurred while reacting using Personal Profile: {error}")

            elif reactor_type == "BOTH":
                try:
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            total_reactions_sent += 1
                            print("Successfully reacted using both methods ✅")
                            if total_reactions_sent >= num_reactions:
                                return True
                        else:
                            print(f"Failed to react. Status code: {response.status_code}, Response: {response.text}")
                except requests.exceptions.RequestException as error:
                    print(f"Exception occurred while reacting: {error}")

        else:
            print("Invalid access token format")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "")
            futures.append(executor.submit(react_with_token, access_token, reactor_type))

        for future in as_completed(futures):
            if total_reactions_sent >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {total_reactions_sent}")

# Example usage
# Auto_react_comment('123456789', 'LIKE', 'BOTH', 10)

def Auto_react_comment(post_id, reaction_type, reactor_type, num_reactions):
    """Perform reactions on a Facebook post/comment."""
    access_tokens_data = Load_data_alot()
    access_tokens = access_tokens_data.get("access_tokens", [])

    reactions_count = 0
    total_reactions_sent = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "")
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    # Use only pages as reactors
                    pages = token_info.get("pages", [])
                    for page in pages:
                        page_access_token = page.get("access_token", "")
                        page_name = page.get("name", "")
                        try:
                            if not has_reacted(post_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)
                                
                                if response.status_code == 200:
                                    reactions_count += 1
                                    total_reactions_sent += 1
                                    print("\033[1m\033[92mSuccessfully\033[0m\033[1m\033[92m✅\033[0m")

                                    if total_reactions_sent >= num_reactions:
                                        print(f"Reached the limit of {num_reactions} reactions.")
                                        return
                                else:
                                    print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                        except requests.exceptions.RequestException as error:
                            print(f"Exception occurred while reacting using Page '{page_name}': {error}")
                        
                elif reactor_type == "ACCOUNT":
                    # Use only personal account as reactor
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                total_reactions_sent += 1
                                print("\033[1m\033[92m[Successfully\033[0m\033[1m\033[92m✅\033[0m\033[1m\033[92m]")

                                if total_reactions_sent >= num_reactions:
                                    print(f"\033[1m\033[92mReached the limit of {num_reactions} reactions✅.\033[0m")

                                    return
                            else:
                                print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        print(f"Exception occurred while reacting using Personal Profile: {error}")
                    
                elif reactor_type == "BOTH":
                    # Use both pages and personal account as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                total_reactions_sent += 1
                                if "pages" in token_info:  # Check if pages are available
                                    print("\033[1m\033[92mSuccessfully\033[0m\033[1m\033[92m✅\033[0m")

                                else:
                                    print("Successfully reacted using Personal Profile")
                                
                                if total_reactions_sent >= num_reactions:
                                    print(f"Reached the limit of {num_reactions} reactions.")
                                    return
                            else:
                                if "pages" in token_info:
                                    print(f"Failed to react using Page '{page_name}'. Status code: {response.status_code}, Response: {response.text}")
                                else:
                                    print(f"Failed to react using Personal Profile. Status code: {response.status_code}, Response: {response.text}")
                    except requests.exceptions.RequestException as error:
                        if "pages" in token_info:
                            print(f"Exception occurred while reacting using Page '{page_name}': {error}")
                        else:
                            print(f"Exception occurred while reacting using Personal Profile: {error}")
            else:
                print("Invalid access token format")
        except requests.exceptions.RequestException as error:
            print(f"Exception occurred: {error}")

    print(f"Total reactions sent: {total_reactions_sent}")

def has_reacted(post_id, access_token):
    """Check if the user has already reacted to the post."""
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            for reaction in data.get("data", []):
                if reaction.get("id") == access_token:  # Check if user ID matches access_token (simplified check)
                    return True
            return False
        else:
            print(f"Failed to check reactions. Status code: {response.status_code}, Response: {response.text}")
            return False
    except requests.exceptions.RequestException as error:
        print(f"Exception occurred while checking reactions: {error}")
        return False

MONTHS = {
    '1': 'januari', '2': 'februari', '3': 'maret', '4': 'april', '5': 'mei', '6': 'juni', 
    '7': 'juli', '8': 'agustus', '9': 'september', '10': 'oktober', '11': 'november', '12': 'desember'
}
DAYS = {
    'Sunday': 'Minggu', 'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu', 
    'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu'
}
COMMENTS = ['Semangat Bang', 'Keren Bang', 'Gokil Suhu', 'Panutanku', 'Semangat Terus']

# Session
ses = requests.Session()

# Helper functions
def get_current_date():
    now = datetime.datetime.now()
    return f"{now.day} {MONTHS[str(now.month)]} {now.year}"

def clear_screen():
    os.system('clear')

def login():
    clear_screen()
    cookie = input('</> 🥵Cookie🥵 : ')
    try:
        response = requests.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "cookie": cookie
            }
        )
        token = re.search(r"(EAAG\w+)", response.text).group(1)
        if token:
            with open('cookie.txt', 'w') as f:
                f.write(cookie)
            with open('token.txt', 'w') as f:
                f.write(token)
            rich_print("</> 🚭Login Successful🔞 !!! ")
            bot(cookie)
        else:
            raise AttributeError
    except AttributeError:
        rich_print("</> 😭Cookie Expired😓 !!")
        time.sleep(4)
        login()
    except requests.exceptions.ConnectionError:
        sys.exit("</> Internet Connection ERROR !!!")

def bot(cookie):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_day = DAYS[datetime.datetime.now().strftime("%A")]
    date_str = get_current_date()
    token = open("token.txt", "r").read()
    response_message = random.choice(COMMENTS)
    comment = f"\n\nhttps://www.facebook.com/100089033379675/posts/139149639062815/?app=fbl\n\nKomentar Ini Ditulis Oleh Bot"
    
    post_url = f"https://graph.facebook.com/100089033379675_139149639062815/comments"
    post_data = {
        "message": f"{response_message} {comment}\n[ Pukul {current_time} WIB ] \n- {current_day}, {date_str} -",
        "access_token": token
    }
    headers = {"cookie": cookie}
    requests.post(post_url, data=post_data, headers=headers)
    
    share_post()

def share_post():
    clear_screen()
    header = {
        "authority": "graph.facebook.com",
        "cache-control": "max-age=0",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"
    }
    post_link = input("</> 😘Your Fucking Post Link🥵 : ")
    share_limit = int(input("</> 🔰Share Limit🔰 : "))
    rich_print('</> Post Share Started...')
    
    cookie = open('cookie.txt', 'r').read()
    token = open('token.txt', 'r').read()
    cookies = {"cookie": cookie}
    
    try:
        for i in range(share_limit):
            response = ses.post(
                f"https://graph.facebook.com/me/feed?link={post_link}&published=0&access_token={token}",
                headers=header,
                cookies=cookies
            ).json()
            
            if "id" in response:
                                rich_print(f"</> Post Shared : {response['id']}")
                sys.stdout.flush()
            else:
                sys.exit('</> ERROR DATA\n')
                
        rich_print("</> All Shares Complete !!! ")
        input("</> Press Enter To Back")
        share_post()
    except requests.exceptions.ConnectionError:
        sys.exit('</> Server Error !!! \n')
def load_data():
    try:
        with open('Eaau.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"accounts": [], "access_tokens": []}
    except json.decoder.JSONDecodeError:
        return {"accounts": [], "access_tokens": []}
def load_data_rpw():
    try:
        with open('Rpw.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"accounts": [], "access_tokens": []}
    except json.decoder.JSONDecodeError:
        return {"accounts": [], "access_tokens": []}

def save_data(data):
    print("Saving data:", data)  
    with open('data.json', 'w') as f:
        if isinstance(data, dict):
            json.dump(data, f, indent=4)
        else:
            json.dump({"access_tokens": data}, f, indent=4)

def count_accounts_and_pages(data):
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])
    
    total_accounts = len(access_tokens)
    total_pages = sum(len(token.get("pages", [])) for token in access_tokens)
    
    return total_accounts, total_pages
class color:
    END = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'

def add_token():
    data = load_data()
    
    if isinstance(data, list):
        access_tokens = data
    else:
        access_tokens = data.get("access_tokens", [])
    
    while True:
        access_token = input('Enter your access token (if done just leave this blank): ')
        if not access_token:
            save_data(data)  
            main()  
            break
        
        
        
        if any(token.get("access_token") == access_token for token in access_tokens):
            print("Token already exists.")
            continue

        
        try:
            response = requests.get(f'https://graph.facebook.com/me?access_token={access_token}')
            if response.status_code == 200:
                is_valid_token = True
                
                pages_response = requests.get(f'https://graph.facebook.com/me/accounts?access_token={access_token}')
                if pages_response.status_code == 200:
                    pages_data = pages_response.json().get("data", [])
                   
                    account_data = {"access_token": access_token}
                    account_pages = [page for page in pages_data]
                    account_data["pages"] = account_pages
                    access_tokens.append(account_data)
                    if isinstance(data, list):
                        data = access_tokens  # Update data if it was initially a list
                    else:
                        data["access_tokens"] = access_tokens  # Update the access_tokens in the data structure
                        
                    print("\033[91mSuccessfully added Account\033[0m")  # Successfully added message in red
            else:
                is_valid_token = False
        except requests.exceptions.RequestException:
            is_valid_token = False

        if not is_valid_token:
            print("Invalid token. Please enter a valid token.")

        # Add this line for debugging
        save_data(data)

def Video_Extractid(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    video_pattern = r'videos/(\d+)/'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    video_match = re.search(video_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    elif video_match:
        video_id = video_match.group(1)
        return video_id
    else:
        return None
def perform_reaction_video(url, reaction_type, reactor_type, num_reactions):
    
    post_id = url
    if not post_id:
        print("[ERROR] Invalid URL or unable to extract post ID.")
        return

    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    # Use only pages as reactors
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        try:
                            if not has_reacted(post_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)
                                
                                if response.status_code == 200:
                                    reactions_count += 1
                                    print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, post_id, str(response.json())))
                                    if reactions_count >= num_reactions:
                                        print("Reached the limit of {} reactions.".format(num_reactions))
                                        return
                                else:
                                    print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                        except requests.exceptions.RequestException as error:
                            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
                elif reactor_type == "ACCOUNT":
                    # Use only accounts as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
                elif reactor_type == "BOTH":
                    # Use both pages and accounts as reactors
                    try:
                        if not has_reacted(post_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(post_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            else:
                print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        except requests.exceptions.RequestException as error:
            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            main()
import requests

def perform_reaction_media(url, reaction_type, reactor_type, num_reactions):
    media_id = Video_Extractid(url)  # Function to extract the media ID (photo or video)
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        try:
                            if not has_reacted(media_id, page_access_token):
                                url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                                params = {'access_token': page_access_token, 'type': reaction_type}
                                response = requests.post(url, params=params)

                                if response.status_code == 200:
                                    reactions_count += 1
                                    print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, media_id, str(response.json())))
                                    if reactions_count >= num_reactions:
                                        print("Reached the limit of {} reactions.".format(num_reactions))
                                        return
                                else:
                                    print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                        except requests.exceptions.RequestException as error:
                            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
                elif reactor_type == "ACCOUNT":
                    try:
                        if not has_reacted(media_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
                elif reactor_type == "BOTH":
                    try:
                        if not has_reacted(media_id, access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
            else:
                print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        except requests.exceptions.RequestException as error:
            print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# perform_reaction_media('https://example.com/video_or_photo_url', 'LIKE', 'BOTH', 10)

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_reaction_media_fast(url, reaction_type, reactor_type, num_reactions):
    media_id = Video_Extractid(url)  # Function to extract the media ID (photo or video)
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    def react_with_token(access_token, reactor_type):
        nonlocal reactions_count
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                
                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    page_name = page.get('name', '')
                    try:
                        if not has_reacted(media_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)

                            if response.status_code == 200:
                                reactions_count += 1
                                print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {}\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(page_name, media_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    print("Reached the limit of {} reactions.".format(num_reactions))
                                    return True
                            else:
                                print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                    except requests.exceptions.RequestException as error:
                        print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                        
            elif reactor_type == "ACCOUNT":
                try:
                    if not has_reacted(media_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
                            print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                print("Reached the limit of {} reactions.".format(num_reactions))
                                return True
                        else:
                            print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                except requests.exceptions.RequestException as error:
                    print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
                    
            elif reactor_type == "BOTH":
                try:
                    if not has_reacted(media_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
                            print("\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m Personal Profile\033[0m \033[1m|\033[91m {}\033[0m \033[1m|\033[90m {}\033[0m".format(media_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                print("Reached the limit of {} reactions.".format(num_reactions))
                                return True
                        else:
                            print("\033[1;91m[ERROR]\033[0;1m FAILED TO POST REACTION | \033[91m{}\033[0m".format(media_id))
                except requests.exceptions.RequestException as error:
                    print("\033[1;91m[EXCEPTION]\033[0;1m {}\033[0m".format(error))
        else:
            print("\033[1;91m[ERROR]\033[0;1m Invalid access token format\033[0m")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = []
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
            futures.append(executor.submit(react_with_token, access_token, reactor_type))

        for future in as_completed(futures):
            if reactions_count >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# perform_reaction_media('https://example.com/video_or_photo_url', 'LIKE', 'BOTH', 10)
import requests

def like_profile_cover(url, reaction_type, num_reactions):
    media_id = Video_Extractid(url)  # Replace with your function to extract media ID
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if not has_reacted(media_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                    params = {'access_token': access_token, 'type': reaction_type}
                    response = requests.post(url, params=params)

                    if response.status_code == 200:
                        reactions_count += 1
                        print(f"Successfully reacted to {media_id}. Response: {response.json()}")
                        if reactions_count >= num_reactions:
                            print(f"Reached the limit of {num_reactions} reactions.")
                            return
                    else:
                        print(f"Failed to react. Status code: {response.status_code}")
            else:
                print("[ERROR] Invalid access token format")
        except requests.exceptions.RequestException as error:
            print(f"[EXCEPTION] {error}")

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# like_profile_cover('https://example.com/profile_cover_url', 'LIKE', 10)
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def like_profile_cover_fast(url, reaction_type, num_reactions):
    media_id = Video_Extractid(url)  # Replace with your function to extract media ID
    if not media_id:
        print("[ERROR] Invalid URL or unable to extract media ID.")
        return

    access_tokens_data = load_data()  # Load your access tokens
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])

reactions_count = 0

    def react_with_token(access_token):
        nonlocal reactions_count
        
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if not has_reacted(media_id, access_token):
                url = f'https://graph.facebook.com/v18.0/{media_id}/reactions'
                params = {'access_token': access_token, 'type': reaction_type}
                response = requests.post(url, params=params)

                if response.status_code == 200:
                    reactions_count += 1
                    print(f"Successfully reacted to {media_id}. Response: {response.json()}")
                    if reactions_count >= num_reactions:
                        return True
                else:
                    print(f"Failed to react. Status code: {response.status_code}")
        else:
            print("[ERROR] Invalid access token format")
        
        return False

    with ThreadPoolExecutor(max_workers=2000) as executor:
        futures = {executor.submit(react_with_token, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info): token_info for token_info in access_tokens}
        
        for future in as_completed(futures):
            if reactions_count >= num_reactions:
                print(f"Reached the limit of {num_reactions} reactions.")
                break

    print(f"Total reactions sent: {reactions_count}")

# Example usage
# like_profile_cover('https://example.com/profile_cover_url', 'LIKE', 10)

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def react_with_token_video(post_id, access_token, reaction_type, reactor_type):
    reactions_count = 0
    try:
        if access_token.startswith("EA") or access_token.startswith("EAA"):
            if reactor_type == "PAGE":
                response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                for page in response.get('data', []):
                    page_access_token = page.get('access_token', '')
                    if not has_reacted(post_id, page_access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': page_access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)

                        if response.status_code == 200:
                            reactions_count += 1
            elif reactor_type in ["ACCOUNT", "BOTH"]:
                if not has_reacted(post_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    params = {'access_token': access_token, 'type': reaction_type}
                    response = requests.post(url, params=params)

                    if response.status_code == 200:
                        reactions_count += 1

    except requests.exceptions.RequestException:
        pass

    return reactions_count

def perform_reaction_video_fast(url, reaction_type, reactor_type, num_reactions):
    
    post_id = Video_Extractid(url)
    if not post_id:
        print("[ERROR] Invalid URL or unable to extract post ID.")
        return

    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    total_reactions = 0
    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {executor.submit(react_with_token_video, post_id, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info, reaction_type, reactor_type): token_info for token_info in access_tokens}

        for future in as_completed(future_to_token):
            token_info = future_to_token[future]
            try:
                result = future.result()
                total_reactions += result
                if total_reactions >= num_reactions:
                    print(f"Reached the limit of {num_reactions} reactions.")
                    return
            except Exception as exc:
                print(f'Token {token_info} generated an exception: {exc}')

    print(f"Completed processing with {total_reactions} reactions.")
    main()

# Call the function as needed
# perform_reaction_video(url, reaction_type, reactor_type, num_reactions)

def remove(post_id):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])

    reactions_count = 0

    def remove_reaction_with_token(access_token):
        nonlocal reactions_count
        results = []
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if has_reacted(post_id, access_token):
                    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                    headers = {'Authorization': f'Bearer {access_token}'}
                    params = {'type': 'NONE'}  # Adjust if needed
                    response = requests.delete(url, headers=headers, params=params)

                    if response.status_code == 200:
                        reactions_count += 1
                        results.append(f"SUCCESSFULLY REMOVED REACTION | {post_id} | {response.json()}")
                    else:
                        results.append(f"FAILED TO REMOVE REACTION | {post_id}")
        except requests.exceptions.RequestException as error:
            results.append(f"EXCEPTION: {error}")
        return results

    with ThreadPoolExecutor(max_workers=2000) as executor:
        future_to_token = {executor.submit(remove_reaction_with_token, token_info.get("access_token", "") if isinstance(token_info, dict) else token_info): token_info for token_info in access_tokens}

        for future in as_completed(future_to_token):
            token_info = future_to_token[future]
            try:
                results = future.result()
                for result in results:
                    print(result)
            except Exception as exc:
                print(f'Token {token_info} generated an exception: {exc}')

    print(f"Completed processing with {reactions_count} reactions removed.")
def extract_ids(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
def extract_ids_grouppage(url):
    # Define patterns for different types of Facebook posts
    group_permalink_pattern = r'groups/([^/]+)/permalink/(\d+)/'
    group_post_pattern = r'groups/([^/]+)/posts/(\d+)/'
    user_post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'
    story_fbid_pattern = r'story_fbid=(\d+)&id=(\d+)'

    # Search for matches in the URL
    group_permalink_match = re.search(group_permalink_pattern, url)
    group_post_match = re.search(group_post_pattern, url)
    user_post_match = re.search(user_post_pattern, url)
    photo_match = re.search(photo_pattern, url)
    story_fbid_match = re.search(story_fbid_pattern, url)

    # Check for matches and extract IDs
    if group_permalink_match:
        group_id, post_id = group_permalink_match.groups()
        return f"{group_id}_{post_id}"
    elif group_post_match:
        group_id, post_id = group_post_match.groups()
        return f"{group_id}_{post_id}"
    elif user_post_match:
        user_id, post_id = user_post_match.groups()
        return f"{user_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    elif story_fbid_match:
        post_id, user_id = story_fbid_match.groups()
        return f"{user_id}_{post_id}"
    else:
        return None
def has_reacted(post_id, access_token):
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        reactions = response.json().get('data', [])
        
        # Get the id of the user/page associated with the access token
        user_info = requests.get('https://graph.facebook.com/me', params={'access_token': access_token}).json()
        user_id = user_info.get('id', '')
        
        for reaction in reactions:
            if reaction.get('id') == user_id:
                return True
        
    except requests.exceptions.RequestException:
        pass

    
    return False

def has_commented(post_id, access_token):
    try:
        url = f'https://graph.facebook.com/v18.0/{post_id}/comments'
        params = {'access_token': access_token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        comments = response.json().get('data', [])
        
        # Get the id of the user/page associated with the access token
        user_info = requests.get('https://graph.facebook.com/me', params={'access_token': access_token}).json()
        user_id = user_info.get('id', '')
        
        for comment in comments:
            if comment.get('from', {}).get('id') == user_id:
                return True
        
    except requests.exceptions.RequestException:
        pass
    
    return False



import requests
from concurrent.futures import ThreadPoolExecutor

def send_reaction(post_id, access_token, reaction_type):
    """Send a reaction to a post using a specific access token."""
    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
    params = {'access_token': access_token, 'type': reaction_type}
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json(), True
        else:
            return None, False
    except requests.exceptions.RequestException:
        return None, False

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_reaction(post_id, access_token, reaction_type):
    """Send a reaction to a post using a specific access token."""
    url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
    params = {'access_token': access_token, 'type': reaction_type}
    
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json(), True
        else:
            return None, False
    except requests.exceptions.RequestException:
        return None, False

def perform_reaction_fast(post_id, reaction_type, reactor_type, num_reactions):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0
    tasks = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        for token_info in access_tokens:
            access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type in ["PAGE", "BOTH"]:
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        page_name = page.get('name', '')
                        if not has_reacted(post_id, page_access_token):
                            future = executor.submit(send_reaction, post_id, page_access_token, reaction_type)
                            tasks.append((future, page_name))
                
                if reactor_type in ["ACCOUNT", "BOTH"]:
                    if not has_reacted(post_id, access_token):
                        future = executor.submit(send_reaction, post_id, access_token, reaction_type)
                        tasks.append((future, "Personal Profile"))

        # Process the results as they complete
        for future, name in as_completed(tasks):
            result, success = future.result()
            if success:
                reactions_count += 1
                print(f"\033[0m\033[1m[\033[91mSUCCESS\033[0m\033[1m] SUCCESSFULLY REACTED |\033[91m {name}\033[0m \033[1m|\033[91m {post_id}\033[0m \033[1m|\033[90m {result}\033[0m")
                if reactions_count >= num_reactions:
                    print(f"Reached the limit of {num_reactions} reactions.")
                    break  # Exit early if the reaction limit is reached

    print(f"Total reactions made: {reactions_count}")



def perform_reaction(post_id, reaction_type, reactor_type, num_reactions):
    access_tokens_data = load_data()
    access_tokens = access_tokens_data if isinstance(access_tokens_data, list) else access_tokens_data.get("access_tokens", [])
    
    reactions_count = 0

    for token_info in access_tokens:
        access_token = token_info.get("access_token", "") if isinstance(token_info, dict) else token_info
        try:
            if access_token.startswith("EA") or access_token.startswith("EAA"):
                if reactor_type == "PAGE":
                    response = requests.get(f'https://graph.facebook.com/me/accounts', headers={'Authorization': f'Bearer {access_token}'}).json()
                    
                    for page in response.get('data', []):
                        page_access_token = page.get('access_token', '')
                        if not has_reacted(post_id, page_access_token):
                            url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                            params = {'access_token': page_access_token, 'type': reaction_type}
                            response = requests.post(url, params=params)
                            
                            if response.status_code == 200:
                                reactions_count += 1
                                print("[SUCCESS] SUCCESSFULLY REACTION | {} | {} | {}".format(page.get('name', ''), post_id, str(response.json())))
                                if reactions_count >= num_reactions:
                                    return

                elif reactor_type == "ACCOUNT":
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)
                        
                        if response.status_code == 200:
                            reactions_count += 1
                            print("[SUCCESS] SUCCESSFULLY REACTED | Personal Profile | {} | {}".format(post_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                return

                elif reactor_type == "BOTH":
                    if not has_reacted(post_id, access_token):
                        url = f'https://graph.facebook.com/v18.0/{post_id}/reactions'
                        params = {'access_token': access_token, 'type': reaction_type}
                        response = requests.post(url, params=params)
                        
                        if response.status_code == 200:
                            reactions_count += 1
                            print("[SUCCESS] SUCCESSFULLY REACTED | Personal Profile | {} | {}".format(post_id, str(response.json())))
                            if reactions_count >= num_reactions:
                                return
            else:
                # You may choose to log invalid tokens in a different way if needed
                continue
        except requests.exceptions.RequestException as error:
            continue  # Handle exceptions silently






      
def extract_facebook_id(url):
    # Define the regular expression pattern to match the Facebook URL format
    pattern = r'https?://(?:www\.)?facebook\.com/([0-9]+)'
    
    # Use re.match to find the pattern in the URL
    match = re.match(pattern, url)
    
    # If a match is found, return the extracted ID
    if match:
        return match.group(1)
    else:
        return None 
def EAAA():
    while True:
        username = input(f'{color.BOLD}[✦] Phone Number/Email/ID: {color.END}')
        if username == '0':
            return  # exit the function if the user types 0
        password = input(f'{color.BOLD}[✦] Password: {color.END}')
        url = (f"https://b-api.facebook.com/method/auth.login?format=json&device_id=0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
               f"&email={username}&password={password}&cpl=true&family_device_id=0ksqyflb-tnnh-aaag-j5si-gqof920ps1lo"
               "&sim_serials=%5B%2289014103310593510720%22%5D&credentials_type=password&error_detail_type=button_with_disabled"
               "&locale=en_US&client_country_code=US&method=auth.login&fb_api_req_friendly_name=authenticate"
               "&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662")
        
        try:
            response = requests.get(url)
            responses = response.json()
            if 'access_token' in responses:
                print(responses['access_token'])
                # Add the retrieved token directly
                data = load_data()
                access_tokens = data.get("access_tokens", [])
                if any(token.get("access_token") == responses['access_token'] for token in access_tokens):
                    print("Token already exists.")
                else:
                    access_tokens.append({"access_token": responses['access_token']})
                    data["access_tokens"] = access_tokens
                    save_data(data)
                    print(f"{color.RED}Successfully added Account{color.END}")
            else:
                print(responses.get('error_msg', 'Unknown error occurred'))
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")

import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def follow_page(page, account_id):
    page_access_token = page.get('access_token', '')
    page_name = page.get('name', '')
    
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers',
            headers={'Authorization': f'Bearer {page_access_token}'}
        )
        
        if response.status_code == 200:
            return f'{page_name} \033[1;31mSuccess following account \033[1;32m {account_id}'
        else:
            return f'Failed to follow account {account_id} from page {page_name}: {response.text}'
    except requests.exceptions.RequestException as error:
        return f'Error with page {page_name}: {error}'
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def load_tokens(file_path='Eaau.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [token_data['access_token'] for token_data in data['access_tokens']]

def follow_account(page_access_token, account_id):
    """Follow an account using a specific page access token."""
    try:
        response = requests.post(
            f'https://graph.facebook.com/v18.0/{account_id}/subscribers
