# 📢 IoST Notice Notifier

This Python script automatically checks the [Institute of Science and Technology (IoST), Tribhuvan University](https://iost.tu.edu.np/notices) notice board for new notices and sends an email notification if a new notice is posted **on the same date**.

If no new notice is found for the current day, it sends a friendly email saying _"Stay tuned, no new notices found."_ ☕

---

## 💡 Features

- Scrapes the IoST official notice board
- Compares today's date with the latest notice
- Sends email notification using Gmail SMTP
- Saves the last seen notice to avoid duplicates
- Can be converted to `.exe` and added to **Windows startup**

---

## 🔧 Setup

### 1. Clone the Repository
git clone https://github.com/cypher-aadarsha/iost-notice-notifier.git
cd iost-notice-notifier

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

Please make sure to update tests as appropriate.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
``` 
### 3. Configure Email Settings
Edit the `config.py` file to set your email and password:

```python

### ✅ Output Example
📬 If a new notice is posted today:

Subject: 📢 New IoST Notice Alert!
Body: New notice posted: "Exam Schedule for BSc CSIT 5th Semester"
Check it at: https://iost.tu.edu.np/notices

⏳ If no new notice is posted today:

Subject: 📢 IoST Notice Update
Body: Stay tuned! No new notices found for today.


