# -*- coding: utf-8 -*-

import csv
#from copy import deepcopy


def identity_dict(person):
    library=dict()
    for human in person:
        library[human.id_]=human
        library[human.name]=human.id_
    return library
    



def lexical_analysis(transitions):
    #transitions is an array of words
    accepted_words=["brother","sister","father","mother",
                    "uncle","auntie","great","grand","cousin",
                    "siblings","paternal","maternal","son","daughter"]
    for word in transitions:
        if word not in accepted_words:
            print("Invalid relationship. Unreadable")
            return False
        else:
            return transitions
            
            

class Person():
    def __init__(self,id_,name,title,dad,mom,spouse,brother,sister,son,daughter):
        self.name=name
        self.id_=id_
        self.title=title
        self.dad=dad
        self.mom=mom
        self.spouse=list(spouse.split(","))
        self.brother=list(brother.split(","))
        self.sister=list(sister.split(","))
        self.son=list(son.split(","))
        self.daughter=list(daughter.split(","))
        self.genders=None
        
        
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
            
    def info_display(self):
        print("Name : ",self.name)
        print("ID : ", self.id_)
        print("Father : ",self.dad)
        print("Mother : ", self.mom)
        print("Spouse : ",self.spouse)
        print("Brother : ",self.brother)
        print("Sister : ",self.sister)
        print("Son :",self.son)
        print("Daughter : ",self.daughter)
            
    def gender(self):
        for family in members:
            if self.id_ in family.dad or self.id_ in family.son or self.id_ in family.brother:
                return "Male"
            elif self.id_ in family.mom or self.id_ in family.sister or self.id_ in family.daughter:
                return "Female"
            elif self.id_ == family.mom or self.id_ == family.sister or self.id_ == family.daughter:
                return "Female"
            elif self.id_ == family.dad or self.id_ == family.son or self.id_ == family.brother:
                return "Male"
            else:
                continue
        for family in members:
            if family.genders is None:
                for person in members:
                    if family.id_ in person.spouse:
                        if person.genders=="Male":
                            return "Female"
                        elif person.genders=="Female":
                            return "Male"
            
    
            
        
        
class FamilyTreeSearch(Person):
    def __init__(self,members):
        self.members=members
        
    def search(self):
        transitions=input("Relationship").lower().split(" ")
        subject=input("Enter a name")
        #We need to get the subject's ID at this point
        if subject not in IDENTITY_Lib:
            print("Person not found in data or invalid form ! ")
            return 0
        else:
            ID=IDENTITY_Lib[subject]
        if lexical_analysis(transitions) == False:
            print("Invalid relationship or format ")
            return 0
        else:
            possible=[]
            for word in transitions:
                if word=="brother":
                    possible=self.brother(ID)
                elif word=="sister":
                    possible=self.sister(ID)
        
        
        pass
    
    def brother(identity_number):
        pass
    
    def sister(identity_number):
        pass
    
    def father(identity_number):
        pass
    
    def mother(identity_number):
        pass
    
    def uncle(identity_number):
        pass
    
    def auntie(identity_number):
        pass
    
    def great(identity_number):
        pass
    
    def grand(identity_number):
        pass
    
    def cousin(identity_number):
        pass
    
    def siblings(identity_number):
        pass
    
    def maternal(identity_number):
        pass
    
    def paternal(identity_number):
        pass
    
    def son(identity_number):
        pass
    
    def daughter(identity_number):
        pass
    
    
                
        
members=list()
count=0

def format_and_parse():
    with open('britroyals.csv','r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            if line[0]=="ID":
                continue
            else:
                p=Person(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9])
                members.append(p)
        
    for p in list(members):
        p.genders=p.gender()
    


if __name__=="__main__":
    format_and_parse()
    IDENTITY_Lib=identity_dict(members)
    IDENTITY_Lib["1"].introduce()
    print(IDENTITY_Lib["Alfred the Great"])

     