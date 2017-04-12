import csv
import colorsys

def create_table_page(csvFilename):
    # Do header, table (from CSV file) then footer
    years = set([])
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # HEAD
    html = """
<!html>
<html>
<head>
    <title>ILN Cover main colour: Table view</title>
    <link href="https://fonts.googleapis.com/css?family=Lora:400,400i,700,700i" rel="stylesheet" />
    <style>
        * {font-family: 'Lora', serif;} 
        h1, h2, h3, th {font-weight: bold;}
        #main {float: left; padding-right: 5em;}
        #controls {float: left;}
        a, a:visited, a:hover {color: black}
        th {text-align: right;} 
        td {color: white; text-align: right;} 
        th:nth-of-type(3), td:nth-of-type(3) { padding-right: 10em;} 
        td.viewLink {background-color: white !important;}
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
    <!-- Table sorting from http://stackoverflow.com/questions/3160277/jquery-table-sort -->
    <script type='text/javascript'>//<![CDATA[

$(window).on('load', function(){
    $('.shower').hide()
})
$(window).on('load', function(){
$('th').click(function(){
    var table = $(this).parents('table').eq(0)
    var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
    this.asc = !this.asc
    if (!this.asc){rows = rows.reverse()}
    for (var i = 0; i < rows.length; i++){table.append(rows[i])}
})
function comparer(index) {
    return function(a, b) {
        var valA = getCellValue(a, index), valB = getCellValue(b, index)
        return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB)
    }
}
function getCellValue(row, index){ return $(row).children('td').eq(index).html() }
});//]]> 
    </script>
</head>
<body>
  <h1>Colour analysis of <em>Illustrated London News</em> front covers</h1>
  <h2>Table view</h2>
  <p>Display the most common colour of each issue's cover in a table, with the colour data. See also <a href="calendara.html">simple calendar view</a> and the <a href="https://philreeddata.github.io/dhll201705/london.html" target="_blank">project page</a>.</p>
"""
    # TABLE
    y = 0
    m = 0
    d = 0
    r = 255
    g = 255
    b = 255
    html = html + """
  <div id="main">
    <table id="colorTable">
    <thead>
        <tr><th>year</th><th>month</th><th>day</th><th>red</th><th>green</th><th>blue</th><th>hue (&deg;)</th><th>sat (%)</th><th>lum (%)</th><th>link</th></tr>
    </thead>
    <tbody>
"""
    with open(csvFilename, 'r') as csvFile:
        colorReader = csv.reader(csvFile, delimiter=',')
        # skip first row header
        next(colorReader)
        for row in colorReader:
            if len(row) == 6:
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
                html = html + "        <tr style='background-color: rgb("+r+", "+g+", "+b+")' class='year"+y+" month"+m +"'>"
                #for cell in row:
                #    html = html + "<td>"+cell+"</td>"
                html = html + "<td>"+y+"</td><td>"+m+"</td><td>"+d+"</td>"
                html = html + "<td style='background-color: rgb("+r+",0,0)'>"+r+"</td>"
                html = html + "<td style='background-color: rgb(0,"+g+",0)'>"+g+"</td>"
                html = html + "<td style='background-color: rgb(0,0,"+b+")'>"+b+"</td>"
                html = html + "<td style='background-color: hsl("+str(h)+",50%,50%)'>"+str(h)+"</td>"
                html = html + "<td style='background-color: hsl(0,"+str(s)+"%,0%)'>"+str(s)+"</td>"
                html = html + "<td style='background-color: hsl(0,0%,"+str(l)+"%)'>"+str(l)+"</td>"
                yyyymmdd = y.zfill(4)  + m.zfill(2)  + d.zfill(2) 
                link = "http://find.galegroup.com/iln/browseIssue.do?prodId=ILN&userGroupName=jrycal5&tabID=T004&method=doBrowseIssue&mcode=3IUM&dp="+yyyymmdd+"&docPage=page&fromPage=browseIssuePage&specialIssues=no&searchType=BasicSearchForm"
                html = html + "<td class='viewLink'><a href='" + link + "'>view "+yyyymmdd+ "</a>"
                html = html + """</tr>
"""
            else:
                html= html+ """        <tr class="error"><td>ERR</td><td>ERR</td><td>ERR</td><td>-</td><td>-</td><td>-</td></tr>
"""
    html = html + """
    </tbody></table>
  </div>
"""
    # CONTROLS
    html = html + """
  <div id="controls">
    <h2>Controls</h2>
      <p>Click column headings to sort.</p>
      <h3>Years</h3>
      <ul>
"""
    for year in sorted(years):
        #html = html + "<li><a href=\"#\" onclick=\"$('.year" + year + "').toggle(); return false;\">show/hide</a> " + year + "</li>"
        html = html + "<li><a class=\"shower\" id=\"showyear" + year + "\" href=\"#\" onclick=\""
        html = html + "$('.year" + year + "').show(); $('#hideyear"+year+"').show(); $(this).hide(); return false;"
        html = html + "\">show</a> "
        html = html + "<a class=\"hider\" id=\"hideyear" + year + "\" href=\"#\" onclick=\""
        html = html + "$('.year" + year + "').hide(); $('#showyear" + year+"').show(); $(this).hide(); return false;"
        html = html + "\">hide</a> " + year + "</li>\n"
    
    html = html + """
      </ul>
      
      <h3>Months</h3>
      <ul>
"""
    for monthNum, monthName in enumerate(months):
        monthNumPlus1 = str(monthNum+1)
        #html = html + "<li><a href=\"#\" onclick=\"$('.month"+ monthNumPlus1 +  "').toggle(); return false;\">show/hide</a> " + monthName + "</li>"
        html = html + "<li><a class=\"shower\" id=\"showmonth" + monthNumPlus1 + "\" href=\"#\" onclick=\""
        html = html + "$('.month" + monthNumPlus1 + "').show(); $('#hidemonth"+monthNumPlus1+"').show(); $(this).hide(); return false;"
        html = html + "\">show</a> "
        html = html + "<a class=\"hider\" id=\"hidemonth" + monthNumPlus1 + "\" href=\"#\" onclick=\""
        html = html + "$('.month" + monthNumPlus1 + "').hide(); $('#showmonth" + monthNumPlus1+"').show(); $(this).hide(); return false;"
        html = html + "\">hide</a> " + monthName + "</li>\n"
    html = html + """
      </ul>
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
        html = create_table_page(csvFilename)
        outFilename = "table.html"
        if len(sys.argv) > 2:
            outFilename = sys.argv[2]
        save_html_to_file(html, outFilename)
        print ('read from ' + csvFilename + ' and written to ' + outFilename)
    else:
        print ('usage: create_table_page.py INFILENAME.csv OUTFILENAME.html')
        print ('prints a coloured table HTML file of the given CSV data.')
        
