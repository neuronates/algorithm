from gpiozero import MCP3008

while True:
	with MCP3008(channel=0) as pot:
		pot_v = pot.value*3.3
		print (pot_v)

