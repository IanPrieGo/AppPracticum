
$B = 100

if ($args[0] -ne $null){

    $B = $args[0]

} else {
	echo "No Brightness value entered"
}

$m=Get-CimInstance -Namespace root/WMI -ClassName WmiMonitorBrightnessMethods
Invoke-CimMethod $m -MethodName WmiSetBrightness -Arguments @{Brightness = $B; Timeout = 1}