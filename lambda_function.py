import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = 'rajendrahvs3bkt0001'  # BUCKET NAME

    # Define 30 days threshold
    now = datetime.now(timezone.utc)
    threshold = now - timedelta(days=30)

    # List objects
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    deleted_files = []

    for obj in response['Contents']:
        file_name = obj['Key']
        last_modified = obj['LastModified']

        if last_modified < threshold:
            s3.delete_object(Bucket=bucket_name, Key=file_name)
            deleted_files.append(file_name)
            print(f"Deleted: {file_name}")

    if not deleted_files:
        print("No old files to delete")

    return {
        'statusCode': 200,
     'body': f"Deleted files: {deleted_files}"
    }
