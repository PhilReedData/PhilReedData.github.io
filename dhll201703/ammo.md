---
title: Adam Matthew | Digital Humanities Library Lab: Exploring digital collections, 3 March 2017
---

# Digital Humanities Library Lab: Exploring digital collections, 3 March 2017


## Activity: Adam Matthew Mass Observation

### What is it? Why use it?

### Getting started

- How does it work?
- Get the API key
- Practice in the browser
- Types of request
- Get the code

### How does it work?
A typical web request involves a [URL](https://techterms.com/definition/url){:target="_blank"} typed in the address bar of your web browser. It points to a specific site, and a specific page within that site - click in the address bar now to see the URL of this page. After you enter the URL, either by typing it or clicking on a link that contains it, you will be taken to a web page. Really, this web page is an HTML document delivered from a web server to your browser; that is, a text file written with HTML tags to give structure is rendered onto the screen.

Using the Adam Matthew API is similar. A request takes the form of a URL, which points to a specific bit of data from the Adam Matthew server. It can be used from any computer on University campus (i.e. we are restricted by IP range). You can type or paste Adam Matthew request URLs into your web browser's address bar to return data. The data it returns is still text data, but instead of using HTML markup it uses [JSON](https://en.wikipedia.org/wiki/JSON#Example){:target="_blank"} markup.

Looking at JSON data in the web browser is not particularly helpful. It is designed for programming languages to interpret, making effective use of the nested key-value pairs structure. So we will (TBC) use a short Python script that takes a URL, calls the Adam Matthew API, returns JSON data, then does something with that data.

### Get the API key
For the purposes of security, the URLs that you use to access the Adam Matthew API need to include a 32-digit key. The key given to us for the purpose of this workshop is not included in this web page as it could be viewed by anyone. Please await instructions on the afternoon! 

The files you will download have a dummy key XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX which you can replace with the real one.

### Practice in the browser
Before we dive into any programming or code, copy the example URL request below, paste into a new window or tab address bar, replace the key, and press Enter. 

`https://api.amdigital.co.uk/1.0/massobservation/documents?apiKey=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&take=1`

You should see a JSON data response.

### Types of request
I have written a webpage you may use to [build an Adam Matthew API URL](http://personalpages.manchester.ac.uk/staff/Phil.Reed/) and see returned JSON data. 

[Alternative link](https://PhilReedData.github.io/dhll201703/am-url-builder.html) - you will need to right-click on this link and save the page to your computer, then open it in Chrome. Why? Because the alternative link is hosted outside the University's IP address range so Adam Matthew won't accept requests from it.

...

### Support from Adam Matthew
[The Adam Matthew API](http://developers.amdigital.co.uk/API/Overview)


Go to [Back to top](#activity-adam-matthew-mass-observation) | [Parent](index.html) | [Home](/)