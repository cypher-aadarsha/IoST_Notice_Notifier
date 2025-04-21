import requests
from bs4 import BeautifulSoup
from nepali_datetime import date as nep_date
import smtplib
from email.mime.text import MIMEText
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Function to convert English numbers to Nepali numbers (if needed)
def convert_to_nepali_num(eng_num_str):
    mapping = {
        '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
        '5': '५', '6': '६', '7': '७', '8': '८', '9': '९',
        '10': '१०', '11': '११', '12': '१२', '13': '१३',
        '14': '१४', '15': '१५', '16': '१६', '17': '१७',
        '18': '१८', '19': '१९', '20': '२०', '21': '२१',
        '22': '२२', '23': '२३', '24': '२४', '25': '२५',
        '26': '२६', '27': '२७', '28': '२८', '29': '२९',
        '30': '३०', '31': '३१'
    }
    return ''.join(mapping.get(ch, ch) for ch in str(eng_num_str))
# Get today's Nepali date
today_nep_date = nep_date.today().strftime('%-d %B')  # e.g., "८ बैशाख"
print(f"🔍 Today's Nepali date we're looking for: '{today_nep_date}'")

# Request page
url = 'https://iost.tu.edu.np/notices'
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all notices
notices = soup.find_all('div', class_='notice-listing')

new_notices = []

# Collect notices from today
for notice in notices:
    nepali_date = notice.find('div', class_='date-nep').text.strip()
    title = notice.find('h3').text.strip()
    print(f"📅 Found notice: '{title}' on date: '{nepali_date}'")

    if nepali_date == today_nep_date:
        new_notices.append(title)
# Load last seen notices
try:
    with open('last_notice.txt', 'r', encoding='utf-8') as f:
        last_seen = f.read().splitlines()
except FileNotFoundError:
    last_seen = []

# Filter truly new notices
fresh_notices = [n for n in new_notices if n not in last_seen]

# Compose email content
if fresh_notices:
    content = "📢 New IoST Notices Today:\n\n" + "\n".join(f"- {n}" for n in fresh_notices) + f"\n\nVisit: {url}"
    subject = "📢 New IoST Notice Alert!"
else:
    content = f"📭 Stay tuned!\nNo new notices were posted today ({today_nep_date}) on the IoST website.\n\nVisit: {url}"
    subject = "📢 IoST Notice Update"

# Debug: print email content before sending
print("----- Email Content -----")
print(content)
print("-------------------------")

# Prepare and send email
msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = 'jha.aadarsha2060@gmail.com'
msg['To'] = '023bscit050@sxc.edu.np'

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login('jha.aadarsha2060@gmail.com', 'qdzc tagd zkzj mawx')  # App password
    server.send_message(msg)

print("✅ Email sent successfully.")

# Update the last seen file only if new notices found
if fresh_notices:
    with open('last_notice.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(new_notices))
