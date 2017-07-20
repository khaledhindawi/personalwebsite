from flask import Flask,render_template,request
import random
app= Flask(__name__)
@app.route("/")

def load_page():
	fortune=["chocoleta is the life","If you hate chocolata close this web","cocolata is the tast of love","you have to eat chocolate every time,and forever","welcome in our team of cocoleta addicts"]
	return render_template ("index.html",qouts=random.choice(fortune),)
	# return render_template ("index.html")




@app.route("/aboutme")
def aboutme():
	return render_template ("aboutme.html")
@app.route("/contact")
def contact():
	return render_template ("contact.html")

# @app.route("/form/")
# def form():
	# return render_template ("input_form.html")

@app.route("/form_response",methods=["POST"])
def form_res():
	user_firstname=request.form["firstname"]
	user_lastname=request.form["lastname"]
	user_Messges=request.form["messege"]
	user_gender=request.form["gender"]
	return render_template ("data.html",thefirstname=user_firstname,thelastname=user_lastname,themessege=user_Messges,thegender=user_gender)





if __name__=="__main__":
	app.run() 
