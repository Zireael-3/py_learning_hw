from hw5.hw5_tasks.counter import instances_counter


def test_counter():
    @instances_counter
    class User:
        pass

    if __name__ == '__main__':
        assert User.get_created_instances() == 0
        user, _, _ = User(), User(), User()
        assert user.get_created_instances() == 3
        assert user.reset_instances_counter() == 3
        assert User.get_created_instances() == 0
        assert user.get_created_instances() != 9
