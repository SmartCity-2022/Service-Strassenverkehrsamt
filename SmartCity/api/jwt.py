import jwt
import datetime
import urllib3


JWT_SECRET = None


def read_payload(request):
    return jwt.decode(request.cookies.get("accessToken"), JWT_SECRET, algorithms=["HS256"])


def verify(request):
    access = request.cookies.get("accessToken")
    refresh = request.cookies.get("refreshToken")
    
    if refresh is None or access is None:
        return False
    
    try:
        access_payload = jwt.decode(access, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        try:
            http = urllib3.PoolManager()
            token = http.request("POST",
                                configParser.get("misc", "mainhub_url") + "/token", {"token": refresh})
            request.cookies.__setattr__("accessToken", token)
            refresh_decode = jwt.decode(token, os.environ.get("SECRET"), algorithms=["HS256"])
            request.state.email = refresh_decode.get("email")
        except:
            return False
    return True