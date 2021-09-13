from celery import Celery

app = Celery('Calculator', broker='amqp://guest:guest@localhost:5672')

app.conf.task_default_exchange = 'Calculator'
app.conf.task_default_routing_key = 'Calculator'
app.conf.task_default_queue = 'Calculator'


@app.task()
def Calculator(a, op, b):

    choice = op

    if choice == '+':
        return a + b

    elif choice == '-':
        return a - b

    elif choice == '*':
        return a * b

    elif choice == '/':
        return a / b

    else:
        print("Invalid Input")