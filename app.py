from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test/my/first', methods=["POST"])
def first_post():
	try:
		my_json = request.get_json()
		print(my_json)
		get_name = my_json.get('name')
		get_age = my_json.get('age')
		if not all([get_age, get_name]):
			return jsonify(msg="缺少参数!")
		get_age += 10
		return jsonify(name=get_name, age=get_age)
	except Exception as e:
		print(e)
		return jsonify(msg="请查看是否正确访问!")

if __name__ == '__main__':
	app.run()
