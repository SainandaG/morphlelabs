from flask import Flask
import getpass
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sai Nanda Gurram"
    username = getpass.getuser()

    # IST Time
    ist = pytz.timezone('Asia/Kolkata')
    time_ist = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True)
    except Exception as e:
        top_output = str(e)

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {time_ist}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)