

# aws 사용 

# 간략한 사용 흐름

# boto3 ?

# - Python용 AWS SDK

# put_object ?

# upload 하기 위한 함수

import boto3

def upload_s3(template):
      
        # try:

        if True:
            BUCKET_NAME = 'junjoy.kr'
            s3 = boto3.client('s3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )
                

            key = 'joy/' + str(uuid.uuid4()).replace('-','')[0:15] + '.html'
            html_object = '<meta charset="utf-8">' + template

            s3.put_object(
                Body=html_object,
                Bucket=BUCKET_NAME,
                Key = key,
                ContentType="text/html",
            )
            url = 'https://junjoy.kr/' + key

        # except:
        #     url = None

        
        return url