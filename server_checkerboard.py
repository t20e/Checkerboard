from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def checker_board():
    return render_template('index.html',x_axis=4, y_axis = 4 )


@app.route('/4')
def x_s():
    x_axis = int(4 // 2)
    return render_template('index.html', x_axis = x_axis,y_axis = 4)


@app.route('/<int:t>')
def custom(t):
    x_axis = t//2 
    return render_template('index.html',x_axis = x_axis,y_axis = 4)

@app.route('/<int:t>/<int:h>')
def custom_two(t,h):
    x_axis = t//2 
    y_axis = h//2 
    return render_template('index.html',x_axis = x_axis,y_axis =y_axis)






# local host 5000 should print a 8by 8 cheaker board

# local host 4 should display a 8 by 4 checker board 

# local (x)(y) should display x by y 




if __name__ =="__main__":
    app.run(debug=True)