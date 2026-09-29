inventario= [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"},
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"}
]
#imprimir todos los hostname
for h in inventario:
	prin(h["hostname"])
#imprimir todos las ips
for x in inventario:
	print(x["ip"])
#imprimir todos los que esten en down
for v in range:
	if v ["status"]=="down":
		print(v["hostname"])

