---
title: Colour analysis | Digital Humanities Library Lab - Exploring digital collections, 24 May 2017
---

# Digital Humanities Library Lab: Exploring digital collections, 24 May 2017


## Activity: Colour analysis with front covers of publications

_ROUGH_

#### Objectives
Analyse a visual aspect of an entire historical collection using a simple tool and begin thinking of questions to ask. Repeat the process with another collection and a developed set of tools from another institution.

### Overview

- A (relatively) simple example I developed, using _Illustrated London News_ 
  * Task
  * How was the tool built?
- A more developed example from Yale University Library, using _Vogue_
  * Tasks
  
### A (relatively) simple example I developed, using _Illustrated London News_  
![ILN landing page](img/iln-110.png)
The University of Manchester subscribes to the Gale Cengage collection [Illustrated London News Historical Archive 1842 to 2003](http://www.library.manchester.ac.uk/search-resources/databases/i/dbname-377375-en.htm). Access to Illustrated London News is provided online through usual browse and search tools within a web interface.

![ILN browse by year](img/iln-120.png)
You can search for keywords or any text within the documents, or browse the issues' front covers by year. This interface suits many uses but does not, for example, allow one to look at the covers of all issues at once.

We have a back-up hard drive with all issues, as OCR-transcribed text files and image scans. I wrote a tool to quantify one aspect of the cover image, its (crude) average colour, and show this in a calendar view. It covers data from 1964 onwards, when colour was first used on the cover.

(Note that the crude method to determine single mode colour the image is used to keep the workshop simple. A better method would be to use [_k_-means clustering](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html) for the _k_ main colours of the image.)
* Open [colour analysis tool (calender view)](calendara.html){:target="_blank"}
![ILN tool, calendar default](img/iln-130.png)
The tool has controls to alter the display, which may appear at the bottom or right of the screen. You can adjust scale, gridlines, wrapping and background colour (black or white). It might help to zoom in or out in the browser as well. 

The image below shows the tool adjusted to fit all the issies on-screen, with a black background for clarity.
![ILN tool, calendar altered view](img/iln-131.png)

An alternative, advanced [table view](table.html){:target="_blank"} is also available, with each issue is accompanied by its red, green and blue values, plus the equivalent hue, luminance and saturation values. There are controls to alter the display of the table, and links to open the issue in the regular web interface (if you are on-campus). Be aware, the average colour calculation is very crude, so anything you interpret from the hue, luminance and saturation numbers should consider this.
![ILN tool, table view](img/iln-140.png)

#### Task
1. Look at the average colours for each issue, what can you see?
  * Are there trends? Does this give you a better idea of the change of publishing frequency with time?
  * Is there a correlation between particular colours and particular dates, such as red during times of economic recession, black during times of war...? (Hint: 

![ILN issue that's mostly red in colour](img/iln-150.png)

  
#### How was the tool built?
There were two stages to the process, both involving writing a little Python (version 2.7.6).

1. Read all the front page image scans from bulk access hard drive, one JPG file per issue, and determine the most frequently occuring (mode) colour value for each (as a value for :closed_book: red, :green_book: green and :blue_book: blue). Save this data to a CSV file.
2. Read the CSV file with headings [year, month, day, red, green, blue] and produce an HTML page to show it. The is a script for calendar view, one for table view, and an example CSV file. Note that the RGB values are integers between 0 and 255.

![Python icon](img/python-16.png) [make_csv.py](src/make_csv.py),
![Python icon](img/python-16.png) [create_calendara_page.py](src/create_calendara_page.py),
![Python icon](img/python-16.png) [create_table_page.py](src/create_table_page.py),
![CSV icon](img/csv-16.png) [dummy-values.csv](src/dummy-values.csv)

This version of Python is available on your University desktop through the [Software Centre](http://www.itservices.manchester.ac.uk/software/) (search "Anaconda").

### A more developed example from Yale University Library, using _Vogue_
![RRV landing page](img/rrv-110.png)
![RRV colourmetric space](img/rrv-120.png)
- What else would make this more useful? Text from the cover, charts,...
- This is just the start. Look at a series of projects from the Digital Humanities Lab at Yale University Library, [Robots Reading _Vogue_](http://dh.library.yale.edu/projects/vogue/){:target="_blank"}.
  * Look at some of the developed ideas here.
  * How was this possible? Using a ProQuest collection with access to all fulltext and images, using tools.
  * What is the next step?

### Tasks
_TO DO_



[:arrow_up_small: Back to top](#activity-colour-analysi-with-front-covers-of-publications) | [:arrow_double_up: Parent](index.html) | [:arrow_backward: Prev](jstorta.html) | [:arrow_forward: Next](wrapping.html)

[:house: Home](/)
