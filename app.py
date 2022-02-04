from subprocess import PIPE, Popen;from flask import Flask, render_template;app = Flask(__name__)
@app.route('/os/<command>')
def os(command): 
	stdout, stderr = Popen(f"""cd ~/ && {command.replace("¹", "/")}""", shell=True, stdout=PIPE, stderr=PIPE).communicate()
	return {"output": stdout, "error": stderr}
