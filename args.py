import os
import sys
import platform 
import urllib.request
#import request


#test = "https://artifactory.opentext.net/artifactory/libs-igc-local/com/opentext/be/be-installer/16.6.1.61/be-installer-16.6.1.61.zip!/WebPackage/BravaEnterprise_16.6.1.61.exe"
osytpe = platform.system()
version = sys.argv[1]
location = sys.argv[2]

#print(location+ version)
url = "https://artifactory.opentext.net/artifactory/libs-igc-local/com/opentext/be/be-installer/"+version+"/be-installer-"+version+".zip!/WebPackage/BravaEnterprise_"+version+".exe"

print('Downloading starts...')

#test = requests.get(url)



#print(location+version+".exe")
#urllib.request.urlretrieve(url, location+version+'.exe')

print('Downnloaded')

os.startfile(location+version+".exe")