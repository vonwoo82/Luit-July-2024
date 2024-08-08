import first_boto3

s3 = boto3.client('s3')

response - s3.generate_presigned_url('get_object', params={'Bucket': "twood-boto3-08072024", 'Key': "test_text.txt"}, ExpriesIn=300)

print(response)

