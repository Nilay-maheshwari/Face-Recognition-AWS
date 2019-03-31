# Face-Recognition-AWS
This is a face recognition  project built on AWS cloud using Rekognition , s3 , lambda , DynamoDB , Cloudwatch as a service


create a lambda role with policies :s3 fullaccess, dynamodb fullaccess, Rekognition, cloudwatch fullaccess or cloudwatch log access
upload image 1 in recognition-image1, this will trigger a lambda funtion where we have applied s3 trigger.
From this lambda function we are uploading that image's key and bucket name in dynamodb table using putitem function.
upload image 2 in recognition-image2,this will trigger  a lambda function where we have applied s3 trigger.
From this lambda function we are fetching the image key from the dynamodb table using get item function, now we have both the images so apply comparefaces function
check the response in cloudwatch
fetch the similarity from the response and label them as FACE MATCHED or FACE NOT MATCHED.
