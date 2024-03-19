from pyecharts.charts import Map
from pyecharts import options as opts

province_data = [
    ("广东省", 1222.65), ("北京市", 1774.19), ("上海市", 1800), ("浙江省", 1303.63),
    ("江苏省", 1273.89), ("四川省", 1329.5), ("湖北省", 1000), ("福建省", 1220.55),
    ("河南省", 969.41), ("河北省", 1131.97), ("山东省", 1166.67), ("辽宁省", 984.82),
    ("安徽省", 1003.54), ("湖南省", 1453.68), ("陕西省", 1032.8), ("重庆市", 1212.5),
    ("黑龙江省", 1011.55), ("吉林省", 1680.7), ("云南省", 1343.57), ("贵州省", 1137.07),
    ("甘肃省", 707.68), ("青海省", 956.89), ("江西省", 1198.49), ("新疆维吾尔自治区", 1119.7),
    ("西藏自治区", 1184.55), ("内蒙古自治区", 1456.52), ("广西壮族自治区", 1048.78), ("宁夏回族自治区", 857.14),
    ("山西省", 1025.25), ("海南省", 2014.56)
]

map = Map()
map.add("2023年旅游人均消费", province_data, "china")
map.set_global_opts(
    title_opts=opts.TitleOpts(title="2023年中国各省份及自治区旅游人均消费地图"),
    visualmap_opts=opts.VisualMapOpts(
        max_=2100,
        min_=700,
        is_piecewise=True,  
        pieces=[
            {"min": 2000, "label": '2000元以上', "color": "#7f1818"},
            {"min": 1800, "max": 1999, "label": '1800-1999元', "color": "#9c2929"},
            {"min": 1600, "max": 1799, "label": '1600-1799元', "color": "#b33b3b"},
            {"min": 1400, "max": 1599, "label": '1400-1599元', "color": "#d14e4e"},
            {"min": 1200, "max": 1399, "label": '1200-1399元', "color": "#ef6161"},
            {"min": 1000, "max": 1199, "label": '1000-1199元', "color": "#ff7575"},
            {"min": 800, "max": 999, "label": '800-999元', "color": "#ff8888"},
            {"min": 700, "max": 799, "label": '700-799元', "color": "#ffaaaa"},
        ],
    )
)
map.render("china_tourism_per_capita_spending_2023_more_intervals.html")
