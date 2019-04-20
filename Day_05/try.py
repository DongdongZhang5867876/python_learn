menu = {
    '南京市':{
            "玄武区":{
                '四牌楼':{},
                '玄武湖':{},
                "鸡鸣寺":{},
                "鼓楼":{}
            },
            "江宁区":{
                "万达广场":{},
                "南京南站":{},
                "玛斯兰德":{}
            },
            "栖霞区":{
                "栖霞寺":{},
                "燕子饥":{},
                "幕府山":{}
            },
        },
    "苏州市":{
            "相城区":{
                "经济开发区":{},
                "阳澄湖":{},
                "渭塘镇":{}
            },
            "吴江区":{
                "同里镇":{},
                "静思园":{},
                "师俭堂":{}
            },
        },
    "扬州市":{
            "广陵区":{
                "东关街":{},
                "蜀冈":{}
            },
            "江都区":{
                "仙女公园":{},
                "扬州乐园":{}
            },
            "宝应县":{
                "宝应湖":{},
                "荷园":{},
            }
        }
}
path = []

while True:
    temp = menu
    for item in path:
        temp = temp[item]
    print('当前所有可选节点：', list(temp.keys()), '\n')

    choice = input("请输入你要查询的城市或地区(Q退出/B返回上一级)\n>>>")
    if choice == '1':
        k = input('请输入要增加的子节点的名称：')
        if k in temp:
            print('子节点已存在')
        else:
            temp[k] = {}
    elif choice == '2':
        k = input('请输入要查看的子节点：')
        if k in temp:
            path.append(k)
        else:
            print('子节点名称错误')
    elif choice.lower() == 'q':
        break
    elif choice.lower() == 'b':
        if path:
            path.pop()
    else:
        print('输入不合法，请重新输入\n>>>')