from labels import get_labels
from face_detect import faceDetect
from celebs import celeb

imgurl = "https://i.pinimg.com/originals/0a/39/1f/0a391ff95f731673bea99f40ca25ba46.jpg"

def create_strings(imgurl):
	labels = get_labels(imgurl)
	face = faceDetect(imgurl)
	celebstr = celeb(imgurl)

	labelstr = "Objects detected in the image are:\n"
	facestr = ""
	

	for i in labels:
		labelstr += i['Name'] + " with confidence " + str(i['Confidence']) +",\n"

	if face:
		facestr += "The attributes for faces found in the image are as follows: \n\n" + face[0] + ",\n\n"
		facestr += "Number of faces detected in the image are" + str(face[1]) + "\n\n"
	else:
		facestr += " \n\n"


	return [labelstr,facestr,celebstr]




