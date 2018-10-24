class Test(object):

    def __init__(self):
        print('__init__')

    def __call__(self):
        print('__call__')

t = Test()
t()
