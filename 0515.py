import os
import sys
import urllib.request
client_id = "NrkKI0dzkjbVyJJaGGg1"
client_secret = "bxP7XUH_Sh"
encText = urllib.parse.quote("사랑")
#url = "https://openapi.naver.com/v1/search/book.xml?display=10&start=1&query=" + encText # xml 결과
url = "http://data.ex.co.kr/exopenapi/business/representFoodServiceArea?serviceKey=XUB6tuBsVYatI3IFyS3yqkaAu8TrQx2SAYE%2FjJOKeMBU7EE6E8CerMZALvZQ1v7W4ZGdy6y2y%2FWQFiBS9qBf3A%3D%3D&type=xml"
request = urllib.request.Request(url)
#request.add_header("X-Naver-Client-Id",client_id)
#request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)