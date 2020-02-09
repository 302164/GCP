import os
import tempfile

from google.cloud import storage
from wand.image import Image

storage_client = storage.Client()


def transform_images(data, context):
    file_data = data

    file_name = file_data['name']
    bucket_name = file_data['bucket']

    blob = storage_client.bucket(bucket_name).get_blob(file_name)

    _, temp_local_filename = tempfile.mkstemp()
    blob.download_to_filename(temp_local_filename)
    print('Image' + file_name + 'downloaded to' + temp_local_filename + '.')
    with Image(filename=temp_local_filename) as image:
        image.resize(500, 500)
        image.save(filename=temp_local_filename)

    blur_bucket_name = 'gcp-project2-266914_bucket2'
    blur_bucket = storage_client.bucket(blur_bucket_name)
    new_blob = blur_bucket.blob(file_name)
    new_blob.upload_from_filename(temp_local_filename)

    # Delete the temporary file.
    os.remove(temp_local_filename)
