#complex collection item

# stu_dict1={'irin':[23,34,45,67],'juval':[56,89,23,34],'tina':[22,33,43,43]}
# for stu,mark_list in stu_dict1.items():
#     total=0
#     for marks in mark_list:
#         total=total+marks
#     print(f"{stu} got {total} marks as total")

stu_dict2={'irin':{'phy':23,'chem':34,'maths':45,'cs':67},
           'juval':{'phy':23,'chem':34,'maths':45,'cs':67},
           'tina':{'phy':23,'chem':34,'maths':45,'cs':67}}
for stu,mark_list in stu_dict2.items():
    total=0
    for marks in mark_list.values():
        total=total+marks
    print(f"{stu} got {total} marks as total")