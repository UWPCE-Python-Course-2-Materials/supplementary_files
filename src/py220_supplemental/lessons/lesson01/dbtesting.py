import os
import pytest
import sqlite3
import itertools


@pytest.fixture()
def db_in_memory():
    return 'file::memory:?cache=shared'


@pytest.fixture()
def keep_db():
    return True


@pytest.fixture()
def sql_statements():
    ddl = [
        "create table tt (id char)",
        "create table t2 (id char)",
    ]
    data = [
        [f'INSERT INTO tt VALUES ("{idnum}")' for idnum in range(10)],
        [f'INSERT INTO t2 VALUES ("{idnum}")' for idnum in range(100)],
    ]
    return ddl + list(itertools.chain(*data))


@pytest.fixture()
def session(db_in_memory, keep_db, sql_statements):
    filename = db_in_memory
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    connection = sqlite3.connect(filename)
    db_session = connection.cursor()
    [db_session.execute(sql) for sql in sql_statements]
    connection.commit()

    yield db_session

    connection.close()
    if filename != db_in_memory:
        if not keep_db:
            os.remove(filename)


def test_select_tt(session):
    session.execute("select id from tt")
    results = [int(item[0]) for item in session.fetchall()]
    assert results == list(range(10))


def test_select_t2(session):
    session.execute("select id from t2")
    results = [int(item[0]) for item in session.fetchall()]
    assert results == list(range(100))
