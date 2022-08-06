from flask import Flask,render_template,request
app=Flask(__name__)

#########################################
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search',methods=['POST','GET'])
def search_function():
    name = request.args["in_1"]
    regex = request.args["in_2"]
    return render_template('search.html',n=name,r=regex)




if __name__=='__main__':
    app.run(debug=True)
