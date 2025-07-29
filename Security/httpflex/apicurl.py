import argparse
import requests as r




parser = argparse.ArgumentParser()
parser.add_argument( "-u", "--url", required=True, help="sets the url" )
parser.add_argument( "-m", "--method", choices=["GET", "POST", "DELETE", "PUT", "OPTIONS" ], default="GET", help="HTTP method to use")
parser.add_argument( "-d", "--data", help="provide data for a post request")
parser.add_argument( "-c", "--cookie", help="add cookies in key=value;key2=value2 format")
parser.add_argument( "-he", "--header", help="add a header to the request")
parser.add_argument( "-v", "--verbosity", type=int, choices=[0, 1, 2, 3],help="Set verbosity level (0-3)")
parser.add_argument( "-t", "--timeout", type=int, default=10, help="Request timeout in seconds")
args = parser.parse_args()

    
# Handle optional cookies
cookies = None
if args.cookie and args.cookie.strip():
    cookies = dict(item.strip().split("=", 1) for item in args.cookie.split(";") if "=" in item)

# Handle optional headers
headers = None
if args.header and args.header.strip():
    headers = dict(item.strip().split(":", 1) for item in args.header.split(";") if ":" in item)

verbosity = args.verbosity if args.verbosity is not None else 0
try:    
    if args.method == "POST":
        request = r.post(args.url, data=args.data, headers=headers, cookies=cookies, timeout=args.timeout)
    elif args.method == "PUT":
        request = r.put(args.url, data=args.data, headers=headers, cookies=cookies, timeout=args.timeout)
    elif args.method == "DELETE":
        request = r.delete(args.url, headers=headers, cookies=cookies, timeout=args.timeout)
    elif args.method == "OPTIONS":
        request = r.options(args.url, headers=headers, cookies=cookies, timeout=args.timeout)
    else:
        request = r.get(args.url, headers=headers, cookies=cookies, timeout=args.timeout) 
    
        
    if args.verbosity == 0:
        print(f"Status Response Code: {request.status_code}")
    elif args.verbosity == 1:
        print(f"Status Response Code: {request.status_code}")
        print(f"Cookie: {request.cookies}")
    elif args.verbosity == 2:
        print(f"Status Response Code: {request.status_code}")
        print(f"Cookie: {request.cookies}")
        print(f"Headers: {request.headers}")
    else:
        print(f"Status Response Code: {request.status_code}")
        print(f"Cookie: {request.cookies}")
        print(f"Headers: {request.headers}")
        try:
            print(f"Body: (JSON) {request.json()}")
        except:
            print(f"Body: (TEXT) {request.text}")
# except:
#     print("invalid, please provide a url")

except r.exceptions.RequestException as e:
    print(f"[!] Request error: {e}")
except Exception as e:
    print(f"[!] Unexpected error: {e}")