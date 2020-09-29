def sendemail():
    import smtplib,ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.utils import formatdate
    from email import encoders
    msg = MIMEMultipart()
    msg['From'] = ''
    msg['To'] = ''
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = 'Sentimental Analysis internship output report'
    msg.attach(MIMEText('Output Report'))
  
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("test.pptx", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="test.pptx"')
    msg.attach(part)
  
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login('', '')
    smtp.sendmail('', '', msg.as_string())
    smtp.quit()