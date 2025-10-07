# HeaderHunter
import requests

SEC_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def get_headers(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("❌ URL'e erişilemedi.")
        return []

    headers = []
    for header in SEC_HEADERS:
        if header in response.headers:
            headers.append((header, response.headers[header]))
            print("[+] Header %s: %s" % (header, response.headers[header]))
        else:
            print("[-] Header %s: Bulunamadı" % header)

    return headers

if __name__ == "__main__":
    url = input("Enter URL: ").strip()
    get_headers(url)
