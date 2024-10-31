from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.s3 import S3StaticStorage


class MediaStorage(S3Boto3Storage):
    location = 'event-planner-team-3-media'


class StaticStorage(S3StaticStorage):
    location = 'event-planner-team-3-static'