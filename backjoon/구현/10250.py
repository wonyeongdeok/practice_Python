# T = int(input())
#
# for _ in range(T):
#     H, W, N = map(int, input().split())
#     rooms = []
#     for h in range(H, 0, -1):
#         h = str(h)
#         tmp_rooms = []
#         for w in range(1, W+1):
#             if len(str(w)) == 1:
#                 w = '0' + str(w)
#             else:
#                 w = str(w)
#             room = h + w
#             tmp_rooms.append(room)
#         rooms.append(tmp_rooms)
#
#     n = 0
#     for w in range(W):
#         for h in range(H-1, -1, -1):
#             res = rooms[h][w]
#             n += 1
#             if n == N:
#                 print(res)
