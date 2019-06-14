import xml.dom.minidom as md 
from xml.dom.minidom import Node 

root=md.parse('new.xml')

f=open('distance_file','w')
for elem in root.getElementsByTagName('timestep'):
	time=elem.getAttribute("time")
	edges=elem.getElementsByTagName("edge")
	vehic_pos={}
	for edge in edges:
		for child in edge.childNodes:
			if child.nodeType==3:
				continue
			elif child.nodeType==1:
				highway=child.getAttribute('id')
				vehicles=child.getElementsByTagName("vehicle")
				for vehicle in vehicles:
					vehicle_id=vehicle.getAttribute('id')
					speed=vehicle.getAttribute('speed')
					pos=vehicle.getAttribute('pos')
					vehic_pos[vehicle_id]=pos
	vehicles=list(vehic_pos.keys())
	for i in range(len(vehicles)):
		for j in range(1,len(vehicles)):
				if vehicles[j] == "type1.66" and vehicles[i] == "type2.66":
					dist=abs(float(vehic_pos[vehicles[j]])-float(vehic_pos[vehicles[i]]))
					if dist<20:
						f.write("At time {}, vehicle {} is at range {} from vehicle {} which is in Range \n".format(time,vehicles[j],dist,vehicles[i]))
