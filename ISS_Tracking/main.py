import requests
from datetime import datetime, timezone
import smtplib
from email.mime.text import MIMEText


########### ___Track ISS___ ###########
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
# print(f"ISS Location: {iss_longitude}, {iss_latitude}")



##########___Email____Cred_____##############
EMAIL = "your_email@example.com"    # Your email address
PASSWORD = "your_app_password"       # Your app-specific password (search for 'Google app password' if needed)
SERVER = "smtp.gmail.com"             # SMTP server (ex :  Gmail)
PORT = 587                             # SMTP port (ex:  Gmail)
FROM_EMAIL = EMAIL                       # Sender email (same as your email)
TO_EMAIL = "destination_email@example.com" # Recipient's email address
SUBJECT = "ISS Tracker"                      # Email subject



###########_____Get My  Location_____#################


MY_LAT = "Your latitude"     #######____Change this_____####     !!!!
MY_LNG = "Your longitude"   #######____Change this_____####      !!!!

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# Compare the location of ISS to check if it's close
def is_close_to_me(iss_long, iss_lat):
    return abs(iss_long - MY_LNG) < 5 and abs(iss_lat - MY_LAT) < 5

# Check if it is night
def is_night(sunrise, sunset):
    time_now_utc = datetime.now(timezone.utc).hour
    return time_now_utc >= sunset or time_now_utc < sunrise

# print(is_night(sunrise, sunset))

#########_____Sending email if ISS is visible_____####
msg = MIMEText("You can see the ISS ")
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = SUBJECT


if is_close_to_me(iss_longitude, iss_latitude) and is_night(sunrise, sunset):
    try:
        with smtplib.SMTP(SERVER, PORT) as server:
            server.ehlo()  
            server.starttls() 
            server.login(EMAIL, PASSWORD) 
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())  
            print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[-] An error occurred: {e}")
else:
    print("Wait!")

