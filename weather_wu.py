#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Debbie
#
# Created:     29/09/2014
# Copyright:   (c) Debbie 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
import json

def main():
    f = urllib2.urlopen('http://api.wunderground.com/api/' + wu_key + '/hourly/q/MI/Oxford.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    ##location = parsed_json['location']['city']
    ##temp_f = parsed_json['current_observation']['temp_f']
    ##print "Current temperature in %s is: %s" % (location, temp_f)
    hourlyforecast = parsed_json['hourly_forecast']
    for i in range(len(hourlyforecast)):
        print"Probability of precip is %s in %s hours" % (hourlyforecast[i]['pop'], i )
    ##print "Probability of Precipitation is: %s" % (parsed_json['hourly_forecast'][0]['pop'])
    f.close()

if __name__ == '__main__':
    main()
