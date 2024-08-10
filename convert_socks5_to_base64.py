import base64
import json

# Path to your SOCKS5 proxy list file
proxy_file = "socks5.txt"

# Path to the output file
output_file = "socks5_base64.txt"

# Initialize a list to hold base64 strings
base64_proxies = []

# Read the proxy list from the file
with open(proxy_file, "r") as file:
    for line in file:
        # Split IP and Port
        address, port = line.strip().split(":")
        
        # Create the JSON structure
        proxy_json = {
            "protocol": "socks",
            "settings": {
                "servers": [
                    {
                        "address": address,
                        "port": int(port)
                    }
                ]
            }
        }
        
        # Convert JSON to string and encode as base64
        proxy_str = json.dumps(proxy_json)
        proxy_base64 = base64.b64encode(proxy_str.encode()).decode()
        
        # Add the base64 string to the list
        base64_proxies.append(proxy_base64)

# Write all base64 strings to the output file
with open(output_file, "w") as file:
    for proxy in base64_proxies:
        file.write(proxy + "\n")

print(f"Base64 encoded proxies saved to {output_file}")
