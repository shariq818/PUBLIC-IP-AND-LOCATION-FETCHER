# Public IP & Location Fetcher v1.1 (Interactive)
# Author: Paradox (shariq818)

import requests

def get_location_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        return requests.get(url).json()
    except:
        return None

def main():
    print("=== Public IP & Location Fetcher v1.1 ===")
    print("Press ENTER to auto-detect your IP\n")

    user_ip = input("Enter an IP address (optional): ").strip()

    # Auto-detect
    if user_ip == "":
        print("\nDetecting your public IP...")
        try:
            user_ip = requests.get("https://api.ipify.org").text
            print(f"Detected IP: {user_ip}")
        except:
            print("Error: Could not detect IP")
            return

    print("\nFetching location info...")
    info = get_location_info(user_ip)

    if not info or info.get("status") != "success":
        print("Error: Could not retrieve location details.")
        return

    result = (
        f"IP Address: {user_ip}\n"
        f"Country: {info['country']}\n"
        f"Region: {info['regionName']}\n"
        f"City: {info['city']}\n"
        f"ISP: {info['isp']}\n"
        f"Timezone: {info['timezone']}\n"
    )

    with open("ip_info.txt", "w") as f:
        f.write(result)

    print("\nScan complete! Saved as ip_info.txt")

if __name__ == "__main__":
    main()