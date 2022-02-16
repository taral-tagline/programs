Department = {
    'Python':
    [
        {
            'Name':'Taral',
            'Surname':'Patel'
        },
        {
            'Name':'Sanket',
            'Surname':'Dubaria'
        },
        {
            'Name':'Zeel',
            'Surname':'Radadiya'
        }
    ]
}
#Department['Python'][1]['Surname'] = 'Dubariya'
#print(Department['Python'][1]['Surname'])

for i in range(0,len(Department['Python'])):
    if Department['Python'][i]['Name']== 'Taral':
        Department['Python'][i]['Framework'] = 'Flask'
    #else :
     #   Department['Python'][i]['Framework'] = 'Django'
    for key,value in Department['Python'][i].items():
        print(key,end=' : ')
        print(value)
    print("------------------------")


'''
data = {
    'python':{
        'Framework' : 'Django',
        'Members' : 6
    }
}

data['python']['Framework']='Flask'
data['python'].update({'Company': 'Tagline'})
data['python'].pop('Company')
print(data)
'''