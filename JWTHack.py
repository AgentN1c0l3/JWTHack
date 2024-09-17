import jwt
import json
import requests

# ANSI escape codes for colors
RESET = "\033[0m"
BLUE = "\033[34m"

class JWTHandler:
    def __init__(self, jwt_token):
        self.jwt_token = jwt_token

    def decode(self):
        try:
            header = jwt.get_unverified_header(self.jwt_token)
            payload = jwt.decode(self.jwt_token, options={"verify_signature": False})
            return header, payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.DecodeError:
            raise ValueError("Invalid token.")
        except Exception as e:
            raise Exception(f"Error: {e}")

    def validate(self, secret):
        try:
            decoded = jwt.decode(self.jwt_token, secret, algorithms=["HS256", "RS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token.")
        except Exception as e:
            raise Exception(f"Error: {e}")

    def make_request(self, url):
        headers = {"Authorization": f"Bearer {self.jwt_token}"}
        try:
            response = requests.get(url, headers=headers)
            return response.status_code, response.text
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")

def display_menu():
    print(f"""
{BLUE}               +   .                .   . .     .  .{RESET}
{BLUE}                   .                    .       .     *{RESET}
{BLUE}  .       *                        . . . .  .   .  + .{RESET}
{BLUE}            "You Are Here"            .   .  +  . . .{RESET}
{BLUE} .                 |             .  .   .    .    . .{RESET}
{BLUE}                  |           .     .     . +.    +  .{RESET}
{BLUE}                 \|/            .       .   . .{RESET}
{BLUE}        . .       V          .    * . . .  .  +   .{RESET}
{BLUE}           +      .           .   .      +{RESET}
{BLUE}                            .       . +  .+. .{RESET}
{BLUE}  .                      .     . + .  . .     .      .{RESET}
{BLUE}           .      .    .     . .   . . .        ! /{RESET}
{BLUE}      *             .    . .  +    .  .       - O -{RESET}
{BLUE}          .     .    .  +   . .  *  .       . / |{RESET}
{BLUE}               . + .  .  .  .. +  .{RESET}
{BLUE} .      .  .  .  *   .  *  . +..  .            *{RESET}
{BLUE} .      .   . .   .   .   . .  +   .    .            +{RESET}
                    Made by AgentN1c0l3
    """)
    print("\033[31mAll it takes is a little push… to crack the truth.😜\033[0m")

def main():
    display_menu()
    print("\nChoose an action:")
    print("1. Decode JWT header and payload")
    print("2. Validate JWT with secret/public key")
    print("3. Make an HTTP request with JWT as Authorization header")
    
    try:
        choice = int(input("\nEnter your choice (1-3): "))
        jwt_token = input("\nEnter the JWT token: ")
        jwt_handler = JWTHandler(jwt_token)

        if choice == 1:
            header, payload = jwt_handler.decode()
            print("\n[+] JWT Header:")
            print(json.dumps(header, indent=4))
            print("\n[+] JWT Payload:")
            print(json.dumps(payload, indent=4))
        elif choice == 2:
            secret = input("Enter the secret or public key: ")
            decoded_payload = jwt_handler.validate(secret)
            print("\n[+] JWT is valid. Payload:")
            print(json.dumps(decoded_payload, indent=4))
        elif choice == 3:
            url = input("Enter the URL: ")
            status_code, response_text = jwt_handler.make_request(url)
            print(f"\n[+] Response status code: {status_code}")
            print(f"[+] Response body:\n{response_text}")
        else:
            print("[!] Invalid choice.")
    except ValueError as ve:
        print(f"[!] {ve}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
