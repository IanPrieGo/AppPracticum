import subprocess
import sys

# cmd0 = "$m"
# cmd01 = "=Get-CimInstance -Namespace root/WMI -ClassName WmiMonitorBrightnessMethods"
# cmd1 = "Invoke-CimMethod $m -MethodName WmiSetBrightness -Arguments @{Brightness = 0; Timeout = 1}"

# # subprocess.run(["powershell", cmd0], shell=True)

process = subprocess.run(["powershell", "./test.ps1", sys.argv[1]], shell=True)

# print(sys.argv)
# print(process)
# subprocess.run(["powershell", "echo", "XD"], shell=True)