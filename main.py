# import os
import csv
import json
import tempfile
from google.cloud import storage
from flask import Flask
app = Flask(__name__)



@app.route('/penguin')
def penguin():
    with tempfile.TemporaryDirectory() as temp_path:
        write_path = temp_path + '/arxiv.json'
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=''
        client = storage.Client()
        bucket_name = "penguin-first"
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob('penguin.json')
        blob.download_to_filename(write_path)
        with open(write_path, encoding='unicode-escape') as f:
            article = f.read()
            return article




if __name__ == '__main__':
    app.run()
