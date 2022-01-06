import SSIMComparison
import Firebase
import logoIdentifier
from logoDatabase import get_by_name
from storeDatabase import get_by_productname
from PIL import Image
import requests
import numpy
import io

img = Image.open(requests.get(Firebase.getImage(), stream=True).raw)
buf = io.BytesIO()
img.save(buf, format='JPEG')
imgByte = buf.getvalue()
brand = logoIdentifier.detect_logos(imgByte)


img = numpy.array(img, dtype=numpy.float64)
products = {}

logonameOutput = get_by_name(brand)
for product in logonameOutput: 
    products[product.link] = product.productname

imgList = list(products.keys())

def productMatch(inputImg, imgList):
    global products
    SSIMValues = {}
    
    for link in imgList:
        comparisonImg = Image.open(requests.get(link, stream=True).raw)
        comparisonImg = numpy.array(img, dtype=numpy.float64)
        SSIMValues[link] = SSIMComparison.compareImages(inputImg, comparisonImg)

    return products[min(SSIMValues)]

finalProduct = "".join(productMatch(img, imgList).split(" "))

storeOutput = get_by_productname(finalProduct)
print(storeOutput)
storePrices = {}

for store in storeOutput:
    storePrices['StoreName'] = store.storename
    storePrices['Price'] = store.productprice
print(storePrices)

Firebase.convertToCSV(storePrices)
Firebase.uploadOutput()

