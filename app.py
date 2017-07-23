from flask import Flask,render_template,request
import random
import dataset

app= Flask(__name__)

# db=dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")
# table=db["khaled_user"]
# print(db.tables)






@app.route("/")
def load_page():
	fortune=["chocoleta is the life","If you hate chocolata close this web","cocolata is the tast of love","you have to eat chocolate every time,and forever","welcome in our team of cocoleta addicts"]
	return render_template ("index.html",qouts=random.choice(fortune))
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
	# table.insert(dict(firstname=user_firstname,lastname=user_lastname,Messges=user_Messges,gender=user_gender))
	# for i in table:
	# return table.find_one(firstname="khaled")


		# print("Id : "+str(i["id"])+"; Name"+i["firstname"]+"; lastname"+i["lastname"],Messges"+i["user_Messges"],user_Messges)
	return render_template("data.html",thefirstname=user_firstname,
							thelastname=user_lastname,themessege=user_Messges,thegender=user_gender)





if __name__=="__main__":
	app.run() 
