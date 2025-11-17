import pickle
import pandas as pd
import hyperopt
# 提供文件的完整路径
file_path = r"D:\PycharmProjections\nbeatsx-main\results\BE\nbeats_x\hyperopt_nbeatsx_0_0.p"

# 打开文件以读取二进制数据
with open(file_path, 'rb') as f:
    # 使用pickle的load函数将二进制数据反序列化为Python对象
    trials_data = pickle.load(f)

'''best_trial = trials_data.best_trial
best_loss = best_trial['result']['loss']'''
#print(trials_data)
#df_trials = pd.DataFrame(trials_data.results)
'''df_trials = pd.DataFrame(list(trials_data.values()))
print(df_trials.head())'''
# 根据你的需求进一步处理best_params
#print(trials_data)

# 将 Trials 对象转换为 DataFrame
'''df_trials = pd.DataFrame([(t['tid'], t['result']['loss'], *(t['misc']['vals'].values()))
                          for t in trials_data.trials if t['state'] == hyperopt.STATUS_OK])'''
print(trials_data)