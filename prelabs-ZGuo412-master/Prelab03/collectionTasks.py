#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/1/26 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv
from pprint import pprint as pp
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab03')

def readcom(Components):
    if Components == "R":
        sub_com = os.path.join(DataPath, 'maps/resistors.dat')
    elif Components == "I":
        sub_com = os.path.join(DataPath, 'maps/inductors.dat')
    elif Components == 'C':
        sub_com = os.path.join(DataPath, 'maps/capacitors.dat')
    elif Components == 'T':
        sub_com = os.path.join(DataPath, 'maps/transistors.dat')
    else:
        return
    with open(sub_com, 'r') as file:    #read components.dat
        file.readline()
        file.readline()
        file.readline()
        data = file.readlines()
        pro = [n.split() for n in data]
        com_ID = [''] * len(pro)
        price = [''] * len(pro)
        for i in range(0,len(pro)):
            com_ID[i] = pro[i][0]
            price[i] = pro[i][1]
    x = com_ID, price
    return x
def readfiles(projectID, Components,problem,id2):
    sub_project = os.path.join(DataPath, 'maps/projects.dat')
    sub_student = os.path.join(DataPath,'maps/students.dat')
    with open(sub_student, 'r') as file:    #read students.dat
        file.readline()
        file.readline()
        data = file.readlines()
        stu = [n.split() for n in data]
        name = [''] * len(stu)
        stu_ID = [''] * len(stu)
        for i in range(0, len(stu)):
            name[i] = stu[i][0] + ' ' + stu[i][1]
            stu_ID[i] = stu[i][3]
    id_name = dict(zip(stu_ID, name))
    name_id = dict(zip(name,stu_ID))
    with open(sub_project, 'r') as file:    #read projects.dat
        file.readline()
        file.readline()
        data = file.readlines()
        pro = [n.split() for n in data]
        circuit = [''] * len(pro)
        Pro_ID = [''] * len(pro)
        for i in range(0,len(pro)):
            circuit[i] = pro[i][0]
            Pro_ID[i] = pro[i][1]
        pro_id = sorted(list(set(Pro_ID))) # I really need to convert list and sets. And I will find a way to avoid this by asking TA next week or google
        cir = [[' ']] * len(pro_id)
        pro_cir = dict(zip(pro_id,cir))
    for n in range(0, len(pro_id)):
        pro_cir[pro_id[n]] = ['']
        for k in range(0, len(Pro_ID)):
            if pro_id[n] == Pro_ID[k]:
                pro_cir[pro_id[n]].append(circuit[k])
    for x in range(0, len(pro_cir)):
        pro_cir[pro_id[x]] = pro_cir[pro_id[x]][1:]

    if Components == "R":
        sub_com = os.path.join(DataPath, 'maps/resistors.dat')
    elif Components == "I":
        sub_com = os.path.join(DataPath, 'maps/inductors.dat')
    elif Components == 'C':
        sub_com = os.path.join(DataPath, 'maps/capacitors.dat')
    elif Components == 'T':
        sub_com = os.path.join(DataPath, 'maps/transistors.dat')
    else:
        return
    with open(sub_com, 'r') as file:    #read components.dat
        file.readline()
        file.readline()
        file.readline()
        data = file.readlines()
        pro = [n.split() for n in data]
        com_ID = [''] * len(pro)
        price = [''] * len(pro)
        for i in range(0,len(pro)):
            com_ID[i] = pro[i][0]
            price[i] = pro[i][1]
    cir_path = os.path.expanduser('~ee364/DataFolder/Prelab03/circuits')
    cir_list = os.listdir(cir_path)
    cir_com = [['']] * len(cir_list)
    cir_stu = [['']] * len(cir_list)
    for y in range(0, len(cir_list)):
        cir_id = 'circuits/' + cir_list[y]
        sub_circuit = os.path.join(DataPath,cir_id)
        with open(sub_circuit, 'r') as file:
            file.readline()
            file.readline()
            data = file.readlines()
            for i in range(0, len(data) - 1):
                data[i] = data[i][0:len(data[i]) - 1]
        cir_com[y] = (data[data.index('Components:') + 2: len(data)])
        cir_stu[y] = data[0: data.index('Components:') - 1]
    for m in range(0, len(cir_com)):
        for a in range(0,len(cir_com[m])):
            cir_com[m][a] = cir_com[m][a][2:len(cir_com[m][a])]

    if problem == 1:
        if projectID not in Pro_ID:
            raise ValueError("PROJECT ID NOT FOUND")
        else:
            cir_need = pro_cir[projectID]
            com_list = [['']]
            for s in range(0,len(cir_need)):
                com_list.extend(cir_com[cir_list.index('circuit_' + cir_need[s] + '.dat')])
            com_list = sorted(list(set(com_list[1:])))
            count = 0
            for com_li in com_list:
                if com_li in com_ID:
                    count += 1
            return count
    elif problem == 2:
        student = projectID
        if student not in name:
            raise ValueError("STUDENT NOT FOUND")
        else:
            need_id = stu_ID[name.index(student)]
            com_list = ['']
            for f in range(0, len(cir_stu)):
                if need_id in cir_stu[f]:
                    com_list.extend(cir_com[f])
            com_list = sorted(list(set(com_list[1:])))  #I really need to convert sets and lists
            count = 0
            for com_li in com_list:
                if com_li in com_ID:
                    count += 1
            return count
    elif problem == 3:
        student = projectID
        if student not in name:
            raise ValueError("STUDENT NOT FOUND")
        else:
            need_id = stu_ID[name.index(student)]
            cir_li = ['']
            for g in range(0, len(cir_stu)):
                if need_id in cir_stu[g]:
                    cir_li.append(cir_list[g])
            cir_li = cir_li[1:]
            pro_id = ['']
            for f in range(0, len(cir_li)):
                for s in range(0, len(circuit)):
                    if circuit[s] in cir_li[f]:
                        pro_id.append(Pro_ID[s])
            pro_id = pro_id[1:]
            return set(pro_id)
    elif problem == 4:
        if projectID not in Pro_ID:
            raise ValueError("PROJECT ID NOT FOUND")
        else:
            cir_need = pro_cir[projectID]
            stu_list = ['']
            for s in range(0, len(cir_need)):
                stu_list.extend(cir_stu[cir_list.index('circuit_' + cir_need[s] + '.dat')])
            stu_list = stu_list[1:]
            for f in range(0, len(stu_list)):
                stu_list[f] = id_name[stu_list[f]]
            return set(stu_list)
    elif problem == 5:
        code1, price1 = readcom('R')
        code2, price2 = readcom('I')
        code3, price3 = readcom('C')
        code4, price4 = readcom('T')
        code1.extend(code2)
        code1.extend(code3)
        code1.extend(code4)
        price1.extend(price2)
        price1.extend(price3)
        price1.extend(price4)
        code = code1
        price = price1
        sum = [0.00] * len(pro_id)
        for f in range(0, len(pro_id)):
            cir_need = pro_cir[pro_id[f]]
            cir_li = ['']
            for s in range(0,len(cir_need)):
                cir_li.extend(cir_com[cir_list.index('circuit_' + cir_need[s] + '.dat')])
            cir_li = cir_li[1:]
            for h in range(0,len(cir_li)):
                sum[f] += float(price[code.index(cir_li[h])][1:])
                sum[f] = float('%.2f' %sum[f])
        cost_dict = dict(zip(pro_id,sum))
        return cost_dict
    elif problem == 6:
        pro_set = set('')
        comp = projectID
        cir_li = ['']
        for f in range(0,len(comp)):
            for s in range(0,len(cir_com)):
                if comp[f] in cir_com[s]:
                    cir_li.append(cir_list[s])
        cir_li = cir_li[1:]
        for c in range(0, len(cir_li)):
            for v in range(0, len(circuit)):
                if circuit[v] in cir_li[c]:
                    pro_set.add(Pro_ID[v])
        return pro_set
    elif problem == 7:
        if projectID not in Pro_ID:
            raise ValueError("ID1 not found")
        elif id2 not in Pro_ID:
            raise ValueError("ID2 NOT FOUND")
        else:
            cir_l1 = pro_cir[projectID]
            cir_l2 = pro_cir[id2]
            common = ['']
            com_l1 = ['']
            com_l2 = ['']
            for u in range(0, len(cir_l1)):
                com_l1.extend(cir_com[cir_list.index('circuit_' + cir_l1[u] + '.dat')])
            com_l1 = com_l1[1:]
            for o in range(0, len(cir_l2)):
                com_l2.extend(cir_com[cir_list.index('circuit_' + cir_l2[o] + '.dat')])
            com_l2 = com_l2[1:]
            for l1 in com_l1:
                if l1 in com_l2:
                    common.append(l1)
            common = sorted(list(set(common[1:])))
            return common
    elif problem == 8:
        coun= [0]* len(projectID)
        for l in range(0, len(projectID)):
            for u in range(0, len(pro_id)):
                need_circuit = pro_cir[pro_id[u]]
                need_com = ['']
                for o in range(0, len(need_circuit)):
                    need_com.extend(cir_com[cir_list.index('circuit_' + need_circuit[o] + '.dat')])
                need_com = need_com[1:]
                coun[l] += need_com.count(projectID[l])
        report = dict(zip(projectID,coun))
        return report
    elif problem == 9:
        cirset = set('')

        for l in range(0, len(projectID)):
            for u in range(0,len(cir_stu)):
                if name_id[projectID[l]] in cir_stu[u]:
                    cirset.add(cir_list[u][8:15])
        return cirset

    elif problem == 10:
        cirset = set('')
        for l in range(0,len(projectID)):
            for u in range(0,len(cir_com)):
                if projectID[l] in cir_com[u]:
                    cirset.add(cir_list[u][8:15])
        return cirset
