import os

# 参考连接
# http://www.cnblogs.com/OldPanda/archive/2013/04/12/3017100.html

# 每次计算取实例点的顺序对于计算结果是有影响的

# 三个实例点 (3, 3)、(4, 3)为正，(1, 1)是负实例
train_set = [[(3, 3), 1], [(4, 3), 1], [(1, 1), -1]]

# w, b 初始值为0（默认）
w = [0, 0]
b = 0
# 学习率为1（默认）
learning_rate = 1


def cal(item):
    global w, b
    # 对于正实例 y(w*x + b) >= 0
    # 对于负实例 y(w*x + b) < 0
    return item[1] * (w[0] * item[0][0] + w[1] * item[0][1] + b)


def update(item):
    global w, b
    # w_(i + 1) <- w_i + learning_rate * x_i * y_i
    for index in range(len(item[0])):
        w[index] = w[index] + item[1] * item[0][index] * learning_rate
    # b <- b + learning_rate * y
    b = b + item[1] * learning_rate
    print('点：', str(item))
    print('w:', str(w), ' ,b:', b)


def preceptron(train_set):
    flag = False
    for item in train_set:
        if cal(item) <= 0:
            flag = True
            update(item)
    # 不存在误分类点之后输出结果
    if not flag:
        print("RESULT: w: ", str(w), " b: ", str(b))
        os._exit(0)


if __name__ == '__main__':
    for i in range(100):
        print('第', i + 1, "次计算")
        preceptron(train_set)
    print("The training_set is not linear separable. ")
