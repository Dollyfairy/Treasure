import db

def create(line_id,gender,time,phone,address,name):
    db.run("insert into treasure_member (Member_LINEid,Member_Gender,Member_Birthady,Member_Phone,Member_Address,Member_Name) values(\"%s\", \"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %(line_id,gender,time,phone,address,name))
    return 0

print('memberOk')
