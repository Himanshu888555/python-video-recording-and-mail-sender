import smtplib
content ='hello parth go out and fuck yourself'
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('youremail888555@gmail.com','your password please')
header = 'To:' + 'yourfriendgoel06@gmail.com' + '\n' + 'From:' \
         + 'yourmail888555@gmail.com' + '\n' + 'Subject:babyhackmeplease\n'
content=header+content
mail.sendmail('yourmail888555@gmail.com','yourfriendgoel06@gmail.com',content)
mail.close()
