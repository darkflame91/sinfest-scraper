import requests
import datetime
start = datetime.date(2000,1,17)
current = datetime.date(2014,8,1)
special = datetime.date(2012,8,18)
givendir = raw_input("Enter the path where the images should be stored!\n")
i = 0
try:
    while current <= special:
        i += 1
        if i%50 == 0:
            print str(current)+" is what I'm working on"
        ext = ".jpg"
        r = requests.get("http://www.sinfest.net/btphp/comics/"+str(current)+ext)
        if r.status_code != 200:
            ext = ".png"
            r = requests.get("http://www.sinfest.net/btphp/comics/"+str(current)+ext)
            if r.status_code != 200:
                current = current + datetime.timedelta(days=1)
                continue
        with open(givendir+"/"+str(current)+ext, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)    
        print str(current)+" complete!"
        current = current + datetime.timedelta(days=1)

        

    while current <= datetime.date.today():
        i += 1
        ext = ".gif"
        r = requests.get("http://www.sinfest.net/btphp/comics/"+str(current)+ext)
        if r.status_code != 200:
            ext = ".jpg"
            r = requests.get("http://www.sinfest.net/btphp/comics/"+str(current)+ext)
            if r.status_code != 200:
                ext = ".png"
                r = requests.get("http://www.sinfest.net/btphp/comics/"+str(current)+ext)
                if r.status_code != 200:
                    print str(current)+" DIDN'T HAPPEN!"
        with open(givendir+"/"+str(current)+".gif", 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
        if i%10 == 0:
            print str(current)+" complete!"
        current = current + datetime.timedelta(days=1)
except requests.exceptions.RequestException:
    print str(current)+" OH SHIT!!!!"
