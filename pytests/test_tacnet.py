import unittest
import os
import torch

from os.path import split, realpath, join
import sys
# hacky way of importing from repo
base_dir = split(split(realpath(__file__))[0])[0]
sys.path.append(base_dir)

import networks.tacnet as t_net

# tests
# ====================================================


class test_tacnet(unittest.TestCase):
    # def setUp(self):
    #     self.csv = join(base_dir, 'dev-data/tactip-127/model_surface2d/targets.csv')
    #     self.image_dir = join(base_dir, 'dev-data/tactip-127/model_surface2d/frames_bw')
    #     self.dataloader = dataloader.get_data(self.csv, self.image_dir)

    def test_can_start(self):
        self.make_and_run_square_net(128)
        self.make_and_run_square_net(256)
        # self.make_and_run_square_net(512)

    def make_and_run_square_net(self, size):
        x = torch.zeros(1,1,size,size)
        net = t_net.network(size)
        out = net.forward(x)






if __name__ == '__main__':
    unittest.main()
