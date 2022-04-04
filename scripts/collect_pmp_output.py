import glob
import os
import shutil


#metrics_categories = ["mean_climate", "variability_modes", "enso_metric"]
metrics_categories = ["mean_climate"]
data_directory = "/p/user_pub/pmp/pmp_results/pmp_v1.1.2/metrics_results"
target_directory = "../metrics_results"


def copy_files(src_files, dest):
    for file_name in src_files:
        if os.path.isfile(file_name):
            shutil.copy(file_name, dest)


for metrics in metrics_categories:
    cmips = [os.path.basename(x) for x in sorted(glob.glob(os.path.join(data_directory, metrics, "cmip*")))]
    print('-------------------------------')
    print('metrics:', metrics)
    print('-------------------------------')
    for cmip in cmips:
        exps = [os.path.basename(x) for x in sorted(glob.glob(os.path.join(data_directory, metrics, cmip, "*")))]
        for exp in exps:
            versions = [os.path.basename(x) for x in sorted(glob.glob(os.path.join(data_directory, metrics, cmip, exp, "v????????")))]
            versions.reverse()  # start from latest date
            if metrics == "mean_climate":
                for version in versions:
                    raw_json_files = glob.glob(os.path.join(data_directory, metrics, cmip, exp, version, "*."+version+".json"))
                    if len(raw_json_files) > 20:  # having at least 20 json files under the directory to consider completed
                        # copy files 
                        target_path = os.path.join(target_directory, metrics, cmip, exp, version)
                        os.makedirs(target_path, exist_ok=True)
                        copy_files(raw_json_files, target_path)             
                        print('COPIED: cmip, exp, version, #jsons:', cmip, exp, version, len(raw_json_files)) 
                        break
