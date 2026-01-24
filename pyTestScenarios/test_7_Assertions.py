

def test_assert():
    input1 = "Gilberto"
    output1 = "gil"

    assert input1 == output1, "both strings not matched"
    assert output1 in input1
    assert False, "default failed"

# def test_assert():
#     input1 = "Gilberto"
#     output1 = "gil"
#     if input1 == output1:
#         print("both are equals")
#     else:
#         print("both not equals")
