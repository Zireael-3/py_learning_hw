"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """
    The instances_counter decorator takes a cls class and returns a new NewClass class that inherits from cls.
    Two methods are added to NewClass: get_created_instances and reset_instances_counter.
    Also, the created_instances attribute is added to NewClass, which stores the number of class instances created.
    """
    class NewClass(cls):
        created_instances = 0

        def __new__(cls, *args, **kwargs):
            """
            The __new__ method is overridden to
            increment the created_instances counter
            when a new class instance is created.
            """
            instance = super().__new__(cls)
            cls.created_instances += 1
            return instance

        @classmethod
        def get_created_instances(cls):
            return cls.created_instances

        @classmethod
        def reset_instances_counter(cls):
            count = cls.created_instances
            cls.created_instances = 0
            return count

    return NewClass


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
    User.get_created_instances()  # 0
