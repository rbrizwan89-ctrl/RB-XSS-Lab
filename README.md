# 🚀 RB XSS Vulnerable Lab

Developed by **RB Education Hub – Cyber Security Labs** 🔥  

Cross-Site Scripting (XSS) ko samajhne ke liye ek powerful web lab.  
Isme Reflected + Stored XSS vulnerabilities dikhayi gayi hain,  
aur secure version bhi diya gaya hai.

---

## 📺 Video Tutorial

🎥 XSS lab ka detailed tutorial YouTube par aayega  
⚠️ Channel subscribe karke update le sakte ho:

👉 https://www.youtube.com/@RBEDUCATIONHUB-l5n

---

## 🧠 What You Will Learn

- Reflected XSS Attack  
- Stored XSS (Persistent) Attack  
- Input Sanitization vs `|safe` escaping difference  
- Cookie stealing & Data Exfiltration concept demo  
- Real world XSS exploitation workflow 🔥

⚠️ **Warning:**  
Ye sirf educational purpose ke liye hai.  
Real websites par bina permission XSS test ❌ **illegal** hai.

---

## 🧩 Requirements

- Python 3.8+
- Browser (Burp Suite optional)
- Flask install:

```bash
pip install flask

⚙️ Installation & Run

git clone https://github.com/rbrizwan89-ctrl/RB-XSS-Lab.git
cd RB-XSS-Lab
pip install flask
python3 app.py

✔ Lab run hoga:
http://127.0.0.1:5001/


---

🌍 Lab Routes

Feature	URL	Status

Home	/	🏠
Reflected XSS (vuln)	/search	❌ Vulnerable
Reflected XSS (secure)	/search_secure	✅ Secure
Stored XSS (vuln)	/comments	❌ Vulnerable
Stored XSS (secure)	/comments_secure	✅ Secure
Cookie Steal Demo	/steal?data=	🧪 Demo



---

💥 Reflected XSS — Test Payloads

Open:

http://127.0.0.1:5001/search?query=test

Try payload:

<script>alert('RB XSS')</script>

Or:

<img src=x onerror="alert('RB XSS')">

🟢 Alert box aaye → Reflected XSS Successful 💣

Secure version:

http://127.0.0.1:5001/search_secure?query=test

Yahaan payload text ki tarah dikhega, execute nahi hoga 🛡️


---

🔥 Stored XSS — Comment System

Open:

http://127.0.0.1:5001/comments

Comment box me payload:

<script>alert('Stored XSS by RB')</script>

🔄 Page reload → sab visitors ko alert popup
Ye Persistent XSS hota hai ⚠️

Secure version:

http://127.0.0.1:5001/comments_secure

🔐 Yahaan payload text form me hi show hoga.


---

👨‍💻 Author

RB Education Hub – Cyber Security Training
YouTube: https://www.youtube.com/@RBEDUCATIONHUB-l5n

💬 Follow for more hacking labs and tutorials 🔥


---

⭐ Support the Project

Agar ye lab helpful lage:

⭐ Star this repository
🍴 Fork karein
💡 Suggestions share karein
