# aws-s3-cleanup-lambda
aws-s3-cleanup-lambda to clean files older than 30 days in S3 bucket
# AWS S3 Cleanup using Lambda & Boto3

## 📌 Objective
Automatically delete files older than 30 days from an S3 bucket.

---

## 🛠️ Services Used
- AWS S3
- AWS Lambda
- IAM
- Python (Boto3)

---

## ⚙️ Setup Steps

### 1. S3 Bucket
- Created bucket
- Uploaded sample files

### 2. IAM Role
- Created Lambda role
- Attached:
  - AmazonS3FullAccess

### 3. Lambda Function
- Runtime: Python 3.x
- Logic:
  - List objects
  - Check last modified date
  - Delete files older than 30 days

### 4. Testing
- Manually triggered Lambda
- Verified old files deleted

---

## 📂 Project Structure
