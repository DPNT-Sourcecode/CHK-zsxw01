

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    return "Hello, %(friend_name)s!" % dict(friend_name=friend_name)
