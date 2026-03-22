# AWS-s3-cleanup-lambda
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

Screenshot

<img width="1599" height="445" alt="image" src="https://github.com/user-attachments/assets/9247a42b-e42e-4d82-85ef-c1bbd8ea2ab5" />



### 2. IAM Role
- Created Lambda role
- Attached:
  - AmazonS3FullAccess

### 3. Lambda Function
- Runtime: Python 3.14
- Logic:
  - List objects
  - Check last modified date
  - Delete files older than 30 days

### 4. Testing
- Manually triggered Lambda
- Verified old files deleted

### 5. Final Output Screenshot

<img width="1618" height="403" alt="image" src="https://github.com/user-attachments/assets/4019e797-676a-4313-a716-d20e4bd6f9a5" />


---

## 📂 Project Structure
