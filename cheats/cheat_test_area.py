# import pytest
# import learn_testing.area.calc_areas as calc_areas
# import learn_testing.area.exception_zero as Ng

# # Rectangle test:
# @pytest.mark.parametrize(
#     "a,b,r",
#     [
#         (5,2,10),
#         (2,3,6),
#         (3,3,9),
#     ],
# )
# def test_rectangle_happy_path(a, b, r):
#     assert calc_areas.rectangle(a,b) == r


# @pytest.mark.parametrize(
#     "a,b,e",
#     [
#         (5,"2",TypeError),
#         (-1,5,Ng.NegativeError),
#     ],
# )
# def test_rectangle_sad_path(a ,b, e):
#     pytest.raises(e, calc_areas.rectangle, a,b)


# # Triangle test:

# @pytest.mark.parametrize(
#     "a,b,r",
#     [
#         (5,4,10),
#         (2,3,3),
#     ],
# )
# def test_triangle_happy_path(a, b, r):
#     assert calc_areas.triangle(a,b) == r


# @pytest.mark.parametrize(
#     "a,b,e",
#     [
#         (5,"2",TypeError),
#         ("3",2,TypeError),
#         (5,-1,Ng.NegativeError),
#         (-1,5,Ng.NegativeError),
#     ],
# )
# def test_triangle_sad_path(a ,b, e):
#     pytest.raises(e, calc_areas.triangle, a,b)

# # Hexagon test:

# @pytest.mark.parametrize(
#     "a,r",
#     [
#         (2,10.39),
#         (3,23.38)
        
#     ],
# )
# def test_hexagon_happy_path(a, r):
#     assert round(calc_areas.hexagon(a),2) == r


# @pytest.mark.parametrize(
#     "a,e",
#     [
#         ("2",TypeError),
#         (-1,Ng.NegativeError),  
#     ],
# )
# def test_hexagon_sad_path(a, e):
#     pytest.raises(e, calc_areas.circle, a)

# # Circle test:

# @pytest.mark.parametrize(
#     "a,r",
#     [
#         (3,28.27),
#         (2,12.57),
        
#     ],
# )
# def test_circle_happy_path(a, r):
#     assert round(calc_areas.circle(a),2) == r


# @pytest.mark.parametrize(
#     "a,e",
#     [
#         ("2",TypeError),
#         (-1,Ng.NegativeError),  
#     ],
# )
# def test_circle_sad_path(a , e):
#     pytest.raises(e, calc_areas.circle, a)