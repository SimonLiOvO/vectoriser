import vectoriser as v
import debug

ubisoft = v.getPixelArray("E:/Projects/Vectoriser/bitmap/hood.png")
grey_ubisoft = v.getGreyscaleArray(ubisoft, "RGB")
debug.saveBitmap(grey_ubisoft, "bitmap/grey.png")