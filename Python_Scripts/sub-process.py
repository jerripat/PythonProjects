import subprocess
cmd="ls -lrt"
sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
rc=sp.wait()
output, error = sp.communicate()
print(output.decode('utf-8'))
