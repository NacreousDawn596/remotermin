import requests;import sys
while True: 
	um="\n->"
	result = requests.get(f"{f'http://{sys.argv[1]}/os/'}{input(um).replace('/', '¹')}").json()
	if result["error"] == "": print(result["output"])
	elif result["error"] != "" && result["output"]: print(result["error"])
	else: print(f"""output: \n{result["output"]}\nerror: \n{result["error"]}"")
