# 使用生成器实现单线程并发效果
import time
students = ['stu:%s'%x for x in range(10)]

# 消费者
def consumer(name):
    print("%s 准备学习"%name)
    while True:
        lesson = yield
        print("开始【%s】了，【%s】老师来讲课了！"%(lesson,name))
# 生产者
def producer():
    c = consumer('A')
    c1 = consumer('B')

    next(c)
    next(c1)

    for i in students:
        time.sleep(2)
        c.send(i)
        c1.send(i)

if __name__ == '__main__':
    producer()