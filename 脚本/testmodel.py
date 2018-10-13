#!/usr/bin/env python
#_*_coding=utf-8_*_

#########################
# >File Nime: testmodel.py
# >author: ly
# >email: 406728295@qq.com
#########################
import numpy as np 
import sys 

caffe_root='/home/jsj/caffe/'
sys.path.insert(0,caffe_root + 'python')

import caffe

caffe.set_mode_cpu()

model_def = '/home/jsj/xytest/model/deploy.prototxt'
model_weights = '/home/jsj/xytest/model/iter_13000.caffemodel'

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)
mu = np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mu.mean(1).mean(1)
print('mean-subtracted values:',zip('BGR',mu))

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # 通道变换，例如从(530,800,3) 变成 (3,530,800)
transformer.set_mean('data', mu) #
transformer.set_raw_scale('data', 255)  # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2, 1, 0))  # swap channels from RGB to BGR

net.blobs['data'].reshape(1,
                          3,
                          227,227)

image = caffe.io.load_image('/home/jsj/xytest/test_image/red_100.jpg')
transformed_image = transformer.preprocess('data', image)
net.blobs['data'].data[...] = transformed_image

output = net.forward()

output_prob = output['prob'][0]

print('predicted class is:',output_prob.argmax())