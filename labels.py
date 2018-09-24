import boto3
import image_helpers

client = boto3.client('rekognition')

#imgurl = 'https://www.parrots.org/images/uploads/dreamstime_C_47716185.jpg'
#imgurl = 'http://www.gstatic.com/tv/thumb/persons/673351/673351_v9_ba.jpg'

# grab the image from online
def get_labels(imgurl):
	img = image_helpers.get_image_from_url(imgurl)

	exp = client.detect_labels(Image={'Bytes': imgbytes},
	                               MinConfidence=50)
	return (exp['Labels'])
