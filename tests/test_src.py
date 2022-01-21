from dot4dict import dotdict


def test_create_single_depth():
    test_dict = dotdict({"a": 5})
    assert test_dict["a"] == 5
    assert test_dict.a == 5


def test_create_double_depth():
    test_dict = dotdict({"a": {"b": 5}})
    assert test_dict["a"]["b"] == 5
    assert test_dict.a["b"] == 5
    assert test_dict.a.b == 5


def test_update_single_depth():
    test_dict = dotdict({"a": 5})
    test_dict["b"] = 25
    assert test_dict["a"] == 5
    assert test_dict["b"] == 25

    assert test_dict.a == 5
    assert test_dict.b == 25


def test_update_double_depth():
    test_dict = dotdict({"a": 5, "b": 10})
    test_dict["b"] = {"c": 125}

    assert test_dict["b"]["c"] == 125
    assert test_dict["b"].c == 125
    assert test_dict.b["c"] == 125
    assert test_dict.b.c == 125
