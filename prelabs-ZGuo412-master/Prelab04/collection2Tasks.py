#######################################################
#    Author:      <Ziyu Guo >
#    email:       <guo412@purdue.edu >
#    ID:           <ee364d25>
#    Date:         <2019/2/1 >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import csv
import copy
from pprint import pprint as pp
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab04')

def readfiles(problem, var1):
    sub_tech = os.path.join(DataPath, 'maps/technicians.dat')
    sub_vir = os.path.join(DataPath, 'maps/viruses.dat')
    with open(sub_tech, 'r') as file:    #read students.dat
        file.readline()
        file.readline()
        data = file.readlines()
        tech = [n.split() for n in data]
        tech_name = [''] * len(tech)
        tech_ID = [''] * len(tech)
        for i in range(0, len(tech)):
            tech_name[i] = tech[i][0] + ' ' + tech[i][1]
            tech_ID[i] = tech[i][3]
    id_name = dict(zip(tech_ID, tech_name))
    name_id = dict(zip(tech_name,tech_ID))
    with open(sub_vir, 'r') as file:
        file.readline()
        file.readline()
        data = file.readlines()
        vir = [m.split() for m in data]
        vir_name = [''] * len(vir)
        vir_id = [''] * len(vir)
        vir_price = [''] * len(vir)
        for j in range(0, len(vir)):
            vir_name[j] = vir[j][0]
            vir_id[j] = vir[j][2]
            vir_price[j] = vir[j][4][1:]
    vname_id = dict(zip(vir_name, vir_id))
    id_vname = dict(zip(vir_id,vir_name))
    id_price = dict(zip(vir_id,vir_price))
    vname_price = dict(zip(vir_name, vir_price))

    report_path = os.path.expanduser('~ee364/DataFolder/Prelab04/reports')
    report_list = os.listdir(report_path)
    report_id = copy.copy(report_list)
    for a in range(0, len(report_list)):
        report_id[a] = report_id[a].replace('report_','')
        report_id[a] = report_id[a].replace('.dat','')
    re_userid = [''] * len(report_list)
    report = [''] * len(report_list)
    for r in range(0, len(report_list)):
        report_file = os.path.join(report_path,report_list[r])
        with open(report_file) as file:
            reid = file.readlines(1)
            reid = [n.split() for n in reid]
            re_userid[r] = reid[0][2]
            file.readline()
            file.readline()
            file.readline()
            data = file.readlines()
            report[r] = [m.split() for m in data]

    if problem == '1':
        id = name_id[var1]
        vir = set('')
        for i in range(0, len(re_userid)):
            if id == re_userid[i]:
                for j in range(0, len(report[i])):
                    vir.add(report[i][j][1])
        vir = list(vir)
        for k in range(0, len(vir)):
            vir[k] = id_vname[vir[k]]
        num = [0] * len(vir)
        vir_num = dict(zip(vir, num))
        for m in range(0, len(re_userid)):
            if id == re_userid[m]:
                for n in range(0, len(report[m])):
                    vir_num[id_vname[report[m][n][1]]] += int(report[m][n][2])
        return vir_num
    elif problem == '2':
        id = vname_id[var1]
        tech = set('')
        for i in range(0, len(report)):
            for j in range(0, len(report[i])):
                if id == report[i][j][1]:
                    tech.add(re_userid[i])
                    break
        tech = list(tech)
        for k in range(0, len(tech)):
            tech[k] = id_name[tech[k]]
        num = [0] * len(tech)
        tech_num = dict(zip(tech, num))
        for m in range(0, len(report)):
            for n in range(0, len(report[m])):
                if id == report[m][n][1]:
                    tech_num[id_name[re_userid[m]]] += int(report[m][n][2])
        return tech_num
    elif problem == '3':
        tech_n = list(set(re_userid))
        spend = [0] * len(tech_n)
        for o in range(0, len(tech_n)):
            vir_nu = getTechWork(id_name[tech_n[o]])
            vn = list(vir_nu.keys())
            nu = list(vir_nu.values())
            for p in range(0, len(vir_nu)):
                spend[o] += float(vname_price[vn[p]]) * float(nu[p])
            spend[o] = float('%.2f' %spend[o])
        for q in range(0, len(tech_n)):
            tech_n[q] = id_name[tech_n[q]]
        tech_spend = dict(zip(tech_n, spend))
        return tech_spend
    elif problem == '4':
        vn = [' '] * len(vir_name)
        nu = [0]* len(vir_name)
        count = 0
        for r in range(0, len(vir_name)):
            vir_nu = getStrainConsumption(vir_name[r])
            nu_temp = sum(list(vir_nu.values()))
            if nu_temp > 0:
                vn[count] = vir_name[r]
                nu[count] = nu_temp * float(vname_price[vir_name[r]])
                nu[count] = float('%.2f' %nu[count])
                count = count + 1
        vn = vn[0:count]
        nu = nu[0:count]
        virspend = dict(zip(vn,nu))
        return(virspend)
    elif problem == '5':
        attend = list(set(re_userid))
        all_tech = list(set(tech_ID))
        abs_tech = set('')
        for s in range(0, len(all_tech)):
            if all_tech[s] not in attend:
                abs_tech.add(id_name[all_tech[s]])
        return abs_tech
    elif problem == '6':
        abs_vir = set('')
        for w in range(0, len(vir_name)):
            vir_nu = getStrainConsumption(vir_name[w])
            nu_temp = sum(list(vir_nu.values()))
            if nu_temp == 0:
                abs_vir.add(vir_name[w])
        return abs_vir
    return

def getTechWork(techName):
    number = readfiles('1', techName)
    return number

def getStrainConsumption(virusName):
    number = readfiles('2', virusName)
    return number

def getTechSpending():
    techSpend = readfiles('3', '')
    return techSpend

def getStrainCost():
    virSpend = readfiles('4', '')
    return virSpend

def getAbsentTechs():
    absent = readfiles('5', '')
    return absent

def getUnusedStrains():
    absent = readfiles('6', '')
    return absent