import json
import requests
from datetime import datetime

# the json file I'm reading from
url = 'https://miau.sadgrl.online/yesterweb-ring/webring.json'

# getting the status code of the website
data = requests.get(url)

# loading the json data
yesterwebRing = json.loads(data.text);

# this opens the HTML file which is generated at the end
#f = open('yesterCheck.html', 'w')
f = open('/var/www/ring-status.yesterweb.org/html/index.html', 'w')

# this opens the log file which is generated at the end
#log = open('log.txt', "a")
log = open('/var/www/ring-status.yesterweb.org/html/log.txt', "a")

# get current time
now = datetime.now()

# this writes the html stuff that comes before the loop
f.write('<!DOCTYPE html><head><link rel="stylesheet" href="style.css"></head><body><div class="container"><h1>Yesterweb Webring Status</h1><table><colgroup><col span="1" style="50%"><col span="1" style="50%"></colgroup>')

# this function validates the URL and returns an error message associated with the status returned
def _validate_url(url):
                try:
                        r = requests.head(url, timeout=10.0)
                        # for 404s
                        if r.status_code == 404:
                                f.write ('<tr><td><a href="' + url + '" target="blank">' + url + '</a></td>' + '<td class="fourohfour">' + ' 404 NOT FOUND' + '</td></tr>')
                                # writes current date/time and error to log
                                log.write(now.strftime("%d/%m/%Y %H:%M:%S") + ' : ERROR: 404 NOT FOUND ' + url + "\n")
                        # for 200 (success)
                        if r.status_code == 200:
                                f.write ('<tr class="success"><td><a href="' + url + ' target="blank">' + url + '</a></td>' + '<td>' + ' 200 SUCCESS' + '</td></tr>')
                # if the request times out
                except requests.Timeout as err:
                        f.write ('<tr><td><a href="' + url + '" target="blank">' + url + '</a></td>' + '<td class="timedout">' + 'TIMED OUT' + '</td></tr>')
                        log.write(now.strftime("%d/%m/%Y %H:%M:%S") + ' : ERROR: URL TIMED OUT ' + url + "\n")
                # this seems to cover a lot of different errors
                except requests.RequestException as err:
                        f.write ('<tr><td><a href="' + url + '" target="blank">' + url + '</a></td>' + '<td class="error">' + 'ERROR'  + '</td></tr>')
                        log.write(now.strftime("%d/%m/%Y %H:%M:%S") + ' : ERROR: UNKNOWN ' + url + "\n")
                        # needs more info


# loops through each line in the JSON file
for s in range(len(yesterwebRing)):
        # grab the url values
        eachURL = format(yesterwebRing[s]["url"])
        # runs the validate function
        _validate_url(eachURL)

# end of page html
f.write('</table></div></body></html>')

# close log files
f.close()
log.close()