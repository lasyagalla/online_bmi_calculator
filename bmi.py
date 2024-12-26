from flask import Flask,request,render_template

obj=Flask(__name__)
@obj.route("/",methods=["GET","POST"])
def home():
    weight=''
    height=''
    bmi=''
    bmi1=''
    if request.method=="POST":
        if 'w1' in request.form and 'w2' in request.form:
            weight=request.form.get('w1')
            height=request.form.get('w2')
            bmi=int(weight)/int(height)
        if bmi<18.5:
            bmi1='Underweight'
        elif bmi>=18.5 and bmi<24.9:
            bmi1='Normal'
        elif bmi>=25 and bmi<=29.9:
            bmi1='Over weight'
        else:
            bmi1='Obesity'
    return render_template("index.html",weight=weight,height=height,bmi=bmi,bmi1=bmi1)

obj.run()