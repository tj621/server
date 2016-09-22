'''

@author: Zxh
'''
import urllib2
import urllib

data = {"roof_vent_south": "on"}

url = 'http://localhost:8020/control'
post_data = urllib.urlencode(data)

req = urllib2.urlopen(url, post_data)

content = req.read().decode
