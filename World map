from pyecharts.charts import Map
from pyecharts import options as opts

data = [
    ("Finland", 7.537), ("Denmark", 7.522), ("Iceland", 7.504), ("Switzerland", 7.494),
    ("Norway", 7.469), ("Netherlands", 7.377), ("Canada", 7.316), ("New Zealand", 7.314),
    ("Australia", 7.284), ("Sweden", 7.284), ("Israel", 7.213), ("Costa Rica", 7.079),
    ("Austria", 7.006), ("United States", 6.993), ("Ireland", 6.977), ("Germany", 6.951),
    ("Belgium", 6.891), ("Luxembourg", 6.863), ("United Kingdom", 6.714), ("Chile", 6.652),
    ("United Arab Emirates", 6.648), ("Brazil", 6.635), ("Czech Republic", 6.609),
    ("Argentina", 6.599), ("Mexico", 6.578), ("Singapore", 6.572), ("Malta", 6.527),
    ("Uruguay", 6.454), ("Guatemala", 6.454), ("Panama", 6.452), ("France", 6.442),
    ("Thailand", 6.424), ("Taiwan", 6.422), ("Spain", 6.403), ("Qatar", 6.375),
    ("Colombia", 6.357), ("Saudi Arabia", 6.344), ("Trinidad and Tobago", 6.168),
    ("Kuwait", 6.105), ("Slovakia", 6.098), ("Bahrain", 6.087), ("Malaysia", 6.084),
    ("Nicaragua", 6.071), ("Ecuador", 6.008), ("El Salvador", 6.003), ("Poland", 5.973),
    ("Uzbekistan", 5.971), ("Italy", 5.964), ("Russia", 5.963), ("Belize", 5.956),
    ("Japan", 5.92), ("Lithuania", 5.902), ("Algeria", 5.872), ("Latvia", 5.85),
    ("Moldova", 5.838), ("South Korea", 5.838), ("Romania", 5.825), ("Bolivia", 5.823),
    ("Turkmenistan", 5.822), ("Kazakhstan", 5.819), ("North Cyprus", 5.81), ("Slovenia", 5.758),
    ("Peru", 5.715), ("Mauritius", 5.629), ("Cyprus", 5.621), ("Estonia", 5.611),
    ("Belarus", 5.569), ("Libya", 5.525), ("Turkey", 5.5), ("Paraguay", 5.493),
    ("Hong Kong", 5.472), ("Philippines", 5.43), ("Serbia", 5.395), ("Jordan", 5.336),
    ("Hungary", 5.324), ("Jamaica", 5.311), ("Croatia", 5.293), ("Kosovo", 5.279),
    ("China", 5.273), ("Pakistan", 5.269), ("Indonesia", 5.262), ("Venezuela", 5.25),
    ("Montenegro", 5.237), ("Morocco", 5.235), ("Azerbaijan", 5.234), ("Dominican Republic", 5.23),
    ("Greece", 5.227), ("Lebanon", 5.225), ("Portugal", 5.195), ("Bosnia and Herzegovina", 5.182),
    ("Honduras", 5.181), ("Macedonia", 5.175), ("Somalia", 5.151), ("Vietnam", 5.074),
    ("Nigeria", 5.074), ("Tajikistan", 5.041), ("Bhutan", 5.011), ("Kyrgyzstan", 5.004),
    ("Nepal", 4.962), ("Mongolia", 4.955), ("South Africa", 4.829), ("Tunisia", 4.805),
    ("Palestine", 4.775), ("Egypt", 4.735), ("Bulgaria", 4.714), ("Sierra Leone", 4.709),
    ("Cameroon", 4.695), ("Iran", 4.692), ("Albania", 4.644), ("Bangladesh", 4.608),
    ("Namibia", 4.574), ("Kenya", 4.553), ("Mozambique", 4.55), ("Myanmar", 4.545),
    ("Senegal", 4.535), ("Zambia", 4.514), ("Iraq", 4.497), ("Gabon", 4.465),
    ("Ethiopia", 4.46), ("Sri Lanka", 4.44), ("Armenia", 4.376), ("India", 4.315),
    ("Mauritania", 4.292), ("Congo (Brazzaville)", 4.291), ("Georgia", 4.286),
    ("Congo (Kinshasa)", 4.28), ("Mali", 4.19), ("Ivory Coast", 4.18), ("Cambodia", 4.168),
    ("Sudan", 4.139), ("Ghana", 4.12), ("Ukraine", 4.096), ("Uganda", 4.081),
    ("Burkina Faso", 4.032), ("Niger", 4.028), ("Malawi", 3.97), ("Chad", 3.936),
    ("Zimbabwe", 3.875), ("Lesotho", 3.808), ("Angola", 3.795), ("Afghanistan", 3.794),
    ("Botswana", 3.766), ("Benin", 3.657), ("Madagascar", 3.644), ("Haiti", 3.603),
    ("Yemen", 3.593), ("South Sudan", 3.591), ("Liberia", 3.533), ("Guinea", 3.507),
    ("Togo", 3.495), ("Rwanda", 3.471), ("Syria", 3.462), ("Tanzania", 3.349),
    ("Burundi", 2.905)
]
map = Map()
map.add("幸福指数", data, "world")
map.set_global_opts(
    title_opts=opts.TitleOpts(title="世界各国人民幸福指数"),
    visualmap_opts=opts.VisualMapOpts(max_=8, min_=2, is_piecewise=True,
                                      pieces=[
                                          {"min": 7, "color": "#006837"},
                                          {"min": 6, "max": 7, "color": "#1a9850"},
                                          {"min": 5, "max": 6, "color": "#66bd63"},
                                          {"min": 4, "max": 5, "color": "#fdae61"},
                                          {"min": 2, "max": 4, "color": "#d73027"},
                                      ]),
)
map.render("world_happiness_index_map.html")
