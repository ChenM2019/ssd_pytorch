import os.path as osp
sk = [ 15, 30, 60, 111, 162, 213, 264 ]
feature_map = [ 38, 19, 10, 5, 3, 1 ]
steps = [ 8, 16, 32, 64, 100, 300 ]
image_size = 300
aspect_ratios = [[2], [2, 3], [2, 3], [2, 3], [2], [2]]
MEANS = (104, 117, 123)
batch_size = 32
data_load_number_worker = 4
lr = 1e-3
momentum = 0.9
weight_decacy = 5e-4
gamma = 0.1
VOC_ROOT = osp.join('./', "VOCdevkit/")
dataset_root = VOC_ROOT
use_cuda = True
lr_steps = (80000, 100000, 120000)
max_iter = 120000