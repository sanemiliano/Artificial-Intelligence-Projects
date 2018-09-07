import tensorflow as tf

g = tf.Graph()

with g.as_default():
    x = tf.constant(7,name="x_const")
    y = tf.constant(5,name="y_const")
    z = tf.constant(3,name="z_constant")
    my_sum = tf.add(x,y,name="x_y_sum")
    my_sum = tf.add(my_sum,z,name="x_y_z_sum")

    with tf.Session() as sess:
     print(my_sum.eval(session=sess))