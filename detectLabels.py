import boto3
import image_helpers

client = boto3.client('rekognition')

# Dummy image for testing
imgUrl = 'https://www.newreleasetoday.com/images/article_images/art_img_2608.jpg'

imgBytes = image_helpers.get_image_from_url(imgUrl)

result = client.detect_labels(Image={'Bytes': imgBytes})

print(result)