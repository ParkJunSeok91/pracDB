__author__ = 'user'

import glob
import sqlite3

#데이터베이스를 핸들 클래스
class DatabaseHandler:
    #생성자에서는 con과 cursor를 설정해줍니다
    def __init__(self):
        self.con = sqlite3.connect("test.db")
        self.cursor = self.con.cursor()
    #테이블을 만드는 함수입니다
    def CreateTable(self):
        create = "CREATE TABLE test(DataDate DATE, Num1 VARCHAR(4), Num2 VARCHAR(4), Num3 VARCHAR(4))"
        self.cursor.execute(create)
    #테이블에 값을 넣어주는 함수입니다
    #InsertValues의 인자 값으로 dic은 BringData에서 생성한
    #Dictionary입니다
    def InsertValues(self, dic):
        values = "INSERT INTO test VALUES('{DataDate}', '{Num1}', '{Num2}', '{Num3}')".format_map(dic)
        self.cursor.execute(values)
        self.con.commit()
    #connect을 종료해주는 함수입니다
    def DatabaseClose(self):
        self.con.close()


#glob모듈을 이용하여 해당 파일을 읽어서 데이터를 가져오는 클래스입니다
class globHandler:
    #생성자에서 파일 리스트들을 저장하고 변수들을 초기화합니다
    def __init__(self, name):
        self.file_list = glob.glob(name)
        self.data = ''
        self.data_list = []
        self.dic = {}
    #모든 값을 읽어서 ','로 나누어 준 뒤 마지막 값은 '\n'을 제거해주고
    #Dictionary에 가져온 값들은 나누어 넣어준뒤
    #테이블에 값을 넣어주는 InserValues 함수를 호출합니다
    #BringData인자 값으로 db는 DatabaseHandler 클래스의 인스턴스입니다
    def BringData(self, db):
        for x in range(len(self.file_list)):
            with open(self.file_list[x], 'r') as f:
                data = f.read()
                data_list = data.split(',')
                data_list[3] = data_list[3][:-1]
                self.d = {
                    "DataDate": data_list[0],
                    "Num1": data_list[1],
                    "Num2": data_list[2],
                    "Num3": data_list[3]
                }
                db.InsertValues(self.d)


db = DatabaseHandler()
db.CreateTable()
gh = globHandler("*_DATA.txt")
gh.BringData(db)
db.DatabaseClose()
