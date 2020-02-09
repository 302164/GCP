
import base64
from google.cloud import storage, vision
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

storage_client = storage.Client()
client = vision.ImageAnnotatorClient()


def detect_text(event, context):
	fi = base64.b64decode(event['data']).decode('utf-8')
	bucket_name = 'gcp-project2-266914_bucket1'

	blob_uri = 'gs://' + bucket_name + '/' + fia

	old_link = 'https://storage.cloud.google.com/gcp-project2-266914_bucket1/' + fi
	new_l = 'https://storage.cloud.google.com/gcp-project2-266914_bucket2/' + fi

	image = vision.types.Image()
	image.source.image_uri = blob_uri
	response = client.text_detection(image=image)
	texts = response.text_annotations
    
    
	message = Mail(
    	from_email='302164@student.mini.pw.edu.pl',
    	to_emails='kulp900101@outlook.com',
    	subject='gcp project',
    	html_content=old_link+'<br>' +'<br>' +new_l+'<br>'+'<br>' +'no word found')
    	#html_content=old_link+'<br>' +'<br>' +new_l+'<br>'+'<br>' +str(texts[0].description))
        
        #TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
        #IndexError: list index (0) out of range

	k = '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'
	sg = SendGridAPIClient(k)
	response = sg.send(message)
