import os;os.system(f"""flask run -h {os.popen("ip addr show | grep 'inet 19'").read().split('/')[0].split()[-1]}""")