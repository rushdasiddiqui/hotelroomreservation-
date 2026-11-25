from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template["index.html"]
@app.route("/reserve",methods=["POST"])
def reserve():
    name=request.form["guest"]
return "Reservation confirmed for " +name
    
if __name__=="__main__":
app.run(debug==True)
