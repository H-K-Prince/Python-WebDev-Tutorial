from flask import Flask, render_template, request, redirect, url_for,jsonify

JOB = [
	{
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    }
    
]

comp_name = "HALDIYAS"

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html",
                jobs=JOB,
        		company_name=comp_name)
@app.route("/api/jobs")
def joblist():
    return jsonify(JOB)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True) 