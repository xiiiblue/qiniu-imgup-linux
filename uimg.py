# -*- coding: utf-8 -*-

import qiniu
import os, random, string
from config import *


# 生成5位随机文件名
def random_name():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))


# 上传至七牛云
def upload_img(fn, sfx='.jpg'):
    key = random_name() + sfx
    q = qiniu.Auth(QINIU_AK, QINIU_SK)
    token = q.upload_token(QINIU_BUCKET, key, 3600)
    ret, info = qiniu.put_file(token, key, fn)
    if ret != None and ret['key'] == key and ret['hash'] == qiniu.etag(fn):
        return QINIU_DOMAIN + key
    else:
        return False


def run():
    upRes = upload_img('/tmp/snap_shutter.jpg')
    if upRes:
        os.system('上传成功 -t 3000')
        print('![](' + upRes + ')')
    else:
        os.system('上传失败 -t 3000')
        print('UPLOAD FAILED')


if __name__ == '__main__':
    run()
