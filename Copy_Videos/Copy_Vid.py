import os

import boto
import boto.s3.connection
import boto3
from boto.s3.connection import S3Connection
import tarfile
import vlc

AWS_ACCESS_KEY_ID = "AKIAQHOX2GYSTS3XQ76J"
AWS_SECRET_ACCESS_KEY = "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"
DEST_BUCKET = "tensorrt-bucket"
OBJECT_NAME = "research_collection/cart_idresearch-cart_cam3_utc_1546870917.7195964.tar"
FILE_NAME = "cart_idresearch-cart_cam3_utc_1546870917.7195964.tar"
OUTPUT_DIR = "/home/teresa/firstVideo"

def test_makeDir():
    current_directory = os.getcwd()
    file_path = current_directory + "/video"
    os.makedirs(file_path)

def test_get_conf():
    print
    #DOWNLOAD VIDEO FROM EC2

    # bashCommand = "scp -i ~/key/tensor_rt_keypair.pem ubuntu@52.51.240.77:/mnt-ebs/input_videos/cart_idruntime-test-cart_cam0_utc_1546874007.3419626.tar ~/AICVideos/"
    # os.popen(bashCommand).read()
    #
    # print os.getcwd()
    # tar = tarfile.open("/home/teresa/AICVideos/cart_idruntime-test-cart_cam0_utc_1546874007.3419626.tar", mode='r')
    # for member in tar.getmembers():
    #     if member.isreg():  # skip if the TarInfo is not files
    #         member.name = os.path.basename(member.name)  # remove the path by reset it
    #         tar.extract(member, OUTPUT_DIR)  # extract
    # player = vlc.MediaPlayer("/home/teresa/firstVideo/19-05-12_18-13-27_motion.h264")
    # player.play()
    # while True:
    #     pass
#################################################################
    # DOWNLOAD VIDEO FROM S3
    client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    client.download_file(DEST_BUCKET, OBJECT_NAME, "/home/teresa/AICVideos/vid1.tar")
    tar = tarfile.open("/home/teresa/AICVideos/vid1.tar", mode='r')
    for member in tar.getmembers():
        if member.isreg():  # skip if the TarInfo is not files
            member.name = os.path.basename(member.name)  # remove the path by reset it
            tar.extract(member, OUTPUT_DIR)  # extract
    player = vlc.MediaPlayer("/home/teresa/firstVideo/19-05-12_17-21-57_motion.h264")
    player.play()
    while True:
        pass
