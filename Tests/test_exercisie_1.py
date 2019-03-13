def test_exercise(app):
    app.open_home_page()
    app.enter_exercise(1)
    assert app.get_page_title() == "Exercise 1 - Two buttons"