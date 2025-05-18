from flask import Flask, request, render_template
import csv

app = Flask(__name__)
fields = ['First Name', 'Last Name', 'Age']

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
  
  with open('data.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([fname, lname, age])
    return render_template("index.html")
  
if __name__ == "__main__":
  app.run(port=3000, debug=True)


  

