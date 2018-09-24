import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

# grab the image from online
# imgurl = 'https://media1.popsugar-assets.com/files/thumbor/xptPz9chB_kMwxzqI9qMCZrK_YA/fit-in/1024x1024/filters:format_auto-!!-:strip_icc-!!-/2015/07/13/766/n/1922398/3d3a7ee5_11698501_923697884352975_2728822964439153485_n.jpg'
# imgurl = 'http://media.comicbook.com/uploads1/2015/07/fox-comic-con-panel-144933.jpg'
#imgurl = 'http://www.gstatic.com/tv/thumb/persons/673351/673351_v9_ba.jpg'

def celeb(imgurl):
	img = image_helpers.get_image_from_url(imgurl)

	exp = client.recognize_celebrities(Image={'Bytes': img})
	
	try:
		Name = exp['CelebrityFaces'][0]['Name']
		Confidence = exp['CelebrityFaces'][0]['MatchConfidence']
		return "Found Celebrity is " + Name + " with confidence: " + str(Confidence) + " percent!"
	except:
		return ""
