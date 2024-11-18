# etf-grids
ETF拯救世界的网格策略生成工具

## QuickStart

### require
```
pip install -r requirements.txt
```

### setup
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

### start
```
python3 grids.py
```

## Reference
1. [波段策略.网格之一：写在前面、体系以及策略](https://mp.weixin.qq.com/s/uxktt5ZpNo03FpQQX-aG7g)
2. [波段策略.网格之二：网格策略基础/1.0版](https://mp.weixin.qq.com/s/-czfqGvxkDcay_tSI1jv5g)
3. [波段策略.网格之三：网格策略进阶/2.0版](https://mp.weixin.qq.com/s/8pRKsjiQSZzrmH-uWCkRLQ)