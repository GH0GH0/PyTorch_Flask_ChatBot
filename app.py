from flask import Flask, render_template, url_for, request
from chat import bot_name,get_response
import json

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.form['content']
        reponse = get_response(message)
        with open(filename) as json_file:
            msg = json.load(json_file)
            
            temp = msg['Chat']
            # python object to be appended
            y = {
                "message-user": message,
                    "reponse": reponse
                }
            # appending msg to emp_details 
            temp.append(y)
       
        write_json(msg)

        return render_template('index.html', monBot=bot_name,reponse=reponse, message=message)

    else:
        return render_template('index.html')


filename='chat.json'
# function to add to JSON
def write_json(msg):
    with open(filename,'w') as f:
        json.dump(msg, f, indent=4)
      
      

      


if __name__ == "__main__":
    app.run(debug=True)