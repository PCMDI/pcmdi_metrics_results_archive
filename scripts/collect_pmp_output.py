import glob
import os
import shutil


#metrics_categories = ["mean_climate", "variability_modes", "enso_metric"]
#metrics_categories = ["mean_climate"]
metrics_categories = ["variability_modes"]
data_directory = "/p/user_pub/pmp/pmp_results/pmp_v1.1.2/metrics_results"
target_directory = "../metrics_results"


def copy_files(src_files, target_path):
    os.makedirs(target_path, exist_ok=True)
    for src_file in src_files:
        if os.path.isfile(src_file):
            if not os.path.isfile(os.path.join(target_path, os.path.basename(src_file))):
                shutil.copy(src_file, target_path)


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
                        copy_files(raw_json_files, target_path)             
                        print('Collected: cmip, exp, version, #jsons:', cmip, exp, version, len(raw_json_files)) 
                        break
            elif metrics == "variability_modes":
                for version in versions:
                    modes = [os.path.basename(x) for x in sorted(glob.glob(os.path.join(data_directory, metrics, cmip, exp, version, "*")))]
                    # print(cmip, exp, version, modes)
                    if exp in ['historical', '20c3m']:
                        num_all_modes = 7
                    elif exp in ['amip']:
                        num_all_modes = 5
                    if len(modes) == num_all_modes:
                        for mode in modes:
                            obss = [os.path.basename(x) for x in sorted(glob.glob(os.path.join(data_directory, metrics, cmip, exp, version, mode, "*")))]
                            for obs in obss:
                                raw_json = glob.glob(os.path.join(data_directory, metrics, cmip, exp, version, mode, obs, "*_allModels_allRuns_1900-2005.json"))
                                if len(raw_json) > 0:
                                    target_path = os.path.join(target_directory, metrics, cmip, exp, version, mode, obs)
                                    copy_files(raw_json, target_path)
                                    print('Collected: cmip, exp, version, mode, obs:', cmip, exp, version, mode, obs)