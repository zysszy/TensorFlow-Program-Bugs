import tensorflow as tf

#  tf.version == 1.0.0
v_1 = tf.Variable(1)
v_2 = tf.Variable(v_1)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(v_2))