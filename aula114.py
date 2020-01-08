import subprocess, sys



print(subprocess.call(['ls', '-l']))
input()

print(subprocess.check_call(['cat', 'usuarios.']))
