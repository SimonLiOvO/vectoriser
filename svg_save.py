import svgwrite

# Create a SVG object
dwg = svgwrite.Drawing('vector/quincy.svg', size=(300, 300))
# Draw lines
dwg.add(dwg.line((0, 0.5), (100, 0.5), stroke=svgwrite.rgb(10, 10, 16)))
# Draw rect
dwg.add(dwg.rect((0, 0), (30, 20), 2, 20))
# 
dwg.save()