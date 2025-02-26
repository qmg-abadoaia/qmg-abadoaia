import boto3
import os

def lambda_handler(event, context):
    source_bucket = 'source_bucket_name'
    destination_bucket = 'destination_bucket_name'
    file_key = 'file_key'
    
    s3 = boto3.client('s3')
    
    try:
        # Copy the file to the destination bucket
        copy_source = {'Bucket': source_bucket, 'Key': file_key}
        s3.copy_object(Bucket=destination_bucket, Key=file_key, CopySource=copy_source)
        
        # Delete the original file from the source bucket
        s3.delete_object(Bucket=source_bucket, Key=file_key)
        
        print(f"File {file_key} moved from {source_bucket} to {destination_bucket}")
        return {
            'statusCode': 200,
            'body': f"File {file_key} moved successfully!"
        }
    except Exception as e:
        print(f"Error moving file: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error moving file: {str(e)}"
        }
