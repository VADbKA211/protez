from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#----Кновка в главное меню-------
buttonmain = KeyboardButton('Головне меню 🔙')



#------menu--------

b1 = KeyboardButton('📩Нове звернення')
b2 = KeyboardButton('🌐Ми в соціальних мережах')

#-------Главное меню--------

s1 = KeyboardButton('Покрокова інструкція з отримання протезу')
s2 = KeyboardButton('Найпоширеніші запитання')
s3 = KeyboardButton('Історії побратимів')
s4 = KeyboardButton('Перелік документів')
s5 = KeyboardButton('Центри протезування в Україні')
s6 = KeyboardButton('Про проєкт')
sector = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
sector.insert(s1)
sector.add(s5)
sector.add(s3)
sector.insert(s4)
sector.insert(s6)
sector.insert(s2)

#----------------------Покрокова інструкція зотримання протезу------------------------------------

p1 = KeyboardButton('1 крок')
p2 = KeyboardButton('2 крок')
p3 = KeyboardButton('3 крок')
p4 = KeyboardButton('4 крок')
p5 = KeyboardButton('5 крок')
p6 = KeyboardButton('На що звернути увагу')
p7 = KeyboardButton('Головне меню 🔙')
pokrokova = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
pokrokova.add(p1, p2, p3, p4, p5, p6, p7)

#----------------------------Найпоширеніші запитання--------------------------------------------
n1  = KeyboardButton('Вибрати питання')
n2  = KeyboardButton('Довідник користувача')
n3  = KeyboardButton('Зворотній зв`язок')
n4  = KeyboardButton('Істрії')
n5  = KeyboardButton('Документи')
zaput = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
zaput.add(n1, n2, n3, n4, n5, buttonmain)

#---------------------Історії  про протезування від побратимів----------------------------------------
i1 = KeyboardButton('Протезувався в Україні')
i2 = KeyboardButton('Протезувався за кордоном')
i3 = KeyboardButton('Як можуть обманути?')
istor = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
istor.add(i1, i2, i3, buttonmain)

#---------ukr protez

dali = KeyboardButton('Ще історії')
nazad = KeyboardButton('Попереднє меню↩️')
istor_ukr = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
istor_ukr.add(dali, nazad, buttonmain)



dali2 = KeyboardButton('Ще  історії')
nazad3 = KeyboardButton('Попереднє меню↩️')
istor_ukr3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
istor_ukr3.add(dali2, nazad3, buttonmain)


#---za kordon

dali2 = KeyboardButton('Ще  історії')
nazad2 = KeyboardButton('Попереднє меню↩️')
istor_kord = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
istor_kord.add(dali2, nazad2, buttonmain)







############ i = KeyboardButton('') ###################



#-------------------------------Зразки документів------------------------------------------------------------

zraz1 = KeyboardButton('Для  проходження МСЕК')
zraz2 = KeyboardButton('Для протезування')
zraz3 = KeyboardButton('Для отримання статусу УБД')
zraz4 = KeyboardButton('Для отримання статусу особи з інвалідністю')
zraz5 = KeyboardButton('Зразки документів')



zraz = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
zraz.add(zraz1, zraz3)
zraz.insert(zraz2)
zraz.insert(zraz5)
zraz.insert(zraz4)
zraz.add(buttonmain)

zrazz1 = KeyboardButton('форма 027/0')
zrazz2 = KeyboardButton('форма 025/о')
zrazz4 = KeyboardButton('форма 088/о')
zrazz5 = KeyboardButton('Заява на отримання протезного виробу')
zrazz6 = KeyboardButton('Довідка про участь у бойових діях')
zrazz7 = KeyboardButton('Довідка про обставини травми')
zrazz8 = KeyboardButton('Витяг з журналу ведення бойових дій')
zrazz3 = KeyboardButton('Назад')
zrazz = ReplyKeyboardMarkup(resize_keyboard=False)
zrazz.add(zrazz1, zrazz2, zrazz4, zrazz5, zrazz6, zrazz7, zrazz8, zrazz3, buttonmain)




#---------------------------Центри протезування в Україні--------------------------------------------------------------------
c1 = KeyboardButton('Superhumans')
c2 = KeyboardButton('Без обмежень')
c3 = KeyboardButton('Незламні')
c4 = KeyboardButton('ВЦРП ЗДОРОВ`Я')
c7 = KeyboardButton('СТЕЦЕНКО. ЦЕНТР ПРОТЕЗУВАННЯ')

c5 = KeyboardButton('БІОСКУЛЬПТОР')
c8 = KeyboardButton('Далі🔜')
c6 = KeyboardButton('Головне меню')
centre = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
centre.add(c1, c2, c3, c4, c5, c7, buttonmain, c8)


