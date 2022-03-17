import gpxpy
import gpxpy.gpx
import os

gpx_file = open('res/sample.gpx', 'r')

gpx_input = gpxpy.parse(gpx_file)

for i,track in enumerate(gpx_input.tracks):
    gpx_output = gpxpy.gpx.GPX()
    gpx_output.tracks.append(track)
    with open(os.path.dirname(__file__) + "/output/" + str(i) + ".gpx", "w") as f:
        f.write(gpx_output.to_xml())
