import re
import requests


# 定义常用关键词:
def often():
    often_dict = ['中国', '美国', '俄罗斯', '亚洲', '地球', '太阳系', '人工智能', '胡歌', '易烊千玺', '薛之谦', '毛不易', '知识图谱', '刘德华', '张学友', '明星']
    return often_dict


# api -> 读取搜索条件并返回搜索结果
def search(entity):  # entity 参数为传入搜索的关键词

    # 对一些常用的关键词进行搜索优化
    if entity == '薛之谦':
        return_data = {'薛之谦': ['实体'], '属性': ['中国内地男歌手', '音乐制作人', '演员'], '中文名': ['薛之谦'], '外文名': ['Joker'],
                       '别名': ['谦谦', '二谦'], '国籍': ['中国'], '民族': ['汉族'], '星座': ['巨蟹座'], '血型': ['O型'],
                       '身高': ['172cm'], '体重': ['55kg'], '出生地': ['上海'], '出生日期': ['1983年7月17日','农历6月8日'],
                       '职业': ['主持人'], '毕业院校': ['格里昂酒店管理学院'], '经纪公司': ['海蝶音乐'], '代表作品': ['认真的雪', '演员',
                                                                                        '丑八怪', '绅士', '意外', '你还要我怎样',
                                                                                        '刚刚好', '几个你', '我好像在哪见过你', '渡',
                                                                                        '初学者', '怪咖', '一半', '动物世界',
                                                                                        '方圆几里', '深深爱过你', '慢半拍', '天外来物'],
                       '主要成就': ['2016酷音乐亚洲盛典年度最受欢迎创作人'], '语言': ['吴语', '普通话', '英语'], '粉丝': ['谦友'],
                       '妻子': ['高磊鑫'], '搭档': ['君君'], '主要作品': ['水晶之恋','我们的少年时代'], '语种': ['吴语'], '儿子': ['小雪糕'],
                       '前女友': ['李雨桐']}
        return return_data

    url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity  # 知识图谱的API
    sess = requests.get(url)  # 发出get请求
    text = sess.text  # 获取返回的数据
    response = eval(text)  # 转为字典类型 ( 字典有键值对 ), 注: 这个response数据嵌套多个字典

    knowledge = response['data']  # response 这个字典里有 "data" 键
    # 属性值
    return_data = {}
    # 正则表达式 获取 knowledge['entity'] 数据的 [] 内容作为实体的属性值;
    comment = re.compile(r'\[(.*?)\]', re.S)  # S 表示字符串
    return_data[entity] = ["实体"]
    return_data["属性"] = comment.findall(knowledge['entity'])
    # response['data']  # response的 "data" 键所对应的值
    # response['data']['avp']  # response的 "data" 键所对应的值 里的 "avp" 键所对应的值

    for avp in knowledge['avp']:  # 相当于 用avp 遍历 response['data']['avp']
        # knowledge['avp'] : [['中文名', '明星'], ['外文名', 'Star;Celebrity;Lucida'], ['拼音', 'míngxīng'], ['注音', 'ㄇㄧㄥˊㄒㄧㄥ'],
        # 遍历的 avp 是每一个列表 如 ['中文名', '明星'] ; 此时的 avp[0]:'中文名', avp[1]:'明星'
        nums = len(return_data.keys())
        for i in list(return_data.keys()):  # i : 键
            if i == avp[0]:  # avp[0] : 键
                j_nums = len(return_data[i])
                for j in return_data[i]:  # j : 值
                    if j != avp[1] and j_nums == 1:  # 值j 和 值avp[1] 不相等
                        return_data[i].append(avp[1].split('、'))
                    j_nums -= 1
            elif nums == 1:
                return_data[avp[0]] = avp[1].split('、')
            nums -= 1
    print(return_data)
    return return_data
