import os
import _thread as thread
from source import search
import time
from py2neo import Graph, Node, Relationship
from PySide2 import QtGui


# api ->  将内容输出到操作页面
def outputWritten(self, text):
    cursor = self.textBrowser.textCursor()
    cursor.movePosition(QtGui.QTextCursor.End)
    cursor.insertText(text)
    self.textBrowser.setTextCursor(cursor)
    self.textBrowser.ensureCursorVisible()


# 启用多线程 -> CMD 命令行
def cmd(arg1, arg2):  # 多线程需要两个参数，即使不用
    # 在命令行输入指令 neo4j.bat console
    try:
        os.system("neo4j.bat console")
        # print("CMD 命令行调用成功 neo4j.bat console...")
        # print("cmd 线程创建成功！！！")
    except:
        print("cmd 线程创建失败！！！")
        print("neo4j 图形数据库服务 可能已经开启！！！")
        # print("具体错误原因如下:")


# 启动多线程 -> 连接图形数据库
def connect(self, search):  # search -> 搜索所返回的字典数据

    # 连接图形数据库
    outputWritten(self, "正在连接图形数据库......\n")
    # 连接图形数据库，输入个人配置
    graph = Graph("http://localhost:7474/browser/", username='neo4j', password='123456', run="sub")
    outputWritten(self, "连接图形数据库成功！！！！！\n")

    # 清空图形数据库里的全部数据
    graph.delete_all()
    # 开启一个新的事务
    graph.begin()

    # 对数据进行节点的设置
    # 将字典中的键转化为列表:
    searchkeys = list(search.keys())

    # 根据字典中的键的数量 来确定需要循环的次数:
    for i in range(1, len(search.keys())):
        # 根据搜索关键词 设置最主节点（起点）:
        title = searchkeys[0]  # title 为搜索的关键词
        # 建立节点的属性:
        node = Node(title, name=title)
        # 创建节点:
        graph.merge(node, title, 'name')

        # 设置子节点: ( 如上 )
        title1 = searchkeys[i]  # title1 为 i 对应索引的 键
        # 建立节点的属性:
        node1 = Node(title, name=title1)
        # 创建节点:
        graph.merge(node1, title, 'name')

        # 创建节点的指向:
        rel = Relationship(node, title1, node1, type="属性")  # node 起始节点; 指向节点 node1
        # 构建节点关系:
        graph.merge(rel)

        # 设置最小的子节点
        for j in search[title1]:  # 关系44行代码, j 为遍历 键title1 所对应的值
            node2 = Node(name=j)
            graph.merge(node2, title1, 'name')
            # 创建节点的指向:
            rel = Relationship(node1, title1, node2, type="属性")  # node1 起始节点; node2 指向节点
            # 构建节点关系:
            graph.merge(rel)

    # 输出到操作页面:
    # outputWritten(self, "================================")
    outputWritten(self, "图形数据库数据导入成功,知识图谱建立成功！！！\n")


def create(self, word):
    # 创建CMD命令行线程 (绘制知识图谱需要在命令行 开启neo4j服务,需持续运行):
    thread.start_new_thread(cmd, ("", ""))
    try:
        Search = search.search(word)  # 调用搜索的py文件里的搜索函数
        connect(self, Search)
        outputWritten(self, "请手动在浏览器中打开链接......  http://127.0.0.1:7474/browser/\n \n")
    except:
        return 0
