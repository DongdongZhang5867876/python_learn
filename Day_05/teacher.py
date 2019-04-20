#!/usr/bin/evn python
# -*-coding:utf8 -*-
class menu(object):
    def __init__(self, menus):
        self.menus = menus
    def view_dict(self,menu):
        print('请输入进入地区，输入"b"返回上层菜单，输入"q"退出'.center(40, '-'))
        print('\n'.join([str(key) for key in menu]))
        choice = input("请选择>>:")
        if choice == 'q':
            exit()
        elif choice == 'b':
            if menu != self.menus:
                return
            else:
                print('已经是最顶层目录，请选择或退出，谢谢'.center(40,' '))
                self.view_dict(menu)
        elif choice in [key for key in menu]:
            if type(menu[choice]).__name__=='dict':
                 self.view_dict(menu[choice])
                 self.view_dict(menu)
            else:
                print('\n'.join([item for item in menu[choice]]))
                print('已经是最后一层，返回请输入"b",退出请输入"q",谢谢!'.center(40,'*'))
                self.view_dict(menu)
        else:
            print('请输入正确口令，谢谢！')
            self.view_dict(menu)
if __name__=='__main__':

    zone = {
     '山东': {
         '青岛': ['四方', '黄岛', '崂山', '李沧', '城阳'],
         '济南': ['历城', '槐荫', '高新', '长青', '章丘'],
         '烟台': ['龙口', '莱山', '牟平', '蓬莱', '招远']
     },
     '江苏': {
         '苏州': ['沧浪', '相城', '平江', '吴中', '昆山'],
         '南京': ['白下', '秦淮', '浦口', '栖霞', '江宁'],
         '无锡': ['崇安', '南长', '北塘', '锡山', '江阴']
     },
     '浙江': {
         '杭州': ['西湖', '江干', '下城', '上城', '滨江'],
         '宁波': ['海曙', '江东', '江北', '镇海', '余姚'],
         '温州': ['鹿城', '龙湾', '乐清', '瑞安', '永嘉']
     },
     '安徽': {
         '合肥': ['蜀山', '庐阳', '包河', '经开', '新站'],
         '芜湖': ['镜湖', '鸠江', '无为', '三山', '南陵'],
         '蚌埠': ['蚌山', '龙子湖', '淮上', '怀远', '固镇']
     },
     '广东': {
         '深圳': ['罗湖', '福田', '南山', '宝安', '布吉'],
         '广州': ['天河', '珠海', '越秀', '白云', '黄埔'],
         '东莞': ['莞城', '长安', '虎门', '万江', '大朗']
     }}

    view = menu(zone)
    view.view_dict(zone)