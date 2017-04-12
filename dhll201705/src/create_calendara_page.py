import csv
import colorsys

def create_calendara_page(csvFilename):
    # Do header, table (from CSV file) then footer
    years = set([])
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # HEAD
    html = """
<!html>
<html>
<head>
    <title>ILN Cover main colour: Calendar view</title>
    <link href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i" rel="stylesheet" />
    <style>
        * {font-family: 'Lora', serif;} 
        h1, h2, h3, th {font-weight: bold;}
        #main {float: left; padding-right: 5em;}
        #controls {float: left;}
        #colorCalendar {color: white;}
        #colorCalendar h4 {color: black; }
        #colorCalendar p {float: left; margin: 0.2em;}
        .yearCol {float: left;  }
        .issue {float: left; clear: left; width: 6em; margin: 0.1em; height: 2em;}
        a, a:visited, a:hover {color: black}
        .viewLink {background-color: white !important; display: none;}
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
    <!-- Table sorting from http://stackoverflow.com/questions/3160277/jquery-table-sort -->
    <script type='text/javascript'>//<![CDATA[

$(window).on('load', function(){
    $('.shower').hide()
})
//]]> 
    </script>
</head>
<body>
  <h1>Colour analysis of <em>Illustrated London News</em> front covers</h1>
  <h2>Calendar view</h2>
  <p>Display the most common colour of each issue's cover in a table, with the colour data. See also <a href="table.html">advanced table view</a> and the <a href="https://philreeddata.github.io/dhll201705/london.html" target="_blank">project page</a>.</p>
"""
    # CALENDAR
    first = True
    y = 0
    yPrev = 0 # year for previous issue
    m = 0
    d = 0
    r = 255
    g = 255
    b = 255
    html = html + """
  <div id="main">
    <div id="colorCalendar">
"""
    with open(csvFilename, 'r') as csvFile:
        colorReader = csv.reader(csvFile, delimiter=',')
        # skip first row header
        next(colorReader)
        for row in colorReader:
            if len(row) == 6:
                yPrev = y
                y = row[0]
                years.add(y)
                m = row[1]
                d = row[2]
                r = row[3]
                g = row[4]
                b = row[5]
                h, l, s = colorsys.rgb_to_hls(float(r)/255.0, float(g)/255.0, float(b)/255.0)
                h = int(h*360)
                l = int(l*100)
                s = int(s*100)

                if y != yPrev:
                    if not first:
                        html = html + "</div>" # end <div class='year'>
                    else:
                        first = False
                    # start new year 'column'
                    html = html + "<div class='yearCol' id='yearCol"+y+"'><h4>"+ y+"</h4>"

                html = html + "        <div style='background-color: rgb("+r+", "+g+", "+b+")' class='issue year"+y+" month"+m +"'>"
                html = html + "<p>"+m.zfill(2)+"-"+d.zfill(2)+"</p>"
                yyyymmdd = y.zfill(4)  + m.zfill(2)  + d.zfill(2) 
                link = "http://find.galegroup.com/iln/browseIssue.do?prodId=ILN&userGroupName=jrycal5&tabID=T004&method=doBrowseIssue&mcode=3IUM&dp="+yyyymmdd+"&docPage=page&fromPage=browseIssuePage&specialIssues=no&searchType=BasicSearchForm"
                html = html + "<p class='viewLink'> <a href='" + link + "'>view</a> </p>"
                html = html + """</div>
"""
            else:
                html= html+ """        <div class="error">ERR</div>
"""
        html = html + "</div>" # end <div class='year'>
    html = html + """
    </div>
  </div>
"""
    # CONTROLS
    html = html + """
  <div id="controls">
    <h2>Controls</h2>
    <h3>Scale</h3>
    <p>
        <input type="button" value="Small" onclick="$('.issue').css({'width':'2em','height':'0.5em','font-size':'smaller'}); $('.yearCol h4').css('font-size','smaller');" />
        <input type="button" value="Medium" onclick="$('.issue').css({'width':'3.5em','height':'1.3em','font-size':'smaller'}); $('.yearCol h4').css('font-size','inherit');" />
        <input type="button" value="Large (default)" onclick="$('.issue').css({'width':'6em','height':'2em','font-size':'inherit'}); $('.yearCol h4').css('font-size','inherit');" />
    </p>
    <h3>Grid</h3>
    <p>
    <input type="button" value="None" onclick="$('.issue').css('margin','0');" />
        <input type="button" value="Thin (default)" onclick="$('.issue').css('margin','0.1em');" />
        <input type="button" value="Thick" onclick="$('.issue').css('margin','0.3em');" />
    </p>
    <h3>Wrap</h3>
    <p>
        <input type="button" value="No wrap" onclick="$('#colorCalendar').css('width','300em');" />
        <input type="button" value="Wrap (default)" onclick="$('#colorCalendar').css('width','inherit');" />
    </p>
    <h3>Background</h3>
    <p>
        <input type="button" value="White (default)" onclick="$('#main').css('background-color','white');  $('#colorCalendar').css('color','white'); $('#colorCalendar h4').css('color','black');" />
        <input type="button" value="Black" onclick="$('#main').css('background-color','black');  $('#colorCalendar').css('color','black'); $('#colorCalendar h4').css('color','white');" />        
    </p>
  </div>
"""
    
    # FOOT
    html = html + """
</body>
</html>   
"""
    return (html)

def save_html_to_file(html, outFilename):
    with open(outFilename, 'w') as outFile:
        outFile.write(html)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        csvFilename = sys.argv[1]
        html = create_calendara_page(csvFilename)
        outFilename = "calendara.html"
        if len(sys.argv) > 2:
            outFilename = sys.argv[2]
        save_html_to_file(html, outFilename)
        print ('read from ' + csvFilename + ' and written to ' + outFilename)
    else:
        print ('usage: create_calendara_page.py INFILENAME.csv OUTFILENAME.html')
        print ('prints a calendar (type A) HTML file of the given CSV data.')
        
