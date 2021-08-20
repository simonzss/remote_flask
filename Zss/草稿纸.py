# import copy
#
# # t_C 是orm里的类名, query_type 字符串，判断查询, cityinfo 字典，其key为表格主栏, specinfo 字典，其key为表格宾栏
# cityinfo_SP = {
#     "工业": ["1"],
#     "建筑业": ["2"],
#     "批发业": ["3"],
#     "零售业": ["4"],
#     "住宿业": ["5"],
#     "餐饮业": ["6"],
#     "房地产": ["7"],
#     "服务业": ["8"],
#     "投资": ["9"],
#     "总计": ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
#     "五上": ["1", "2", "3", "4", "5", "6", "7", "8"],
#     "农林牧渔业": ["01", "02", "03", "04", "05"],
#     "采矿业": ["06", "07", "08", "09", "10", "11", "12"],
# }
#
# specinfo_SP = {
#     "上年度营收不够": ["1"],
#     "当年无经营房地产": ["2"],
#     "注销吊销退出": ["3"],
#     "专业变更退出": ["4"],
#     "辖区跨省退出": ["5"],
#     "单位界定错误": ["6"],
#     "投资项目完成": ["7"],
#     "停业歇业退出": ["8"],
#     "其他原因退出": ["9"],
# }
#
#
# def query_year_month(t_C, query_type, cityinfo, specinfo):
#     # count_temp = t_C.query.filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").count()
#     # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(t_C.数据处理地.startswith('6101%'),t_C.报表类别=="B").scalar()
#     s_n = {}
#     s = {}
#     # print(list(cityinfo.keys()))
#     # print(list(specinfo.keys()))
#     # print(list(cityinfo.values()))
#     for i in list(cityinfo.keys()):
#         if query_type == 'LW':
#             count_temp_haha = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][0]))
#             if len(cityinfo[i]) > 1:
#                 for k in range(1, len(cityinfo[i])):
#                     count_temp_haha = count_temp_haha.union_all(
#                         t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i][k])))
#         elif query_type == 'Tk':
#             if cityinfo.keys() in ["工业","建筑业","批发业","零售业","住宿业","餐饮业","房地产","服务业","投资","总计","五上"]:
#                 count_temp_haha = t_C.query.filter(t_C.所属专业==cityinfo[i][0])
#                 if len(cityinfo[i]) > 1:
#                     for k in range(1, len(cityinfo[i])):
#                         count_temp_haha = count_temp_haha.union_all(
#                             t_C.query.filter(t_C.所属专业==cityinfo[i][k]))
#             elif cityinfo.keys() in ["农林牧渔业","采矿业"]:
#                 count_temp_haha = t_C.query.filter(t_C.行业代码_17.startswith(cityinfo[i][0]))
#                 if len(cityinfo[i]) > 1:
#                     for k in range(1, len(cityinfo[i])):
#                         count_temp_haha = count_temp_haha.union_all(
#                             t_C.query.filter(t_C.行业代码_17.startswith(cityinfo[i][0])))
#         else:#query_type == 'SP' or 'SP_YEAR'
#             count_temp_haha = t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][0]))
#             if len(cityinfo[i]) > 1:
#                 for k in range(1, len(cityinfo[i])):
#                     count_temp_haha = count_temp_haha.union_all(
#                         t_C.query.filter(t_C.统计局代码.startswith(cityinfo[i][k])))
#
#
#         for j in list(specinfo.keys()):  # ['工业', ... '总计']
#             count_temp1 = 0
#             for list_temp in specinfo[j]:  # "总计"key对应的value["1", "2", "3", "4", "5", "6", "7", "8", "9"],
#                 # count_temp = t_C.query.filter(t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).count()
#                 if query_type == 'LW':
#                     count_temp = count_temp_haha.filter(t_C.报表类别 == list_temp).count()
#                     # count_temp = db.session.query(func.count(t_C.组织机构代码)).filter(
#                     # t_C.数据处理地.startswith(cityinfo[i]), t_C.报表类别 == list_temp).scalar()
#                 elif query_type == 'SP':
#                     count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
#                                                         t_C.审批类型.in_(['1', '2', '6', '9'])).count()
#                 elif query_type == 'SP_YEAR':
#                     count_temp = count_temp_haha.filter(t_C.所属专业 == list_temp, t_C.单位类型 == "1",
#                                                         t_C.审核类型.in_(['1', '2', '4'])).count()
#                 elif query_type == 'TK':
#                     count_temp = count_temp_haha.filter(t_C.审核类型 == list_temp, t_C.单位类型 == "1",
#                                                         ).count()
#
#                 count_temp1 = count_temp1 + count_temp
#             s_n[j] = count_temp1
#             # print(s_n, "```````````")
#             s[i] = copy.deepcopy(s_n)
#     # print(s)
#     return s
#
#
# L = []
# year_select=''
# query_type=''
# cityinfo=''
# specinfo=''
#
# s_all = {}
# for x in L:
#     if x == "year_report":
#         if query_type == "SP":
#             post_str = "SP_YEAR" + str(int(year_select) - 1)
#             t_C = globals()[post_str]
#             # print(post_str, "####")
#             # print(query_type, "####")
#             msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
#             s_all[x] = msg_temp
#         elif query_type == "TK":
#             post_str = "TK_YEAR" + str(int(year_select) - 1)
#             t_C = globals()[post_str]
#             # print(post_str, "####")
#             # print(query_type, "####")
#             msg_temp = query_year_month(t_C, "TK", cityinfo_SP, specinfo_SP)
#     else:
#         post_str = query_type + year_select + x
#         # print(post_str, "~~~~~")
#         t_C = globals()[post_str]
#         if query_type == "LW":
#             msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
#         elif query_type == "SP":
#             msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
#         elif query_type == "TK":
#             msg_temp = query_year_month(t_C, query_type, zhulaninfo_TK, binlaninfo_TK)
#         s_all[x + "月"] = msg_temp
# msg = json.dumps(s_all, ensure_ascii=False)
#
# s_all_lastyear = {}
# for x in L:
#     if x == "year_report":
#         if query_type == "SP":
#             post_str = "SP_YEAR" + str(int(year_select) - 2)
#             t_C = globals()[post_str]
#             msg_temp = query_year_month(t_C, "SP_YEAR", cityinfo_SP, specinfo_SP)
#             s_all_lastyear[x] = msg_temp
#         elif query_type == "TK":
#             post_str = "TK_YEAR" + str(int(year_select) - 2)
#             t_C = globals()[post_str]
#             msg_temp = query_year_month(t_C, "TK", zhulaninfo_TK, binlaninfo_TK)
#             s_all_lastyear[x] = msg_temp
#     else:
#         post_str = query_type + str(int(year_select) - 1) + x
#         # print(post_str, "~~~~~")
#         t_C = globals()[post_str]
#         if query_type == "LW":
#             msg_temp = query_year_month(t_C, query_type, cityinfo, specinfo)
#         elif query_type == "SP":
#             msg_temp = query_year_month(t_C, query_type, cityinfo_SP, specinfo_SP)
#         elif query_type == "TK":
#             msg_temp = query_year_month(t_C, query_type, zhulaninfo_TK, binlaninfo_TK)
#         s_all_lastyear[x + "月"] = msg_temp
# msg_lastyear = json.dumps(s_all_lastyear, ensure_ascii=False)




