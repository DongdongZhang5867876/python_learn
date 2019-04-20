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
    for i in temp:
        print(i,'\n')

    choice = input("请输入你要查询的城市或地区(Q退出/B返回上一级)\n>>>")
    if choice in temp:
        path.append(choice)
    elif choice.lower() == 'b':
        if path:
            path.pop()
    elif choice.lower() == 'q':
        break
    else:
        choice = input("输入有误，请再输一遍：\n")