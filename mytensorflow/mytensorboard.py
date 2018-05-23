#/usr/bin/env python
#coding:utf-8
import tensorflow as tf
import tensorboard
import numpy as np

#神经层
def add_layer(inputs,in_size,out_size,activation_function=None):
    with tf.name_scope('layer'):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs
#创建数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(1,0.05,x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32,[None,1],'x_inputs')
    ys = tf.placeholder(tf.float32,[None,1],'y_inputs')

#layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.softplus)
predition = add_layer(l1, 10, 1, activation_function=None)

#预测
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition),
                                        reduction_indices=[1]))

#train
with tf.name_scope('train_step'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#初始所有变量

sess = tf.Session()
writer = tf.summary.FileWriter("logs/",sess.graph)

sess.run(tf.initialize_all_variables())
