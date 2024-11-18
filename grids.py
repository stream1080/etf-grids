from enum import Enum
from math import floor
import pandas as pd

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

# 网格类型
class GearType(Enum):
    small = '小网'
    middle = '中网'
    large = '大网'


# 网格幅度
class GearPercent(Enum):
    small = 0.05
    middle = 0.15
    large = 0.3


# 用于存储网格数据的类
class Grid:
    def __init__(self, type, gear, buy_price, sell_price, buy_amount, buy_count, sell_amount, sell_count, profits, return_rate, retained_profits, retained_count):
        self.type = type
        self.gear = gear
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.buy_amount = buy_amount
        self.buy_count = buy_count
        self.sell_amount = sell_amount
        self.sell_count = sell_count
        self.profits = profits
        self.return_rate = return_rate
        self.retained_profits = retained_profits
        self.retained_count = retained_count


# 保留3位小数的函数
def to_fixed_string(value, digits=3):
    return f"{value:.{digits}f}"


# 精确到3位小数的浮动值
def to_fixed_number(value, digits=3):
    return float(to_fixed_string(value, digits))


# 数字精度问题
def divide(v1, v2):
    return float(f"{v1 / v2:.14g}")


# GearPercent 小网和中网、大网的比例计算
T_MIDDLE = divide(GearPercent.middle.value, GearPercent.small.value)
T_LARGE = divide(GearPercent.large.value, GearPercent.small.value)


# 创建网格的函数
def create_grid(options):
    number_of_retained_profits = options['number_of_retained_profits']
    type = options['type']
    gear = options['gear']
    price = options['price']
    percent = options['percent']
    buy_amount = options['buy_amount']

    buy_price = gear * price
    # 买入必须按照100份整数
    buy_count = floor(buy_amount / buy_price / 100) * 100
    buy_amount = buy_count * buy_price
    sell_price = (gear + percent) * price
    current_amount = buy_count * sell_price
    profits = current_amount - buy_amount
    return_rate = f"{to_fixed_string((profits / buy_amount) * 100, 2)}%"
    
    retained_profits = profits * number_of_retained_profits
    # 卖出必须按照100份整数
    sell_count = floor((current_amount - retained_profits) / sell_price / 100) * 100
    sell_amount = sell_count * sell_price
    retained_profits = current_amount - sell_amount
    retained_count = retained_profits / sell_price

    return Grid(type, gear, buy_price, sell_price, buy_amount, buy_count, sell_amount, sell_count, profits, return_rate, retained_profits, retained_count)


# 使用网格策略生成多个网格
def use_grids(state):
    price = state['price']
    amount = state['amount']
    max_percent_of_decline = state['max_percent_of_decline']
    increase_percent_per_grid = state['increase_percent_per_grid']
    number_of_retained_profits = state['number_of_retained_profits']
    has_middle_grid = state['has_middle_grid']
    has_large_grid = state['has_large_grid']

    grids = []

    # 最大档位和最小档位计算
    max_gear = 1
    min_gear = (1 - max_percent_of_decline) * max_gear

    gear = max_gear
    i = 0
    j = 0
    k = 0

    while gear >= min_gear:
        buy_amount = to_fixed_number((increase_percent_per_grid * i + 1) * amount, 0)
        # 小网幅度5%
        grids.append(create_grid({
            'type': GearType.small.value,
            'buy_amount': buy_amount,
            'gear': gear,
            'percent': GearPercent.small.value,
            'number_of_retained_profits': number_of_retained_profits,
            'price': price
        }))

        # 中网幅度15%
        if has_middle_grid and i and i % T_MIDDLE == 0:
            j += 1
            grids.append(create_grid({
                'type': GearType.middle.value,
                'buy_amount': buy_amount,
                'gear': to_fixed_number(1 - j * GearPercent.middle.value),
                'percent': GearPercent.middle.value,
                'number_of_retained_profits': number_of_retained_profits,
                'price': price
            }))

        # 大网幅度30%
        if has_large_grid and i and i % T_LARGE == 0:
            k += 1
            grids.append(create_grid({
                'type': GearType.large.value,
                'buy_amount': buy_amount,
                'gear': to_fixed_number(1 - k * GearPercent.large.value),
                'percent': GearPercent.large.value,
                'number_of_retained_profits': number_of_retained_profits,
                'price': price
            }))

        i += 1
        gear = to_fixed_number(1 - i * GearPercent.small.value)

    return grids


def to_csv(tables):
    df = pd.DataFrame(tables)
    df.rename(columns={
                    'index': '序号',
                    'type': '种类', 
                    'gear': '档位', 
                    'buy_price': '买入价格',
                    'buy_amount': '买入金额',
                    'buy_count': '买入数量',
                    'sell_price': '卖出价格',
                    'sell_amount': '卖出金额',
                    'sell_count': '卖出数量',
                    'profits': '盈利金额',
                    'return_rate': '盈利比例',
                    'retained_profits': '留存利润',
                    'retained_count': '留存金额',
                    }, inplace=True)

    df.to_csv('output.csv', index=False, encoding='utf-8')


def main():
    grids = use_grids(state)
    tables = []
    for idx, obj in enumerate(grids,start=1):
        obj_dict = vars(obj)
        tables.append({'index': idx, **obj_dict})

    to_csv(tables)


if __name__ == '__main__':
    main()