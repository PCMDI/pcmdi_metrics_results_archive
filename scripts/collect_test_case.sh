# Collect individual model json file for user-model visualization demo

# mean climate

mip="cmip6"
exp="historical"
model="E3SM-1-0"
version="v20201008"

cp /p/user_pub/pmp/pmp_results/pmp_v1.1.2/metrics_results/mean_climate/$mip/$exp/${version}/*/*${model}*.${version}.json ../test_case/mean_climate/
