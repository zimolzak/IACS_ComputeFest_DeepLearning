import pickle
x = open('/Users/ajz/Desktop/mnist/mnist.pkl', 'r')
up = pickle.Unpickler(x)
A = up.load()
