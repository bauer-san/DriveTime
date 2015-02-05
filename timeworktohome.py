import sys
import requests
from time import localtime, strftime, sleep
import matplotlib.pyplot as plt

def setup_backend(backend='TkAgg'):
    import sys
    del sys.modules['matplotlib.backends']
    del sys.modules['matplotlib.pyplot']
    import matplotlib as mpl
    mpl.use(backend)  # do this before importing pyplot
    import matplotlib.pyplot as plt
    return plt

def main(argv):

    #Initialize
    bargraph = [20, 20, 20, 20, 20, 20, 20, 20]

    if argv == '':
        key = 'my_key'
    else:
        key = argv

##    #Set up the bar graph
##    plt = setup_backend()
##    fig = plt.figure()
##    rects = plt.bar(range(8), bargraph, width=0.8, align='center')
##    plt.draw()

    while (1):
        curr_hour=localtime().tm_hour
        if (curr_hour < 9):
            map_url = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.0=1%20Continental%20Dr%2C%20Auburn%20Hills%2C%20MI%2048326&wp.1=601%20Gallagher%20Ct%2C%20Oxford%2C%20MI%2048371&optmz=timeWithTraffic&tt=Departure&key=' + key
        else: ##elif (curr_hour > 15):
            map_url = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.1=1%20Continental%20Dr%2C%20Auburn%20Hills%2C%20MI%2048326&wp.0=601%20Gallagher%20Ct%2C%20Oxford%2C%20MI%2048371&optmz=timeWithTraffic&tt=Departure&key=' + key

        minsTimeDrive = minutesWorkToHome(map_url)
##        retval = (strftime("%Y-%m-%d %H:%M:%S", localtime()), minsTimeDrive)
##        print retval # Has format like ('2015-01-13 22:40:39', 21.15)

        #TODO Complete this section next
        bargraph.pop(0) #remove oldest
        bargraph.append(minsTimeDrive)
        print bargraph

##        #update bargraph
##        #bgAverage = sum(bargraph, 0.0) / len(bargraph)
##        for rect, h in zip(rects, bargraph):
##            rect.set_height(h)
##        fig.canvas.draw()

        sleep(1800) #thirty mins

def minutesWorkToHome(map_url):
    "this funciton fetches the time from work to home in minutes"
    data = requests.get(map_url)  #TODO need some protection for errors
    output = data.json()

    return (output['resourceSets'][0]['resources'][0]['travelDurationTraffic']/60.0)

if __name__ == '__main__':
    main(sys.argv[1])
