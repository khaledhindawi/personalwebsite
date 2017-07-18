from flask import Flask,render_template
import random
app= Flask(__name__)
@app.route("/")

def load_page():
	fortune=["f","d","r","w","y"]
	fortune1=["er","yt","gh","tt","df"]
	return render_template ("index.html",letter=random.choice(fortune),twolettera=random.choice(fortune1))
	# return render_template ("index.html")




@app.route("/aboutme")
def aboutme():
	return render_template ("aboutme.html")



if __name__=="__main__":
	app.run() 
