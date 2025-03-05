import numpy as np

def simulate_down_and_out_call(S0, K, r, sigma, T, b, m, n_paths, seed=None):
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / m
    # 模拟标准正态随机数
    Z = np.random.randn(n_paths, m)
    # 初始化股票价格路径矩阵
    S = np.zeros((n_paths, m+1))
    S[:, 0] = S0

    # 生成股票价格路径
    for i in range(1, m+1):
        S[:, i] = S[:, i-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, i-1])
    
    # 检查路径中是否始终未跌破障碍 b
    not_knocked_out = np.all(S[:, 1:] >= b, axis=1)
    
    # 到期时股票价格
    ST = S[:, -1]
    # 计算看涨期权支付 (仅对未敲出路径有效)
    payoff = np.where(not_knocked_out, np.maximum(ST - K, 0), 0)
    
    # 计算贴现后的期权价格
    discounted_payoff = np.exp(-r * T) * payoff
    price_estimate = np.mean(discounted_payoff)
    std_error = np.std(discounted_payoff) / np.sqrt(n_paths)
    
    return price_estimate, std_error

# 参数设置
S0 = 50
K = 50
r = 0.10
sigma = 0.2
T = 1
b = 45
m = 12  # 监控日期数量
n_paths_list = [10000, 40000]

# 模拟并输出结果
for n_paths in n_paths_list:
    price, se = simulate_down_and_out_call(S0, K, r, sigma, T, b, m, n_paths, seed=42)
    print(f"路径数: {n_paths:5d} 期权价格估计: {price:.4f} 标准误差: {se:.4f}")
