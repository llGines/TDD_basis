# import learn_testing.mymates.exception_list as El

# mates = [
#     "Joey",
#     "Jhonny",
#     "Dee Dee",
#     "Tommy",
#     "Richie",
#     "C.J.",
#     "Marky",
#     "Joe",
#     "Paul",
#     "Mick",
#     "Nicky",
# ]


# def count_vocals(a):
#     b = a.lower()
#     if b not in "aeiou":
#         raise El.NotInListError
#     else:
#         return len([i for x in mates for i in x.lower() if i == b])


# def return_names(a):
#     b = [s for s in mates if a in s.lower()]
#     if len(b) == 0:
#         raise El.NotInListError
#     else:
#         return b
