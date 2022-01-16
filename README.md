### Backend server for generating presigned urls for uploading objects to an Amazon S3 bucket.

To start, run:
```
docker-compose up --build
```

To get a presigned URL, run
```bash
curl -X POST http://localhost:8000/get-presigned-url/ \
   -H "Content-Type: application/json" \
   -d '{"object_name": "foo", "type": "image/jpeg"}' 
```

The response should look something like this:
```json
{
    "url": "https://<your_s3_bucket>.s3.amazonaws.com/",
    "fields": {
        "acl": "public-read",
        "Content-Type": "image/jpeg",
        "key": "foo",
        "x-amz-algorithm": "AWS4-HMAC-SHA256",
        "x-amz-credential": "",
        "x-amz-date": "",
        "policy": "",
        "x-amz-signature": ""
    }
}
```

You can use the [client](https://github.com/andrekrosby92/ak-demo-aws-s3-presigned-url-client) to test the full upload.
