from flask import Flask, request, render_template
import csv
from models import mean_age

app = Flask(__name__)
fields = ['First Name', 'Last Name', 'Age', 'Gender']

try:
  with open('data.csv', 'x', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
except:
  print("File already exists.")

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
  fname = request.form.get("fname")
  lname = request.form.get("lname")
  age = request.form.get("age")
  gender = request.form.get("gender")
  
  with open('data.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([fname, lname, age, gender])
    return render_template("index.html")
  
if __name__ == "__main__":
  app.run(port=3000, debug=True)


  

