import smtplib, ssl

def sendMail(msg):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'rnvish143@gmal.com'
    password = 'cslihmcwdmntyaii'
    receiver_email = 'rkvsk73@gmail.com'
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()