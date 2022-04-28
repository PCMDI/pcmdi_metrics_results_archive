# Collect individual model json file for user-model visualization demo

import shutil 
import glob
import os
import copy
import json

# mean climate

mip = "cmip6"
exp = "historical"
model = "E3SM-1-0"
version = "v20201008"

file_template = os.path.join(
    "/p/user_pub/pmp/pmp_results/pmp_v1.1.2/metrics_results/mean_climate/",
    mip, exp, version, '*',
    '*'+model+'*.'+version+'.json')

dst_dir = "../test_case/mean_climate/"

files = glob.glob(file_template)

# copy original file with new file name
for src in files:
    var = src.split('/')[-1].split('.')[1]
    dst_filename = '.'.join(['my_model', var, 'regrid2.2p5x2p5.json'])
    dst = os.path.join(dst_dir, dst_filename)
    shutil.copy2(src, dst)
    print(src, dst)

# rewrite (overwrite) new files with new model name included 
new_files = glob.glob(os.path.join(dst_dir, 'my_model.*.json'))

for json_file in new_files:
    with open(json_file) as fj:
        dict_temp = json.load(fj)
    dict_temp['RESULTS']['my_model'] = copy.deepcopy(dict_temp['RESULTS']['E3SM-1-0'])
    del dict_temp['RESULTS']['E3SM-1-0']
    with open(json_file, "w") as outfile:
        json.dump(dict_temp, outfile, indent=4, sort_keys=True)
