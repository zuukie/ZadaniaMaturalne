# # f = open("prostokaty.txt", "r")
# # f2 = open("prostokaty_przyklad.txt", "r")
# #
# # biggest = None
# # smallest = None
# #
# # for line in f:
# #     line = line.strip().split()
# #     height = int(line[0])
# #     width = int(line[1])
# #     pole = height * width
# #     if biggest is None and smallest is None:
# #         biggest, smallest = pole, pole
# #     else:
# #         if pole < smallest:
# #             smallest = pole
# #         elif pole > biggest:
# #             biggest = pole
# #
# #
# # f.close()
# # f2.close()
# #
# # print(biggest)
# # print(smallest)
#
# # f = open("prostokaty.txt", "r")
# # f2 = open("prostokaty_przyklad.txt", "r")
# #
# # szerokoscPrim = None
# # wysokoscPrim = None
# # najdluszyCiag = 0
# # najlepszySzerokosc = None
# # najlepszyWysokosc = None
# #
# # for line in f:
# #     line = line.strip().split()
# #     height = int(line[0])
# #     width = int(line[1])
# #     if szerokoscPrim is None and wysokoscPrim is None:
# #         ciag = 1
# #         szerokoscPrim = width
# #         wysokoscPrim = height
# #         continue
# #
# #     if width <= szerokoscPrim and height <= wysokoscPrim:
# #         ciag += 1
# #         szerokoscPrim = width
# #         wysokoscPrim = height
# #         continue
# #
# #     if ciag > najdluszyCiag:
# #         najlepszySzerokosc = szerokoscPrim
# #         najlepszyWysokosc = wysokoscPrim
# #         najdluszyCiag = ciag
# #
# #     ciag = 1
# #     szerokoscPrim = width
# #     wysokoscPrim = height
# #
# # f.close()
# # f2.close()
# #
# # print(najdluszyCiag)
# # print(najlepszyWysokosc)
# # print(najlepszySzerokosc)
#
#
# f = open("prostokaty.txt", "r")
# f2 = open("prostokaty_przyklad.txt", "r")
#
# everything = {}
#
# for line in f:
#     line = line.strip().split()
#     height = int(line[0])
#     width = int(line[1])
#     if height in everything:
#         everything[height].append(width)
#     else:
#         everything[height] = [width]
#     everything[height].sort()
# print(everything)
#
# najszerszy = 0
#
# for key in everything:
#     if len(everything[key]) < 5:
#         continue
#     szerokosc = everything[key][-1] + everything[key][-2] + everything[key][-3] + everything[key][-4] + everything[key][-5]
#     if szerokosc > najszerszy:
#         najszerszy = szerokosc
#
# print(najszerszy)
#
# f.close()
# f2.close()

