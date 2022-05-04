import smtplib
from email.message import EmailMessage
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 메일 주소가 아닙니다.")


message = EmailMessage()
message.set_content("본문 \n 5주차 과제 \n practice4 \n 메일 보내기") #본문
message["Subject"] = "10기 김현정입니다." #제목
message["From"] = "byoridari605@gmail.com"
message["To"] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("byoridari605@gmail.com","#######")
#보안 상의 문제로 비밀번호를 안보이게 했습니다.
sendEmail("ksjoon28@naver.com")
smtp.quit()