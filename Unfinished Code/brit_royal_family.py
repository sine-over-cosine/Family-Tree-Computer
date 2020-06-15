# -*- coding: utf-8 -*-

import csv
#from copy import deepcopy


def identity_dict(person):
    library=dict()
    for human in person:
        library[human.id_]=human
    return library
    
def name_query(person):
    library=dict()
    for human in person:
        library[human.name]=human.id_
    return library
    


def lexical_analysis(transitions):
    #transitions is an array of words
    accepted_words=["brother","sister","father","mother",
                    "uncle","auntie","great","grand","cousin",
                    "siblings","paternal","maternal","son","daughter","spouse"]
    for word in transitions:
        if word not in accepted_words:
            print("Invalid relationship. Unreadable")
            return False
        else:
            return transitions
            
            

class Person():
    def __init__(self,id_,name,title,dad,mom,spouse,brother,sister,son,daughter):
        if name[-1]==" ":
            self.name=name[:-1]
        else:
            self.name=name
        self.id_=id_
        self.title=title
        self.dad=list(dad.split(" "))
        self.mom=list(mom.split(" "))
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
        relationship=input("Relationship\n")
        transitions=relationship.lower().split(" ")
        subject=input("Enter a name\n")
        #We need to get the subject's ID at this point
        if subject not in NAME_Lib:
            print("Person not found in data or invalid form ! ")
            return 0
        for mini_id in IDENTITY_Lib:
            if IDENTITY_Lib[mini_id].name==subject:
                print("ID: {} , NAME: {}, TITLE : {}".format(mini_id,self.members[mini_id].name,self.members[mini_id].title))
            else:
                continue
        ID=input("Enter one of the above ID--Will return a wrong answer otherwise \n")
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
                elif word=="son":
                    possible=self.son(ID)
                elif word=="daughter":
                    possible=self.daughter(ID)
                elif word=="father" or word=="paternal":
                    possible=self.father(ID)
                elif word=="mother" or word=="maternal":
                    possible=self.mother(ID)
                elif word=="siblings":
                    possible=self.siblings(ID)
                elif word=="uncle":
                    if "paternal" in transitions:
                        possible=self.uncle(True)
                    elif "maternal" in transitions:
                        possible=self.uncle(False)
                    else:
                        possible=self.uncle(True)+self.uncle(False)
                elif word=="auntie":
                    if "paternal" in transitions:
                        possible=self.auntie(True)
                    elif "maternal" in transitions:
                        possible=self.auntie(False)
                    else:
                        possible=self.auntie(True)+self.auntie(False)
                elif word=="grand" or word=="great":
                    if "paternal" in transitions:
                        possible=self.grand(True)
                    elif "maternal" in transitions:
                        possible=self.grand(False)
                    else:
                        possible=self.grand(True)+self.great(False)
                elif word=="spouse":
                    possible=self.spouse(ID)
        if len(possible)==0:
            print("No one in data or no one matched the relationship")
        else:
            print("{} 's {} is/are':".format(subject,relationship))
            for t in possible:
                if t == "None":
                    continue
                else:
                    if IDENTITY_Lib[t].title is not None:
                        print(IDENTITY_Lib[t].name,",",IDENTITY_Lib[t].title)
                    else:
                        print(IDENTITY_Lib[t].name)
    
    def brother(identity_number):
        person=IDENTITY_Lib[identity_number].brother
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
            
    
    def sister(identity_number):
        person=IDENTITY_Lib[identity_number].sister
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
    
    
    def father(self,identity_number):
        person=IDENTITY_Lib[identity_number].dad
        print(person)
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return list(person)
    
    def mother(identity_number):
        person=IDENTITY_Lib[identity_number].mom
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
    
    def uncle(identity_number,paternal=True):
        '''
        Either the maternal side or the paternal side brother
        '''
        if paternal==True:
            person=IDENTITY_Lib[identity_number].dad
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                info=IDENTITY_Lib[person[0]].brothers
                if len(info)>0:
                    return list(info)
                else:
                    print("There is no one matching the relationship")
                    return list()
        else:
            person=IDENTITY_Lib(identity_number).mom
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                info=IDENTITY_Lib[person[0]].brothers
                if len(info)>0:
                    return list(info)
                else:
                    print("There is no one matching the relationship")
                    return list()
            
            
    
    def auntie(identity_number,paternal=True):
        if paternal==True:
            person=IDENTITY_Lib[identity_number].dad
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                info=IDENTITY_Lib[person[0]].sisters
                if len(info)>0:
                    return list(info)
                else:
                    print("There is no one matching the relationship")
                    return list()
        else:
            person=IDENTITY_Lib[identity_number].mom
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                info=IDENTITY_Lib[person[0]].sisters
                if len(info)>0:
                    return list(info)
                else:
                    print("There is no one matching the relationship")
                    return list()
    
    def great(identity_number,paternal=True):
        #To go up one generation"
        if paternal==True:
            person=IDENTITY_Lib[identity_number].dad
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                person
        else:
            person=IDENTITY_Lib[identity_number].mom
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                return list(person)
    
    def grand(identity_number,paternal=True):
        #To go up one generation"
        if paternal==True:
            person=IDENTITY_Lib[identity_number].dad
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                person
        else:
            person=IDENTITY_Lib[identity_number].mom
            if len(person)==0:
                print("There is no one matching the relationship")
                return list()
            else:
                return list(person)
       
    
    
    def siblings(self,identity_number):
        person=IDENTITY_Lib[identity_number].sister + IDENTITY_Lib[identity_number].brother
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
    
    def son(identity_number):
        person=IDENTITY_Lib[identity_number].son
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
    
    def daughter(identity_number):
        person=IDENTITY_Lib[identity_number].daughter
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
    
    def spouse(self,identity_number):
        person=IDENTITY_Lib[identity_number].spouse
        if len(person)==0:
            print("There is no one matching the relationship")
            return list()
        else:
            return person
                
        
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
    NAME_Lib=name_query(members)
    print(IDENTITY_Lib["191"].name=="Victoria")
    FamilyTreeSearch(IDENTITY_Lib).search()
    #print(IDENTITY_Lib["258"].brother)

     