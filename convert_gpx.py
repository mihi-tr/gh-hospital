import json
import xml.dom.minidom

f=open("ghana_Health_care.gpx")
x=xml.dom.minidom.parse(f)

def convert_entry(entry):
  data={}
  data["lon"]=entry.getAttribute("lon")
  data["lat"]=entry.getAttribute("lat")
  name=entry.getElementsByTagName("name")[0].firstChild.data
  if ":" in name:
    (data["category"],data["name"])=name.split(":",1)
  else:
    data["category"]=name
    data["name"]=name
  return data

data=[convert_entry(i) for i in x.getElementsByTagName("wpt")]
f.close()
f=open("ghana_Health_care.json","w")
json.dump(data,f)
f.close()
