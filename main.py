#!/usr/bin/python

import sys
import re
import json

def is_delimiter(line):
    rex = re.compile('^202[0-9]+')
    return rex.search(line)

def flatString(r_line):
    return r_line.replace("default ", "default_").replace("INFO  ", "INFO ")

def get_chunk_list(fd):
    chunk_list = []
    chunks = []
    values = []
    while True:
        line = fd.readline()
        if not line:
            break
        else:
            line = line[0:-1]
        if is_delimiter(line):
            if chunks:
                chunks.append(values)
                chunk_list.append(chunks)
                chunks = []
                values = []
            chunks.append(flatString(line))
        else:
            if chunks:
                # Values of not including commnad will be dropped
                values.append(line)
    if chunks:
        chunks.append(values)
        chunk_list.append(chunks)
    return chunk_list

def is_Correlation(line):
    rex = re.compile('Action invoked')
    return rex.search(line)

def getCorrelationDic(c_list):
    CorrelationDic={}
    CorrelList=[]
    for item in range(len(c_list)):
        if is_Correlation(c_list[item][0]):
            CorrelationID = (c_list[item][0].split(' ')[5][1:-1])
            CorrelationDic[CorrelationID] = [c_list[item]]
            CorrelList.append(CorrelationID)
            continue
        if not CorrelationDic:
            continue
        for c_id in CorrelList:
            if c_list[item][0].find(c_id) > 1:
                CorrelationDic[CorrelationID].append(c_list[item])

    return CorrelationDic

def isJson(j_line):
    try:
        jo = json.loads(j_line)
    except ValueError as e:
        return False
    return True

def showLog(c_dic):
    for item in c_dic.keys():
        print("Correlation ID : %s" %(item))
        for idx in range(len(c_dic[item])):
            log_list=c_dic[item][idx][0].split(' ')
            log_string="%s %s %6s" % (log_list[0], log_list[1], log_list[2])
            for l_idx in range(6, len(log_list)):
                log_string="%s %s" % (log_string, log_list[l_idx])
            print(log_string)
            if c_dic[item][idx][1]:
                for v_idx in range(len(c_dic[item][idx][1])):
                    if isJson(c_dic[item][idx][1][v_idx]):
                        print(json.dumps(json.loads(c_dic[item][idx][1][v_idx]), indent=4))
                    else:
                        print("%33s %s" %("", c_dic[item][idx][1][v_idx]))
        print("")

def process(fp):
    with open(fp) as fd:
        c_l = get_chunk_list(fd)
    showLog(getCorrelationDic(c_l))

def main():
    process(sys.argv[1])

if __name__ in ("__main__"):
    main()
