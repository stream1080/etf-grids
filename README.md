# etf-grids
ETF拯救世界的网格策略生成工具

1. [波段策略.网格之一：写在前面、体系以及策略](https://mp.weixin.qq.com/s/uxktt5ZpNo03FpQQX-aG7g)
2. [波段策略.网格之二：网格策略基础/1.0版](https://mp.weixin.qq.com/s/-czfqGvxkDcay_tSI1jv5g)
3. [波段策略.网格之三：网格策略进阶/2.0版](https://mp.weixin.qq.com/s/8pRKsjiQSZzrmH-uWCkRLQ)

## QuickStart

### Require
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Setup
```
# 网格参数
state = {
    'price': 1, # 初始价格
    'amount': 10000, # 每份金额
    'max_percent_of_decline': 0.6, # 最大跌幅
    'increase_percent_per_grid': 0.05, # 加码幅度
    'number_of_retained_profits': 2, # 留存利润份数
    'has_middle_grid': True, # 中网
    'has_large_grid': True # 大网
}
```

### Start
```
python3 grids.py
```

### Result
|   序号 | 种类   |   档位 |   买入价格 |   卖出价格 |   买入金额 |   买入数量 |   卖出金额 |   卖出数量 |   盈利金额 | 盈利比例   |   留存利润 |   留存金额 |
|-----:|:-----|-----:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|:-------|-------:|-------:|
|    1 | 小网   | 1    |   1    |   1.05 |  10000 |  10000 |   9450 |   9000 |    500 | 5.00%  |   1050 |   1000 |
|    2 | 小网   | 0.95 |   0.95 |   1    |  10450 |  11000 |   9900 |   9900 |    550 | 5.26%  |   1100 |   1100 |
|    3 | 小网   | 0.9  |   0.9  |   0.95 |  10980 |  12200 |  10355 |  10900 |    610 | 5.56%  |   1235 |   1300 |
|    4 | 小网   | 0.85 |   0.85 |   0.9  |  11475 |  13500 |  10800 |  12000 |    675 | 5.88%  |   1350 |   1500 |
|    5 | 中网   | 0.85 |   0.85 |   1    |  11475 |  13500 |   9400 |   9400 |   2025 | 17.65% |   4100 |   4100 |
|    6 | 小网   | 0.8  |   0.8  |   0.85 |  12000 |  15000 |  11220 |  13200 |    750 | 6.25%  |   1530 |   1800 |
|    7 | 小网   | 0.75 |   0.75 |   0.8  |  12450 |  16600 |  11600 |  14500 |    830 | 6.67%  |   1680 |   2100 |
|    8 | 小网   | 0.7  |   0.7  |   0.75 |  12950 |  18500 |  12000 |  16000 |    925 | 7.14%  |   1875 |   2500 |
|    9 | 中网   | 0.7  |   0.7  |   0.85 |  12950 |  18500 |  10115 |  11900 |   2775 | 21.43% |   5610 |   6600 |
|   10 | 大网   | 0.7  |   0.7  |   1    |  12950 |  18500 |   7400 |   7400 |   5550 | 42.86% |  11100 |  11100 |
|   11 | 小网   | 0.65 |   0.65 |   0.7  |  13455 |  20700 |  12390 |  17700 |   1035 | 7.69%  |   2100 |   3000 |
|   12 | 小网   | 0.6  |   0.6  |   0.65 |  13980 |  23300 |  12805 |  19700 |   1165 | 8.33%  |   2340 |   3600 |
|   13 | 小网   | 0.55 |   0.55 |   0.6  |  14465 |  26300 |  13140 |  21900 |   1315 | 9.09%  |   2640 |   4400 |
|   14 | 中网   | 0.55 |   0.55 |   0.7  |  14465 |  26300 |  10500 |  15000 |   3945 | 27.27% |   7910 |  11300 |
|   15 | 小网   | 0.5  |   0.5  |   0.55 |  15000 |  30000 |  13475 |  24500 |   1500 | 10.00% |   3025 |   5500 |
|   16 | 小网   | 0.45 |   0.45 |   0.5  |  15480 |  34400 |  13750 |  27500 |   1720 | 11.11% |   3450 |   6900 |
|   17 | 小网   | 0.4  |   0.4  |   0.45 |  16000 |  40000 |  13995 |  31100 |   2000 | 12.50% |   4005 |   8900 |
|   18 | 中网   | 0.4  |   0.4  |   0.55 |  16000 |  40000 |   9955 |  18100 |   6000 | 37.50% |  12045 |  21900 |
|   19 | 大网   | 0.4  |   0.4  |   0.7  |  16000 |  40000 |   3990 |   5700 |  12000 | 75.00% |  24010 |  34300 |
