import time

def test_exercise(app):
    app.open_home_page()
    app.enter_exercise("1")
    assert app.get_page_title() == "Exercise 1 - Two buttons"

    app.push_buttons_in_proper_order()
    time.sleep(3)
    assert app.get_solution_ex_1() == "OK. Good answer"
    time.sleep(3)