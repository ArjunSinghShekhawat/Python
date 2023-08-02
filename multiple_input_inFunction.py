def demo(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(demo(10,20,50,30))

def demo1(**kwargs):
    for k,w in kwargs.items():
        print(k)

demo1(name='arjun',email_id='a@gmail.com')