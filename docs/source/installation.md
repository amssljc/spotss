## Installation
``` shell
$ git clone https://github.com/YangLabHKUST/SpatialScope.git
$ cd SpatialScope
$ conda env create -f environment.yml
$ conda activate SpatialScope
$ python setup.py develop
# fix bug of squidpy
$ rsync ./src/_feature_mixin.py ~/.conda/envs/SpatialScope/lib/python3.9/site-packages/squidpy/im/_feature_mixin.py
```
check the installation status
```shell
$ python ./src/Cell_Type_Identification.py -h
# or directly if `python setup.py develop` has been run
$ Cell_Type_Identification.py -h
```