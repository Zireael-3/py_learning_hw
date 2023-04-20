from hw4.hw4_tasks.task03 import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger('error: something went wrong')
    err = capsys.readouterr()
    assert 'error: something went wrong' in err.err

    my_precious_logger('info: everything is fine')
    out = capsys.readouterr()
    assert 'info: everything is fine' in out.out
