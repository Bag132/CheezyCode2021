from flask import Flask, render_template, request


def create_app():
	app = Flask(__name__)

	@app.route("/")
	def main_page():
		storeName = request.args.get('storename')
		data = {'storename':storeName, 'raccoon':'meh'}
		return render_template('index.html', storename=storeName)

	@app.route("/waitingroom")
	def waiting():
		storeName = request.args.get('storename')
		name_ = request.args.get('name')
		size_ = request.args.get('size')

		return render_template('waitingroom.html', storename=storeName, name=name_, size=size_)
	return app


if __name__ == '__main__':
	app = create_app()
	app.run(host='0.0.0.0', debug=True)
