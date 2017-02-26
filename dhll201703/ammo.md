---
title: Adam Matthew | Digital Humanities Library Lab - Exploring digital collections, 3 March 2017
---

# Digital Humanities Library Lab: Exploring digital collections, 3 March 2017


## Activity: Adam Matthew Mass Observation

![Adam Matthew Mass Observation](ammo-home.png)
![Mass Observation map](ammo-map.png)
### What is it? Why use it?
TBA. ALSO, IMAGES TO FOLLOW.

### Getting started

- How does it work?
- Get the API key
- Practice in the browser
- Use a simple tool
- Exercise
- Other matters
- Support from Adam Matthew

### How does it work?
A typical web request involves a [URL](https://techterms.com/definition/url){:target="_blank"} typed in the address bar of your web browser. It points to a specific site, and a specific page within that site - click in the address bar now to see the URL of this page. After you enter the URL, either by typing it or clicking on a link that contains it, you will be taken to a web page. Really, this web page is an HTML document delivered from a web server to your browser; that is, a text file written with HTML tags to give structure is rendered onto the screen.

Using the Adam Matthew API is similar. A request takes the form of a URL, which points to a specific bit of data from the Adam Matthew server. It can be used from any computer on University campus (i.e. we are restricted by IP range). You can type or paste Adam Matthew request URLs into your web browser's address bar to return data. The data it returns is still text data, but instead of using HTML markup it uses [JSON](https://en.wikipedia.org/wiki/JSON#Example){:target="_blank"} markup.

Looking at JSON data in the web browser is not particularly helpful. It is designed for programming languages to interpret, making effective use of the nested key-value pairs structure. JSON data will look better in some browsers, at least make it readable. 

### Get the API key
For the purposes of security, the URLs that you use to access the Adam Matthew API need to include a 32-digit key. The key given to us for the purpose of this workshop is not included in this web page as it could be viewed by anyone. Please await instructions on the afternoon! 

The files you will download have a dummy key XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX which you can replace with the real one.

### Practice in the browser
Before we dive into any tools or code, let's try a simple, single request.
1. Copy the example URL request below (all one 'word')
2. Paste into the address bar of a new browser window or tab.
3. Replace the API key! (Copy and paste.)
4. Press Enter. 

`https://api.amdigital.co.uk/1.0/massobservation/documents?apiKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&take=1`

You should see a JSON data response. Don't be put off, it's more useful and meaningful than it first appears.

### Use a simple tool
I have written a webpage you may use to [build an Adam Matthew API URL](https://PhilReedData.github.io/dhll201703/am-url-builder.html){:target="_blank"} and see returned JSON data. If you are using Google Chrome, the returned JSON data will, after a few seconds, display in a nicer way (pretty printing). If you are using Firefox, you will need to install an add-on called [JSONView](https://addons.mozilla.org/en-us/firefox/addon/jsonview/){:target="_blank"} to view JSON data nicely, or copy paste the data into the [Online JSON Viewer](http://jsonviewer.stack.hu/){:target="_blank"}.
![Adam Matthew API builder, aplha](img/adam-matthew-api-builder.png)

Use this page to search documents by:

- __id__ - to return a specific document and its full text

...or any combination of the following.

- __query__ - the text to search for, parsed as [Contextual Query Language (CQL)](http://developers.amdigital.co.uk/API/CQL){:target="_blank"}
- __take__ - number of records to return, up to 200
- __skip__ - the record number to start at from the list of results

Complete some of the fields above, and paste in the API key, and press the "Create URL and run" button.

The returned JSON data has a structure which includes:

- __timestamp__ - when the query was executed
- __version__ -  the version of the API used
- __totalResults__ - how many results follow
- __data__ - a list of results, or just one if you specified an "id" in the previous page.

The __data__ items include:

- __type__ - one of "document", "section" or others, depending on the query
- __collection__ - always "Mass Observation" for our queries
- __identifier__ - we can use this in a subsequent query in the "id" field
- __uri__ - a link to view the document in the regular Adam Matthew web interface
- __metadata__ - a list of metatdata items such as title, date, source, rights, and fullText (true/false)
- __fulltext__ - for a single search result (by id), if available, get the full text (could be slow)

![Adam Matthew Mass Observation](ammo-110.png)
![Adam Matthew Mass Observation](download-json-ie.png)
![Adam Matthew Mass Observation](ammo-120.png)
![Adam Matthew Mass Observation](ammo-122.png)
![Adam Matthew Mass Observation](ammo-124.png)
![Adam Matthew Mass Observation](ammo-126.png)
![Adam Matthew Mass Observation](ammo-130.png)
![Adam Matthew Mass Observation](ammo-150.png)
![Adam Matthew Mass Observation](ammo-160.png)
![Adam Matthew Mass Observation](ammo-170.png)

### Exercise
1. Try using the webpage to run a query. Consider using CQL syntax such as "prox".
2. Select a result you want to know more about. 
3. View your chosen in the regular Adam Matthew web interface (hint, find the URI field).
4. Can you get to the full text for that document?
5. _Going further_: Try the second form to look at sections within documents. What differences do you see?
6. _Going even further_: Write a short Python script that takes a URL, calls the Adam Matthew API, returns JSON data, then does something with that data. [I have written the start of the script for you...](https://github.com/PhilReedData/AdamMatthewTry) TBA


### Other matters
(May put this in the Conclusions section) Data mining agreements, copyright... TBA

### Support from Adam Matthew
This is not part of the usual service from Adam Matthew, or from academic libraries in the UK. There is some guidance from [The Adam Matthew API](http://developers.amdigital.co.uk/API/Overview).


Go to [Back to top](#activity-adam-matthew-mass-observation) | [Parent](index.html) | [Home](/) | [Prev](jstortg.html)
