from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.myvars = {}

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		print("whoa it's GET--------------")
		print(type(app))
		return render_template('index.html')
	# must be a post
	print("--------------------notget-------------")
	app.myvars['ticker'] = request.form['myticker']
	print(app.myvars['ticker'])

	script_chart, div_chart = plotty(app.myvars['ticker'])
	#print("@#",script_chart)


	return render_template('index.html',
						   script_chart=script_chart,
						   div_chart=div_chart)



def plotty(ticker):
	import getbokeh
	fig = getbokeh.bokeh(ticker)
	return fig



# @app.route('/ticker.html', methods=['GET','POST'])
# def mychart():
# 	print("--------$$$$$$$$$$$$--", request.method)



@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
  app.run(port=33507)
