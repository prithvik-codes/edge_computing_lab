# -*- coding: utf-8 -*- 
import requests 
import random 
import time 
import os 
# Use the container name as the hostname 
SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://data-logger:8000/log") 
print("Simulator started. Sending data every 10 seconds...") 
while True: 
 temp = round(random.uniform(20.0, 30.0), 2) 
 try: 
 response = requests.post(SERVICE_A_URL, json={"temperature": temp})  print(f"Sent temp {temp}C: Status {response.status_code}") 
 except Exception as e: 
 print(f"Connection Error: {e}") 
 time.sleep(10)
