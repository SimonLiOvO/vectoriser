import vectoriser as v
import debug

ubisoft = v.getPixelArray("E:/Projects/Vectoriser/bitmap/hood.png")
# grey_ubisoft = v.getGreyscaleArray(ubisoft, "RGB")
# debug.saveBitmap(grey_ubisoft, "bitmap/grey.png")

mean_filter = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
grey_ubisoft = v.getGreyscaleArray(ubisoft)
blur_ubisoft = v.applyKernel(grey_ubisoft, mean_filter)
blur_ubisoft = v.applyKernel(blur_ubisoft, mean_filter)
blur_ubisoft = v.applyKernel(blur_ubisoft, mean_filter)
blur_ubisoft = v.applyKernel(blur_ubisoft, mean_filter)
blur_ubisoft = v.applyKernel(blur_ubisoft, mean_filter)
blur_ubisoft = v.getRGBArray(blur_ubisoft)
debug.saveBitmap(blur_ubisoft, "bitmap/blur.png")
