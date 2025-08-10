# ISS Tracker Script 🚀

This Python script tracks the International Space Station (ISS) and sends an email notification when the ISS is visible from your location during the night. It uses public APIs to fetch the ISS location and sunrise/sunset times and an SMTP server to send email alerts.

## Features ✨

- **Track ISS Location**: Fetches real-time latitude and longitude of the ISS.
- **Check Visibility**: Verifies if the ISS is close to your location.
- **Nighttime Detection**: Checks if it’s dark at your location.
- **Email Alerts**: Sends an email notification if the ISS is visible.

## How It Works 🛠️

1. The script uses the [Open Notify API](http://api.open-notify.org/) to fetch the real-time location of the ISS.
2. Your current location's sunrise and sunset times are retrieved using the [Sunrise Sunset API](https://sunrise-sunset.org/api).
3. If the ISS is within 5 degrees of your location **and** it’s nighttime, an email notification is sent to you.

---

## Prerequisites 📋

Before running the script, ensure you have:

1. Python installed on your system.
2. The following Python libraries installed:
   - `requests`
   - `smtplib`
   - `email`
3. An email account (e.g., Gmail) with an app-specific password for SMTP.

---

## Setup 🛠️

1. Clone or download the script.
2. Update the following placeholders in the script:
   - `EMAIL`: Your email address.
   - `PASSWORD`: Your app-specific email password (e.g., for Gmail, search for "Google app password").
   - `MY_LAT`: Your latitude.
   - `MY_LNG`: Your longitude.
   - `TO_EMAIL`: The recipient's email address.

Example values:
```python
EMAIL = "your_email@example.com"
PASSWORD = "your_app_password"
MY_LAT = 37.7749  # Example: San Francisco latitude
MY_LNG = -122.4194  # Example: San Francisco longitude
TO_EMAIL = "recipient_email@example.com"