cc1 = KeyboardButton('УКРАЇНСЬКИЙ НДІ ПРОТЕЗУВАННЯ, ПРОТЕЗОБУДУВАННЯ І ПОНОВЛЕННЯ ПРАЦЕЗДАТНОСТІ')
cc2 = KeyboardButton('Укр Протез')
cc3 = KeyboardButton('Антис Орто')
cc4 = KeyboardButton('Сміливий крок')
cc5 = KeyboardButton('Чернігівський протезно-ортопедичний цех')
cc6 = KeyboardButton('Опора')
cc7 = KeyboardButton('Ортопедичний Сервіс Центр')
cc8 = KeyboardButton('Протезно-ортопедична майстерня')
cc9 = KeyboardButton('Форвард Орто')
cc10 = KeyboardButton('Вінницьке державне підприємство')
cc11 = KeyboardButton('ТОВ Орто Віта')
cc12 = KeyboardButton('Луцький протезно-ортопедичний цех')
cc13 = KeyboardButton('Орто-Трейд')
cc14 = KeyboardButton('ДНІПРОПЕТРОВСЬКЕ КАЗЕННЕ ЕКСПЕРИМЕНТАЛЬНЕ ПРОТЕЗНО-ОРТОПЕДИЧНЕ ПІДПРИЄМСТВО')
cc15 = KeyboardButton('Аванті трейд')
cc16 = KeyboardButton('ЖИТОМИРСЬКЕ ДЕРЖАВНЕ ЕКСПЕРИМЕНТАЛЬНЕ ПРОТЕЗНО-ОРТОПЕДИЧНЕ ПІДПРИЄМСТВО')
cc17 = KeyboardButton('Арол Плюс')
cc18 = KeyboardButton('ЦЕНТР ПРОТЕЗНО-ОРТОПЕДИЧНОЇ РЕАБІЛІТАЦІЇ ІНВАЛІДІВ ОРТТЕХ')
cc19 = KeyboardButton('Івано-Франківський Протезно-ортопедичний Цех')
cc20 = KeyboardButton('ПП Ортосвіт')
cc21 = KeyboardButton('ТОВАРИСТВО З ОБМЕЖЕНОЮ ВІДПОВІДАЛЬНІСТЮ "ЦЕНТР ПРОТЕЗУВАННЯ "ЕДВАРДС"')
cc22 = KeyboardButton('ТОВ Протолайф')
cc23 = KeyboardButton('Чернівецький протезно-ортопедичний цех')

ccc = KeyboardButton('Інші центри протезування')

centre2 = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
centre2.add(cc1,cc2,cc3,cc4,cc5,ccc,buttonmain)

centre2 = ReplyKeyboardMarkup(resize_keyboard=False, one_time_keyboard=False)
centre2.add(cc22,cc8,cc9, cc13,cc20,buttonmain)
centre2.insert((ccc))



#---------------------------------------Про проєкт----------------------------------------------------------------

p1 = KeyboardButton('Історія створення')
p2 = KeyboardButton('Контактні дані')
p3 = KeyboardButton('Зворотній зв`язок')
pro = ReplyKeyboardMarkup(resize_keyboard=True)
pro.add(p1, p2, buttonmain)


#____________krok2_________________________
k1 = KeyboardButton('На що звернути увагу!')
k2 = KeyboardButton('3 крок')
k3 = KeyboardButton('Попередній крок')
krok2 = ReplyKeyboardMarkup(resize_keyboard=True)
krok2.add(k1, k2, k3, buttonmain)


#_______________poshur zaput________________
zap1= KeyboardButton('ХТО МОЖЕ ОТРИМАТИ ПРОТЕЗ?')
zap2 = KeyboardButton('ПРО ВЗУТТЯ')
zap3 = KeyboardButton('СКІЛЬКИ ПРОТЕЗІВ Я МОЖУ ОТРИМАТИ?')
zap4 = KeyboardButton('ПРО СПОРТ')
zap5 = KeyboardButton('ЧАСТКОВА АМПУТАЦІЯ')
zap6 = KeyboardButton('ЩО ТАКЕ ГРАНИЧНІ ЦІНИ?')
zap7 = KeyboardButton('ЯКЩО ВИНИК ДИСКОМФОРТ')
zap8 = KeyboardButton('➡️')
zap9 = KeyboardButton('⬅️')
zap = ReplyKeyboardMarkup(resize_keyboard=False)
zap.add(zap1, zap2, zap3, zap4, zap5, zap8, buttonmain)

zapp = ReplyKeyboardMarkup(resize_keyboard=False)
zapp.add(zap9,zap6, zap7, buttonmain)