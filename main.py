import vectoriser as v
import debug

ubisoft = v.getRgbArray("E:/Projects/Vectoriser/bitmap/hood.png")
grey_ubisoft = v.RgbArrayToGreyscale(ubisoft, "RGB")
debug.saveBitmap(grey_ubisoft, "bitmap/grey.png")

mean_filter = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
grey_ubisoft = v.RgbArrayToGreyscale(ubisoft)
blur_ubisoft = v.applyKernel(grey_ubisoft, mean_filter)
blur_ubisoft = v.GreyscaleArrayToRgb(blur_ubisoft)
debug.saveBitmap(blur_ubisoft, "bitmap/blur.png")