def getComponentCountByProject(projectID, componentSymbol):
    count =  readfiles(projectID,componentSymbol,1,'')
    return count
def getComponentCountByStudent(studentName, componentSymbol):
    count = readfiles(studentName,componentSymbol,2,'')
    return count

def getParticipationByStudent(studentName):
    pro_id = readfiles(studentName,'R',3,'')
    return pro_id

def getParticipationByProject(projectID):
    stu_name = readfiles(projectID,'R',4,'')
    return stu_name

def getCostOfProjects():
    cost = readfiles('','R',5,'')
    return cost

def getProjectByComponent(ComponentIDs):
    comp = sorted(list(ComponentIDs))
    pro_set = readfiles(comp,'R',6,'')
    return pro_set
def getCommonByProject(projectID1, projectID2):
    common = readfiles(projectID1,'R', 7,projectID2)
    return common
def getComponentReport(componentIDs):
    componentIDs = list(componentIDs)
    report = readfiles(componentIDs,'R',8,'')
    return report

def getCircuitByStudent(studentNames):
    studentNames = list(studentNames)
    cir = readfiles(studentNames,'R',9,'')
    return cir

def getCircuitByComponent(componentIDs):
    componentIDs = list(componentIDs)
    cir = readfiles(componentIDs,'R',10,'')
    return cir