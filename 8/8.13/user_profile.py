# 用户简介


def build_profile(first_name, second_name, **feature):
    print('I am '+first_name.title()+second_name+';and my feature are bellow:')
    for k, v in feature.items():
        print(k+';'+v)


build_profile('sin', 'gi', age='26', work='programmer')
