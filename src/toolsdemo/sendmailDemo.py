# -*- coding: utf-8 -*-
import smtplib

TO = "20532486@qq.com"
FROM = "11243253@qq.com"
PSW = "xiaowensheng1981"
Serveraddr = "smtp.qq.com"
msg = ["From: %s"% FROM,
       "To: %s"% TO,
       "Subject: just for test"]

smtp = smtplib.SMTP()
smtp.connect(Serveraddr, 25)
smtp.login("11243253@qq.com", PSW)
smtp.sendmail(FROM, TO, '\r\n'.join(msg))
print ("Done")
smtp.quit()