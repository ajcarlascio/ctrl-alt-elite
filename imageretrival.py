import boto3
import json
import urllib.parse
import base64
from botocore.exceptions import ClientError
import os
import datetime;
 
# ct stores current time

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

HTTP_BAD_REQUEST = {'statusCode': 400}
HTTP_OK = {'statusCode': 200}

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use timestamp
    if object_name is None:
        ct = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        object_name = os.path.basename(ct + '.jpg')
    # Upload the file
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        return False
    return object_name

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    if event.get('routeKey'):
        print("api call")
        img_data = event.get('body')
        if event.get('isBase64Encoded'):
            print("here")
            with open("/tmp/result.jpg", "wb") as fh:
                fh.write(base64.decodebytes(bytes(img_data, 'utf-8')))
                file_name = upload_file("/tmp/result.jpg", "ctrl-alt-elite")
            if file_name:
                try:
                    bucket = 'ctrl-alt-elite'
                    key = file_name
                    response = rekognition.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':key}},
                    MaxLabels=10)
                    return {'result': response}
                except Exception as e:
                    print(e)
                    print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
                    raise e
    return HTTP_BAD_REQUEST