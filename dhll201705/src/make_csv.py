# Read the file structure for all images
# Get the RGB values
# Write to CSV file
# I hard coded the path to read from as a temporary measure

import csv
import glob

from PIL import Image

startYear = 1964
endYear = 2003

def average_image_color(filename):
	i = Image.open(filename)
	h = i.histogram()

	# split into red, green, blue
	r = h[0:256]
	g = h[256:256*2]
	b = h[256*2: 256*3]

	# perform the weighted average of each channel:
	# the *index* is the channel value, and the *value* is its weight
	return (
		sum( i*w for i, w in enumerate(r) ) / sum(r),
		sum( i*w for i, w in enumerate(g) ) / sum(g),
		sum( i*w for i, w in enumerate(b) ) / sum(b)
	)

def make_csv(fileOut='generated.csv'):
    with open(fileOut, 'wb') as f: # for Python 3, change to 'w', newline=''
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['y','m','d','r','g','b'])
        
        # It won't read the directory from the command line correctly! Hard-code it...
        for year in range(startYear, endYear+1):
            print('Reading year ' +str(year))
            imagePaths1Year = glob.glob('i:/IllustratedLondonNews/' + str(year) + '/*/ILN0-????-????-0001.JPG')
            for imagePath in imagePaths1Year:
                y = imagePath[-18:-14]
                m = imagePath[-13:-11]
                d = imagePath[-11:-9]
                r,g,b = average_image_color(imagePath)
                writer.writerow([y,m,d,r,g,b])
    print('Written to ' + fileOut)


if __name__ == '__main__':
    make_csv()
    #print ('usage: make_csv.py')