highTechManu_yyzzy = ["2710", "2720", "2730", "2740", "2750", "2761", "2762", "2770", "2780"]
highTechManu_hkhtzzy = ["3741", "3742", "3743", "3744", "3749", "4343"]
highTechManu_dztxzzy = ["3562", "3563", "3569", "3832", "3833", "3841", "3921", "3922", "3940", "3931", "3932", "3933",
                        "3934", "3939", "3951", "3952", "3953", "3971", "3972", "3973", "3974", "3975", "3976", "3979",
                        "3981", "3983", "3984", "3985", "3989", "3982", "3961", "3962", "3963", "3969", "3990"]
highTechManu_jsjbgzzy = ["3911", "3912", "3913", "3914", "3915", "3919", "3474", "3475"]
highTechManu_ylyqybzzy = ["3581", "3582", "3583", "3584", "3585", "3586", "3589", "4011", "4012", "4013", "4014",
                          "4015", "4016",
                          "4019", "4021", "4022", "4023", "4024", "4025", "4026", "4027", "4028", "4029", "4040",
                          "4090"]
highTechManu_xxhxpzzy = ["2664", "2665"]
highTechManu = highTechManu_yyzzy + highTechManu_hkhtzzy + highTechManu_dztxzzy + highTechManu_jsjbgzzy + highTechManu_ylyqybzzy + highTechManu_xxhxpzzy
print(highTechManu)