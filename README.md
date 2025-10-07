# HeaderHunter 🕵️‍♂️

**Quick Web Security Header Analyzer** — Minimal, single-file tool for learning and quick web security checks.

---

## 🚀 Features
- Checks important HTTP Security Headers:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
- Reports which headers are present and which are missing.
- Clean and simple terminal output.
- No extra dependencies besides `requests`.

---

## 💻 Usage
```bash
git clone https://github.com/YourUsername/HeaderHunter.git
cd HeaderHunter
python headerhunter.py
```
## ⚡ Example Output
Enter URL: https://example.com

🎯 Target: http://example.com

✅ Found Headers:
 - X-Frame-Options: SAMEORIGIN
 - X-Content-Type-Options: nosniff

⚠️ Missing Headers:
 - Content-Security-Policy
 - Strict-Transport-Security
 - Referrer-Policy
 - Permissions-Policy
