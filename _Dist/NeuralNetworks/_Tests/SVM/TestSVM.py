import os
import sys
root_path = os.path.abspath("../../../../")
if root_path not in sys.path:
    sys.path.append(root_path)

from copy import deepcopy

from Util.Util import DataUtil
from _Dist.NeuralNetworks._Tests.TestUtil import draw_acc
from _Dist.NeuralNetworks.f_AutoNN.NN import AutoAdvanced
from _Dist.NeuralNetworks.b_TraditionalML.SVM import SVM, AutoSVM

base_params = {"model_param_settings": {"n_epoch": 30}}
(x, y), (x_test, y_test) = DataUtil.gen_noisy_linear(n_dim=2, n_valid=2, test_ratio=0.01, one_hot=False)
svm = SVM(**deepcopy(base_params)).fit(
    x, y, x_test, y_test, snapshot_ratio=0).visualize2d(x_test, y_test)
nn = AutoAdvanced("NoisyLinear", **deepcopy(base_params)).fit(
    x, y, x_test, y_test, snapshot_ratio=0).visualize2d(x_test, y_test)
draw_acc(svm, nn)

base_params["data_info"] = {"data_folder": "../_Data"}
svm = AutoSVM("mushroom", **deepcopy(base_params)).fit(snapshot_ratio=0)
nn = AutoAdvanced("mushroom", **deepcopy(base_params)).fit(snapshot_ratio=0)
draw_acc(svm, nn)