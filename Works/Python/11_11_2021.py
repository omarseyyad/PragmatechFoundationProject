telebeler=[
    {
    'ad':'Samir',
    'soyad':'Hemidov',
    'yas':30
    },
    {
    'ad':'Memmed',
    'soyad':'Salamov',
    'yas':20
    },
    {
    'ad':'Aliye',
    'soyad':'Qurbanova',
    'yas':16
    },
    {
    'ad':'Sahil',
    'soyad':'Qeniyev',
    'yas':45
    },
    {
    'ad':'Ehmed',
    'soyad':'Qeniyev',
    'yas':50
    }
    
    
]

# for i in range(len(telebeler)):
#     print(telebeler[i]['ad'])


# yaslar=[30,20,16,45,50]
# cem=yaslar[0]+yaslar[1]+yaslar[2]+yaslar[3]+yaslar[4]
# print(cem)


# for i in range(len(telebeler)):
#     if(telebeler[i]['ad']=='Ehmed'):
#         print(telebeler[i])

# ad=input('istifadecinin adini daxil edin:')
# if ad==('samir'):
#         print(telebeler[0])


ad=input('istifadecinin adini daxil edin:')
for i in range(len(telebeler)):
    if(ad==telebeler[i]['ad']):
        print(telebeler[i])