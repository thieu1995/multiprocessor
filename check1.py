#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu" at 22:17, 30/10/2021                                                               %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Nguyen_Thieu2                                  %
#       Github:     https://github.com/thieu1995                                                        %
# ------------------------------------------------------------------------------------------------------%


# def fuckyou(t1, t2=None, *args, **kwargs):
#     print(t1)
#     print(t2)
#
#     print(args)
#
#     if "fucker" in kwargs:
#         print(kwargs["fucker"])
#     else:
#         print("stfu")
#
# fuckyou("Quan", "Mat Loz", (1.2, 5.0), {"fucker": "Lam"})



# def testlam(*args):
#     total = 0
#     for x in args:
#         total += x
#     print(total)
#
# # testlam([1, ])
# # testlam([1, 2, ])
# testlam(1, 2, 3)



# def testlam(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# # testlam(x=2, y=5, lam="anloz")
# testlam(t={"x": 1, "y": 2})



class Test1:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return self.x

print(Test1("thieu"))





