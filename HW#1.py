import random
import pytest

names=['Renat', 'Marat', 'Bulat' , 'Timur', 'Denis', 'Artur' ]

class Queue:

    def __init__(self, typi):
        self.queue = []
        self.typi = typi

#добавляем в очередь
    def enqueue(self, human):
        self.queue.append(human)

#удаляем из очереди
    def dequeue(self, human):
        if len(self.queue) < 1:
            return None
        return self.queue.remove(human)

#вывод queue
    def output(self):
        return self.queue

    def show_size(self):
        return len(self.queue)

    def rear(self):
        return self.queue[-1]

    def front(self):
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def fit_in(self):
        if len(names) < 1:
            return None
        return self.queue.insert(random.randint(0, len(self.queue)), random.choice(names))

    def __str__(self):
        return f'Очередь за {self.typi}'

class Human:
    @staticmethod
    def stop():
        return f'Куда без очереди '

    def __repr__(self):
        return f'{self.name}'

    def __init__(self, name, age=random.randint(1,90)):
        self.name = name
        self.age = age

    def say_bye(self):
        print(f'Bye bye from {self.name} ')

    def say(self):
        print( f"Привет. Мое имя {self.name}. Мне {self.age} лет.")

q=Queue('Auto')
hum = Human("Almaz")
hum2=Human('Andrei', 11)
hum3=Human('Kirill')

qu=Queue('Moloko')
qu.enqueue(hum)
qu.enqueue(hum3)
qu.enqueue(hum2)
print(qu.output())
print(qu.typi)