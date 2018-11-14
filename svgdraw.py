import svgwrite

# Create a SVG object
dwg = svgwrite.Drawing('vector/act.svg', size=(1000, 1000))
# Paste the output from main.py here
data = []
for path in data:
    dwg.add(dwg.path(path, stroke="#000000", fill="#fff"))


# Save file
dwg.save()
