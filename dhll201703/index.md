---
title: Digital Humanities Library Lab: Exploring digital collections, 3 March 2017
---

# Digital Humanities Library Lab: Exploring digital collections, 3 March 2017

## Aims of the workshop
This workshop is for researchers in the Faculty of Humanities at The University of Manchester who wish to continue exploring digital collections at The University of Manchester Library. The ideas and techniques that you will see and have hands-on experience with might inspire you to develop further Digital Humanities research projects. You will look at digital text collections from publishers at platforms such as JSTOR, Jisc, Adam Matthew and Gale Cengage, using light-touch text and data mining techniques. Some of the activities will involve using a bit of Python code; however, the workshop assumes you may have no prior programming experience.

The event is scheduled for 2pm to 5pm on Friday, 3 March 2017 (breaking around 3.30pm for coffee).
Location: Teaching Suite (Blue 4), Main Library, The University of Manchester Library.
Computers will be available, though you may bring your own laptop if you wish.

## Overview of the afternoon
- [Welcome and introduction](welcome.html)
- Activity: Jisc Historical Collections
- Activity: JSTOR Topicgraph
- Activity: Adam Matthew Mass Observation
- Activity: JSTOR Data for Research
- Conclusion

## Welcome and introduction

## Activity: Jisc Historical Collections
We will have a look at [Jisc Historical Collections](http://historicaltexts.jisc.ac.uk/). This interface  provides a single search interface to multiple collections:

- Early English Books Online (EEBO) 1473-1700
- Eighteenth Century Collections Online (ECCO) 1701-1800
- British Library's 19th century collection 1789-1914

It offers elementary Digital Humanities techniques...

## Activity: JSTOR Topicgraph
A new tool to help explore scholarly books is [JSTOR Topicgraph](https://labs.jstor.org/topicgraph/). We will look at visualisations of monographs and try uploading PDFs of our own.

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

## Activity: JSTOR Data for Research
[JSTOR Data for Research](http://dfr.jstor.org/)

## Conclusion
...

Go to [Back to top](#overview-of-the-afternoon) | [Home](/)