import requests;import sys
while True: um="\n->";print(requests.get(f"{f'http://{sys.argv[1]}/os/'}{input(um).replace('/', '¹')}").json()["output"])