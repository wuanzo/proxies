import json

# Define the input and output file paths
input_file = 'socks5.txt'  # Your input file with proxies in ip:port format
output_file = 'socks5_proxies.json'  # Output JSON file path

def parse_proxy_line(line):
    """Parse a proxy line in ip:port format and return a dictionary."""
    try:
        address, port = line.strip().split(':')
        return {
            "address": address,
            "port": int(port)
        }
    except ValueError:
        return None

def main():
    proxies = []

    # Read the proxy addresses from the input file
    with open(input_file, 'r') as file:
        for line in file:
            proxy_info = parse_proxy_line(line)
            if proxy_info:
                proxies.append(proxy_info)
    
    # Create the final JSON structure
    json_structure = {
        "outbounds": [
            {
                "protocol": "socks",
                "settings": {
                    "servers": [
                        {
                            "address": proxy["address"],
                            "port": proxy["port"]
                        }
                    ]
                },
                "tag": f"Proxy{index + 1}"
            }
            for index, proxy in enumerate(proxies)
        ]
    }

    # Write the JSON structure to the output file
    with open(output_file, 'w') as file:
        json.dump(json_structure, file, indent=4)

    print(f"Converted proxies have been written to {output_file}")

if __name__ == "__main__":
    main()
