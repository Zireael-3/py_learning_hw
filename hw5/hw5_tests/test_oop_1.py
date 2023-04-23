import datetime

from hw5.hw5_tasks.oop_1 import Homework, Teacher, Student


def test_oop():
    teacher = Teacher('Arina', 'Pafnuteva')
    student = Student('Vladislav', 'Gnatenko')
    assert teacher.first_name == 'Arina'
    assert teacher.last_name == 'Pafnuteva'
    assert student.first_name == 'Vladislav'
    assert student.last_name == 'Gnatenko'

    expired_homework = teacher.create_homework('Learn functions', 0)
    assert isinstance(expired_homework.created, datetime.datetime)
    assert isinstance(expired_homework.deadline, datetime.timedelta)
    assert expired_homework.text == 'Learn functions'

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    assert isinstance(oop_homework.deadline, datetime.timedelta)
    assert student.do_homework(oop_homework) == 'In process'
    assert student.do_homework(expired_homework) == 'In process'
