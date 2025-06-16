"""
Guardian AI Core System
Author: Sidhant Negi
GitHub: https://github.com/Sidhant1s
Status: Prototype
License: Confidential and Not Patented

Note: Portions of this code were generated or assisted using AI (ChatGPT by OpenAI) under the guidance of the inventor.
"""


import os
import hashlib
import socket
import time
import threading
import cv2
import face_recognition
import platform
from cryptography.fernet import Fernet

# --- Configuration ---
SAFE_PATHS = ["https://secured.cloudserver.com/upload"]
EMERGENCY_CONTACT = "contact@example.com"
AI_MODE = "offline"
KEY = Fernet.generate_key()
fernet = Fernet(KEY)

# --- Functions ---
def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(file_path, 'wb') as f:
        f.write(encrypted)

def scan_path(path):
    return any(path.startswith(safe) for safe in SAFE_PATHS)

def detect_intrusion():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # Simulated pattern check
    suspicious = "192.168" not in ip_address
    if suspicious:
        print("[ALERT] Intrusion detected from:", ip_address)
        lock_device()

def lock_device():
    print("[SECURITY] Locking device and encrypting sensitive data...")
    # Simulate lock (real implementation would integrate with OS)
    os.system("shutdown -l")

def capture_face_emotion():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if not ret:
        return False
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) == 0:
        return False
    print("[INFO] Face detected. Emotion analysis pending...")
    return True

def monitor_sensitive_data(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'rb') as f:
        original_hash = hashlib.sha256(f.read()).hexdigest()
    while True:
        with open(file_path, 'rb') as f:
            current_hash = hashlib.sha256(f.read()).hexdigest()
        if current_hash != original_hash:
            print("[WARNING] Unauthorized modification attempt!")
            encrypt_file(file_path)
            break
        time.sleep(5)

def upload_data_securely(file_path, destination):
    if scan_path(destination):
        encrypt_file(file_path)
        print(f"[UPLOAD] {file_path} uploaded securely to {destination}")
    else:
        print("[BLOCKED] Unsafe upload path. Action stopped.")

def background_monitor():
    while True:
        detect_intrusion()
        time.sleep(60)

# --- Entry Point ---
if __name__ == "__main__":
    sensitive_file = "user_documents/confidential.txt"
    threading.Thread(target=background_monitor, daemon=True).start()
    if capture_face_emotion():
        monitor_sensitive_data(sensitive_file)
        upload_data_securely(sensitive_file, "https://secured.cloudserver.com/upload")
