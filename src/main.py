import gpxpy
import gpxpy.gpx
import os
import regex

gpx_file = open('res/sample.gpx', 'r')

gpx_input = gpxpy.parse(gpx_file)

for track in gpx_input.tracks:
    gpx_output = gpxpy.gpx.GPX()
    gpx_output.tracks.append(track)
    result = regex.search(r'ref=\K(.*)', gpx_output.to_xml()) 
    with open(os.path.dirname(__file__) + "/output/" + str(result[0]) + ".gpx", "w") as f:
        f.write(gpx_output.to_xml())
