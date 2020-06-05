# -*- coding: utf-8 -*-

import csv

class Person():
    def __init__(self,id_,name,title,dad,mom,spouse,son,daughter,brother,sister):
        self.name=name
        self.id_=id_
        self.title=title
        self.dad=dad
        self.mom=mom
        self.spouse=spouse
        self.brother=brother
        self.sister=sister
        self.son=son
        self.daugther=daughter
        
    def __str__(self):
        if self.title!="None":
            return (self.name + ","+self.title)
        else:
            return self.name
        
    def introduce(self):
        if self.title!="None":
            print("I am "+self.name+ " , "+self.title+"!")
        else:
            print("I am "+self.name)
        
class FamilyTree(Person):
    def __init__(self,members):
        self.members=members
        
members=set()
count=0
with open('britroyals.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        if line[0]=="ID":
            continue
        p=Person(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9])
        print(p)
        
        
    

         
