import sys
import requests
from time import localtime, strftime

def main(argv):

    if argv == '':
        key = 'my_key'
    else:
        key = argv

    curr_hour=localtime().tm_hour
    if (curr_hour < 8):
        map_url = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.0=1%20Continental%20Dr%2C%20Auburn%20Hills%2C%20MI%2048326&wp.1=601%20Gallagher%20Ct%2C%20Oxford%2C%20MI%2048371&optmz=timeWithTraffic&tt=Departure&key=' + key
        retval = (strftime("%Y-%m-%d %H:%M:%S", localtime()), minutesWorkToHome(map_url))
    elif (curr_hour > 15):
        map_url = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.1=1%20Continental%20Dr%2C%20Auburn%20Hills%2C%20MI%2048326&wp.0=601%20Gallagher%20Ct%2C%20Oxford%2C%20MI%2048371&optmz=timeWithTraffic&tt=Departure&key=' + key
        retval = (strftime("%Y-%m-%d %H:%M:%S", localtime()), minutesHomeToWork(map_url))

    print retval # Has format like ('2015-01-13 22:40:39', 21.15)

def minutesWorkToHome(map_url):
    "this funciton fetches the time from work to home in minutes"
    data = requests.get(map_url)  #TODO need some protection for errors
    output = data.json()

    return (output['resourceSets'][0]['resources'][0]['travelDurationTraffic']/60.0)

def minutesHomeToWork(map_url):
    "this funciton fetches the time from home to work in minutes"
    data = requests.get(map_url)  #TODO need some protection for errors
    output = data.json()

    return (output['resourceSets'][0]['resources'][0]['travelDurationTraffic']/60.0)

if __name__ == '__main__':
    main(sys.argv[1])
