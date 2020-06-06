# Family-Tree-Computer
To find the person related to the subject via a given relationship and also , in the second part, to input more information and deduce the relationship to the 2 related subjects. I have used the British Royal Family as a testing ground

## Part I
We want to find the person related to the subject given a relationship
For example:
Input: 

Relationship : Paternal great grand uncle

Subject : Richard II

Output:

Edmund Crouchback , Earl of Lancaster, Leicester and Derby
(Will return None should the person exist in real life but not included in the data)

## Part II
We want the program to make inferences of the information we feed in and then output the relationship 

For example:

Inputs:

#In format [Subject_1 , Subject_2 , Relationship] -> Subject 1 is of a Relationship to Subject 2

Edward the Black Prince , Richard II , Father

John of Gaunt , Richard II , Uncle

From here, it can be deduced that Richard II is the nephew of John of Gaunt, hence the new relationship

Richard II , John of Gaunt , Nephew

Of course this is not the only inference the program can make. There is quite a few but there is insufficient time to type them down

Prompt: What is the relationship between John of Gaunt and Edward the Black Prince  ?

Output:

Brother

