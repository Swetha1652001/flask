from flask import Flask,redirect,url_for,request
app=Flask(__name__)
#route() is the decorator,which says the which application URL should call associated fn

@app.route('/hello')
def sucess(name):
    return 'welcome %s' %name
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        user=request.form['nm'] 
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user))       
#bind a URL with a fn 
##app.add_url_rule('/','hello',heloo_world)    

if __name__=='__main__':
    app.run(debug=True)    