from pyecharts.charts import Bar
from pyecharts import options as opts

brands = ["一汽大众", "上汽大众", "上汽通用", "长安汽车", "吉利汽车", "东风日产", "长城汽车", "上汽通用五菱", "东风本田", "广汽丰田", "北京奔驰", "一汽丰田", "华晨宝马", "广汽本田", "奇瑞汽车"]
sales = [232387, 165500, 150014, 147973, 146295, 124077, 109351, 103872, 90136, 87372, 80670, 75710, 73961, 67321, 65155]

bar = Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
bar.add_xaxis(brands)
bar.add_yaxis("销售量", sales)
bar.set_global_opts(title_opts=opts.TitleOpts(title="2021年1月各汽车品牌销售量"), 
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
                    yaxis_opts=opts.AxisOpts(name="销售量"),
                    datazoom_opts=[opts.DataZoomOpts()])

bar.render("car_sales_january_2021.html")
