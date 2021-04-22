from swf.movie import SWF
from swf.export import SVGExporter


file = open('/Users/swar/Downloads/testswf.swf', 'rb')

# load and parse the SWF
swf = SWF(file)

# create the SVG exporter
svg_exporter = SVGExporter()

# export!
svg = swf.export(svg_exporter)

# save the SVG
open('/Users/swar/Downloads/testswf.svg', 'wb').write(svg.read())