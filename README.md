# 🔐 Cybersecurity & Utilities Toolkit  

This repository contains a collection of Python mini-projects that I built while learning **cybersecurity and Python programming**.  
Each script focuses on a different concept: **network scanning, password security, and encryption techniques**.  

The idea behind this repo is to practice Python while applying it to real-world security concepts.  

---

## 📂 Tools Included  

### 1️⃣ Port Scanner  
- Uses the `nmap` library to scan a target IP address.  
- Identifies open ports, running services, and protocols.  
- Helps understand how reconnaissance and network scanning works in cybersecurity.  

**Learning point**: I learned how to use external libraries (`python-nmap`) and how network scanning reveals valuable security information.  

---

### 2️⃣ Password Generator  
- Creates strong random passwords using letters, numbers, and special characters.  
- Default length is 12 characters but can be customized.  
- Demonstrates the importance of randomness in password security.  

**Learning point**: I practiced using Python’s `random` and `string` modules to create secure passwords.  

---

### 3️⃣ Password Manager  
- A simple CLI-based password manager.  
- Allows account creation and login with **SHA-256 password hashing**.  
- Stores hashed passwords instead of plain text, teaching the basics of secure storage.  

**Learning point**: I understood why hashing is important in cybersecurity and how authentication systems work.  

---

### 4️⃣ Caesar Cipher  
- Implements the classic Caesar cipher for encryption and decryption.  
- Shifts letters in the alphabet by a given key.  
- Demonstrates basic cryptography concepts and how substitution ciphers work.  

**Learning point**: I explored how encryption works at a fundamental level before moving to modern cryptography.  

---

## 🚀 How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/cybersecurity-toolkit.git
   cd cybersecurity-toolkit

2. Run any script:
   ```bash
   python port_scanner.py
   python password_generator.py
   python password_manager.py
   python caesar_cipher.py

---

##📌 Requirements 

- Python 3.x
- Livraries:
  ```bash
  pip install python-nmap

---



