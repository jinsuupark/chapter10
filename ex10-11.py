dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책'
}
print(dic)

print(dic['boy'])
print(dic['book'])
# print(dic['girl'])

#키와값의 쌍
dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책'
}
print(dic.get('boy'))
print(dic.get('girl'))
print(dic.get('girl',"사전에 없는 단어입니다."))

dic['boy'] ='남자아이'
dic['girl'] ='소녀'
del dic['book']
print(dic)

print(dic.keys()) #리스트처럼 보이지만 data-type 이  dict_keys 이다.
print(dic.values())
print(dic.items())


keylist = dic.keys()
for key in keylist:
    print(key,dic[key])

#사전 관리 업데이트
dic = {'boy':'소년','school':'학교','book':'책'}
dic2 = {'student':'학생','teacher':'선생님','book':'서적'}

dic.update(dic2)
print(dic)
#사전관리 사전으로 변환
li =[
    ['boy','소년'],
    ['school','학교'],
    ['teacher','선생님'],

]
dic = dict(li)
print(dic)

