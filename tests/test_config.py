from cp_3.config import ROOT_PATH, PATH_CP_3, PATH_OPERATIONS, count_operations


def test_root_path():
    assert ROOT_PATH.exists() is True


def test_path_cp_3():
    assert PATH_CP_3.exists() is True


def test_path_operations():
    assert PATH_OPERATIONS.exists() is True


def test_count_operations():
    assert count_operations == 5
