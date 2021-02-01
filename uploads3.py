import boto3

AWS_S3_CREDS = {
    "aws_access_key_id":"AKIAJ4Z7TGFDCBEMMYJQ",
    "aws_secret_access_key":"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"
}
s3_client = boto3.client('s3', **AWS_S3_CREDS)

if __name__ == "__main__":
    s3_client.upload_file('C:\\Users\\tempsubas\\apps.csv', 'appssulfi', 'apps.csv')