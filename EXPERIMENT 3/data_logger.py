from fastapi import FastAPI 
from pydantic import BaseModel 
import os 
app = FastAPI() 
log_file = "/data/log.txt" 
class SensorData(BaseModel): 
 temperature: float 
@app.post("/log") 
async def log_data(data: SensorData): 
 # Get the date from the system 
 timestamp = os.popen('date').read().strip() 
 with open(log_file, "a") as f: 
 f.write(f"Temperature: {data.temperature}C: at {timestamp}\n") 
 return {"status": "logged"} 
if __name__ == "__main__": 
 import uvicorn 
 uvicorn.run(app, host="0.0.0.0", port=8000)
