from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime', methods=['GET'])
def current_datetime():
    date_now = datetime.now()

    date_today = f"{date_now.strftime('%d')}/{date_now.strftime('%m')}/{date_now.strftime('%Y')}"

    result_date = f"{date_today} {date_now.strftime('%H')}:{date_now.strftime('%M')}:{date_now.strftime('%S')}"
    
    hour_now = int(date_now.strftime("%H"))
    
    if hour_now < 12:
        message = "Bom dia!" 
    
    if hour_now >= 12 and hour_now < 18:
        message = "Boa tarde!"
    
    if hour_now >= 18:
        message = "Boa noite!"
    
    return {"current_datetime": result_date, "message": message}
    



