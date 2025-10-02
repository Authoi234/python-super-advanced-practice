import subprocess
result = subprocess.run(["date"], capture_output=True)
print(result.returncode)
print(result.stdout)

result2 = subprocess.run(["rmdir", "/s", "/q", "xyz.xyz"], capture_output=True)
print("return code", result.returncode)
print("stdout", result.stdout)
print("stderr", result.stderr)