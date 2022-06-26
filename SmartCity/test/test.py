import requests
import json
import configparser
import jwt

configParser = configparser.RawConfigParser()
configParser.read("./test.cfg")
host = configParser["backend-connection"]["backend_url"]


# Credentials for user 'test@gmail.com'
accessToken = jwt.encode({"email": "test@email.com"}, "1", algorithm="HS256")
refreshToken = jwt.encode({"email": "test@email.com"}, "1", algorithm="HS256")
cookies = {
    "accessToken": accessToken,
    "refreshToken": refreshToken
}


def test_vehicles():
    # Calling the page for first time, expect status code 200 OK
    vehicles_startup = requests.get(host + "/vehicle/user/", cookies=cookies)
    assert (vehicles_startup.status_code == 200)
    
    # Register a new vehicle
    vehicle = {
        "brand": "Fiat",
        "model": "Multipla",
        "firstregistration": "2012-04-23T18:25:43.511Z",
        "displacement": 1834,
        "fueltype": "Benzin",
        "emissions": 120,
        "hudeadline": "2012-04-23T18:25:43.511Z",
        "licenseplate": "MI:MI:1234"
    }
    vehicle_post = requests.post(host + "/vehicle/create", cookies=cookies, json=vehicle)
    assert (vehicle_post.status_code == 200)
    
    # Check if new vehicle exists
    vehicle_afterpost = requests.get(host + "/vehicle/user/", cookies=cookies)
    assert (vehicle_afterpost.status_code == 200) and (len(vehicle_afterpost.json()) >= 1)
    
    print("[VEHICLES] All tests passed.")


def test_licenses():
    # Calling the page for first time, expect status code 200 OK
    licenses_startup = requests.get(host + "/licenserequest/user/", cookies=cookies)
    assert (licenses_startup.status_code == 200)
    
    # Create new license request
    request = {
        "licenseclass": "B"
    }
    request_post = requests.post(host + "/licenserequest/create", cookies=cookies, json=request)
    assert (request_post.status_code == 200)
    
    # Calling the page for first time, expect an empty response and status code 200 OK
    licenses_startup = requests.get(host + "/licenserequest/user/", cookies=cookies)
    assert (licenses_startup.status_code == 200) and (len(licenses_startup.json()) >= 1)
    
    print("[LICENSES] All tests passed.")
    

def test_penaltys():
    # Calling the page for first time, expect status code 200 OK
    penaltys = requests.get(host + "/penalty/user/", cookies=cookies)
    assert (penaltys.status_code == 200)
    
    # Calling the page for first time, expect status code 200 OK
    bills = requests.get(host + "/bill/user/", cookies=cookies)
    assert (bills.status_code == 200)

    print("[PENALTYS] All tests passed.")


def run_all_tests():
    test_vehicles()
    test_licenses()
    test_penaltys()


# Run all tests if module called directly
if __name__ == "__main__":
    run_all_tests()