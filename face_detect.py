import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition',region_name = 'us-west-2')

#imgurl = 'http://media.comicbook.com/uploads1/2015/07/fox-comic-con-panel-144933.jpg'
imgurl = 'http://www.gstatic.com/tv/thumb/persons/673351/673351_v9_ba.jpg'

def faceDetect(imgurl):

    imgbytes = image_helpers.get_image_from_url(imgurl)

    exp = client.detect_faces(Image={'Bytes': imgbytes},
                                  Attributes=['ALL'])


    numfaces = len(exp['FaceDetails'])
    

    for facedeets in exp['FaceDetails']:

        # construct a printf (almost) style format string for printing the info
        fmtstr = '{gender} age {lowage}-{highage},'

        # mustache and beard detection
        if facedeets['Mustache']['Value'] and facedeets['Beard']['Value']:
            fmtstr += ' with beard and mustache,'
        elif facedeets['Mustache']['Value']:
            fmtstr += ' with mustache,'
        elif facedeets['Beard']['Value']:
            fmtstr += ' with beard,'

        # sunglasses/eyeglasses detection
        if facedeets['Sunglasses']['Value']:
            fmtstr += ' wearing sunglasses,'
        elif facedeets['Eyeglasses']['Value']:
            fmtstr += ' wearing glasses,'

        fmtstr += ' looks {emotion}'

        return(
            fmtstr.format(
                gender=facedeets['Gender']['Value'],
                lowage=facedeets['AgeRange']['Low'],
                highage=facedeets['AgeRange']['High'],
                emotion=facedeets['Emotions'][0]['Type'].lower()
            ), numfaces
        )


