import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# URL of the IoST notices page
url = 'https://iost.tu.edu.np/notices'

# Fetch the page (skip SSL verification for now)
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all notice blocks
notices = soup.find_all('div', class_='views-row')

# Get today's date
today = datetime.today().strftime('%B %d, %Y')  # e.g., April 21, 2025

found_new_notice = False
new_notice_title = None

# Check if any notice was posted today
for notice in notices:
    date_div = notice.find('span', class_='date-display-single')
    title_tag = notice.find('h3')

    if date_div and today in date_div.text:
        new_notice_title = title_tag.text.strip()
        found_new_notice = True
        break

# Prepare email message
if found_new_notice:
    subject = '📢 New IoST Notice Alert!'
    body = f'New notice posted today ({today}): {new_notice_title}\nCheck it at: {url}'
else:
    subject = '📭 No New IoST Notices Today'
    body = f'Stay tuned! As of {today}, no new notices were posted.\nVisit: {url} to check manually.'

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = 'yourgmail@gmail.com'
msg['To'] = 'yourgmail@gmail.com'

# Send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('yourgmail@gmail.com', '#### #### #### ####')  # App password
    server.send_message(msg)

print("✅ Email sent successfully.")
