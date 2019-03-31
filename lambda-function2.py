from __future__ import print_function

import json
import boto3
from decimal import Decimal
import urllib

rekognition = boto3.client('rekognition', region_name='ap-south-1')
s3 = boto3.client('s3', region_name='ap-south-1')
dynamodb = boto3.resource('dynamodb')


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)    

def lambda_handler(event, context):
    # TODO implement
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(
        event['Records'][0]['s3']['object']['key'].encode('utf8'))
    table=dynamodb.Table('mytest1')  
    response=table.get_item(
        Key={'id':'rekognition-image1'}
        )
    print(response)    
    k1=response['Item']['key']
    


    client = boto3.client('rekognition')
    response1 = client.compare_faces(
        SourceImage={
            'S3Object': {
                'Bucket': 'rekognition-image1',
                'Name': k1
                }
            },
        TargetImage={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
                }
            },
        SimilarityThreshold=90
        
    )
  

    for record in response1['FaceMatches']:
        face = record
        confidence=face['Face']
        print ("Matched With {}""%"" Similarity".format(face['Similarity']))
        print ("With {}""%"" Confidence".format(confidence['Confidence']))
    
        print(response1)
        d=response1
    
        z=d['FaceMatches'][-1].values()
        print("---------------------------------------")
        count=-1
        for  i in z:
        	   count=count+1
        	   if(count==1):
        		   val=i
        if(val>90):
            print("Face is Matched")
        else:
            print("Face Unmatched")
