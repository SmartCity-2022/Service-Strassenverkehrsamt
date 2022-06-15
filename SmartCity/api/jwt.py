import jwt
import datetime
import urllib3


JWT_SECRET = "1"


def read_payload(request):
    return jwt.decode(request.COOKIES.get("accessToken"), JWT_SECRET, algorithms=["HS256"])


def verify(request):
    access = request.COOKIES.get("accessToken")
    refresh = request.COOKIES.get("refreshToken")
    
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