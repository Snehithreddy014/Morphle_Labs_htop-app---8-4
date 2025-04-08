# from flask import Flask
# import getpass
# import time
# import subprocess
# import pytz
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/htop')
# def htop():
#     name = "Snehith Siddharth"  # Replace with your full name
#     username = getpass.getuser()
    
#     ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')

#     top_output = subprocess.getoutput("top -b -n 1 | head -10")

#     html = f"""
#     <h2>Name: {name}</h2>
#     <h2>Username: {username}</h2>
#     <h2>Server Time (IST): {ist_time}</h2>
#     <pre>{top_output}</pre>
#     """
#     return html

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)











from flask import Flask
import getpass
import time
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Snehith Siddharth"  # Replace with your full name
    username = getpass.getuser()
    
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    html = f"""
    Name: {name}<br>
    user: {username}<br>
    Server Time (IST): {ist_time}<br>
    <br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

