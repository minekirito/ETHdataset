import re
import matplotlib.pyplot as plt

# 读取文档内容
with open(r'D:\PycharmProjections\nbeatsx-main\results\BJ\iGWO\fitness_params_blocks.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式提取mea_mean值
mape_means = re.findall(r'mape_mean=(\d+\.\d+)', content)

# 将提取的字符串转换成浮点数
mape_means = [float(mean) for mean in mape_means]

# 绘制mae_mean的变化曲线
plt.figure(figsize=(10, 5))
plt.plot(mape_means, marker='o', linestyle='-', color='b')
plt.title('Changes in mape_mean Over Time')
plt.xlabel('Time Step')
plt.ylabel('mape_mean Value')
plt.grid(True)
plt.show()