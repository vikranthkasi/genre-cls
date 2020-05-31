# %%
import boto3
import os

#changing path 
os.chdir('./data')

ACCESS_KEY = 'AKIASH5N5EHTPUNAMB2Y'
SECRET_KEY = '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'
session = boto3.resource('s3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

my_bucket = session.Bucket('genrefiles')

# download file into current directory
for s3_object in my_bucket.objects.all():
    # Need to split s3_object.key into path and file name, else it will give error file not found.
    path, filename = os.path.split(s3_object.key)
    my_bucket.download_file(s3_object.key, filename)

# %%
