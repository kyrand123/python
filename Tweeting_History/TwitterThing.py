


import twitter, datetime ,urllib2, time   #Import the required features, including twitter wrapper, timestamp, the urllib2 (which is used for websites)


file = open("history file")  #opens the history folder, one has not been specififed as different pcs have different locations
history = file.read() #reads in the history file.

while True:                     #loops forever and ever
        time.sleep(3600)        #sets the timer for one hour delay (updating every hour)

        #Work out how to get the information about the history page. 


        webpage = urllib2.urlopen(page) # uses urllib2 to open a the webpage page
        website = response.read()       #reads in the websites data
        print(website)                  #prints the webpages data

        #Work out how to find the title of the page from start to end. 

        api = twitter.Api(consumer_key="Consumer Key",consumer_secret="Consumer secret",
                          access_token_key="token key",access_token_secret="Token Secret") #This gets all the access information for the twiiter wrapper, I dont have twitter so you can input your own data

        timestamp = datetime.datetime.utcnow()  #This gets a timestamp for the current time zone.

        response = api.PostUpdate("The last thing I looked at is " + websiteTitle + str(timestamp))       #This posts the twitter update including the time stamp from the api and what I have recently been on using data from the hisory page.

        print("Status updated to: " + response.text) #Prints showing that twitter has been updates.
