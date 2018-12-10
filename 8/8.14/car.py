# 汽车


def build_car(build_name, version, **more_info):
    print('制造商是:'+build_name)
    print('型号:'+version)
    print('更多信息:')
    for k, v in more_info.items():
        print(k+';'+v)


build_car('上海大众', 'xs1', 颜色='black', speed='fast')
