import boto3
import image_helpers

client = boto3.client('rekognition')

# Dummy image for testing
imgUrl = 'https://thenypost.files.wordpress.com/2018/10/johnny_english_strikes_again.jpg?quality=90&strip=all&w=618&h=410&crop=1'

imgBytes = image_helpers.get_image_from_url(imgUrl)

result = client.detect_labels(Image={'Bytes': imgBytes},
                              Attributes=['ALL'])

print(result)