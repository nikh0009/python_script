import requests

url="https://artifactory.opentext.net/artifactory/libs-igc-local/com/opentext/be/be-installer/16.6.1.61/be-installer-16.6.1.61.zip!/WebPackage/BravaEnterprise_16.6.1.61.exe"
r = requests.get(url)


print ("Downloading")
with open('C:\\Nikhil Tripathy\\python_script\\pydown\\Brava.exe', wb) as f:
	f.write(r.content)

print(r.status_code)