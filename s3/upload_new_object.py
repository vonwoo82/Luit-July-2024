import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket="twood-boto3-08072024")
                Key="folder/foldera/folder1/test_text_string.txt",
                Body="Hey this is a string",
                ContentType="text/plain")
