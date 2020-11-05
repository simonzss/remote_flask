from Zss.extensions import db
year = ["2019","2020"]
month = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
query_type = ["LW", "SP"]
query_type1 = ["SP_YEAR"]


def create_class(query_type, year, month=[""]):
    for x in query_type:
        for y in year:
            for z in month:
                if x == "LW":
                    # if z in ("2", "3", "4", "5", "6", "7", "8", "9"):
                    #     globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month),
                    #                                      {'__tablename__': y + "0" + z + "_month",
                    #                                       '__bind_key__': 'zss'})
                    # else:
                    globals()[str(x + y + z)] = type(x + y + z, (),
                                                         {'__tablename__': y + z + "_month", '__bind_key__': 'zss'})
                elif x == "SP":
                    # if z in ("2", "3", "4", "5", "6", "7", "8", "9"):
                    #     globals()[str(x + y + z)] = type(x + y + z, (db.Model, Month),
                    #                                      {'__tablename__': y + "0" + z + "_month_1"})
                    # else:
                    globals()[str(x + y + z)] = type(x + y + z, (),
                                                         {'__tablename__': y + z + "_month_1"})
                elif x == "SP_YEAR":
                    globals()[str(x + y + z)] = type(x + y + z, (),
                                                     {'__tablename__': y + z + "_year_1"})



class Month():
    数据处理地 = db.Column(db.Unicode(255))
    组织机构代码 = db.Column(db.Unicode(255), primary_key=True)
    统计局代码 = db.Column(db.Unicode(255))
    所属专业 = db.Column(db.Unicode(255))
    审批类型 = db.Column(db.Unicode(255))
    单位类型 = db.Column(db.Unicode(255))
    单位详细名称 = db.Column(db.Unicode(255))

# create_class(query_type, year, month=month)
create_class(query_type1, year)


L = []
x = "02"
y = "12"
for t in range(int(x),int(y)+1,1):
    if t<10:
        L.append("0"+str(t))
    else:
        L.append(str(t))

print(L)

# from Zss.models import *
print(globals())
class A_SP_YEAR2020():
    pass
print(SP_YEAR2020.__name__)