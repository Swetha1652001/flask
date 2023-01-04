from flask import Flask
app=Flask(__name__)
#route() is the decorator,which says the which application URL should call associated fn

@app.route('/hello')
def heloo_world(swetha):
    return 'hello'
#bind a URL with a fn 
app.add_url_rule('/','hello',heloo_world)    

if __name__=='__main__':
    app.run(debug=True)    