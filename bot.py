
import logging
import markup as mar
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove
import datetime
vremya = datetime.datetime.now()

str_vremya = str(vremya)

API_TOKEN = '6977244775:AAGdIrwEh_dKb9zNkOFKGIJWeeXHCHFhRWc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)






@dp.message_handler(commands=['start'])
async def start_cmd_handler(message: types.Message):
    """
    Обробник команди /start. Ініціалізує запити


    """
#    await bot.send_message(message.from_user.id, 'Вітаємо! Ми готові відповісти на Ваші запитання.')
    await bot.send_message(message.from_user.id, 'Будь ласка, оберіть питання, яке Вас цікавить 👇', reply_markup=mar.sector)

#reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text=='Покрокова інструкція з отримання протезу':
        await bot.send_message(message.from_user.id, 'Відкриваю', reply_markup=mar.pokrokova)
#        await message.reply_document(open('ccc.JPG', 'rb'))
#    elif message.text=='Найпоширеніші запитання':
#        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zaput)
    elif message.text=='Історії побратимів':
        await bot.send_message(message.from_user.id,'В цьому розділі ти можеш почитати історії з життя ветеранів, які вже пройшли свій шлях до отримання протезу і готові поділитися досвідом. Можливо, він для тебе буде корисним', reply_markup=mar.istor)
    elif message.text=='Перелік документів':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zraz)
    elif message.text=='Центри протезування в Україні':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.centre)
    elif message.text=='Про проєкт':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.pro)
    elif message.text=='Головне меню 🔙':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.sector)
    elif message.text=='1 крок':
        await bot.send_message(message.from_user.id,'Збери необхідні документи:\n- паспорт громадянина України, або інший документ, що посвідчує особу;\n- реєстраційний номер облікової картки платника податків;\n- посвідчення (у разі наявності);\n- висновок МСЕК про встановлення інвалідності (якщо інвалідність встановлена);\n- рішення ВЛК чи висновок ЛКК (для УБД, яким не встановлено інвалідність);\n- витяг з наказу командира в/ч або довідку про обставини травми, видану командиром в/ч.')
    elif message.text=='На що звернути увагу':
        await bot.send_message(message.from_user.id,'Якщо тобі пропонують протезування за кордоном, переконайся, що розумієш умови протезування та поцікався, який план подальшого обслуговування протезу. Протягом першого року об’єм кукси змінюється і часто необхідно регулярно підлаштовувати протез. Де б не відбувалось протезування, з`ясуй, як відбуватиметься обслуговування та гарантійний ремонт протеза (https://protezinua.com/)\nВ Урядовому контактному центрі запрацює спеціалізована "гаряча лінія" з питань реабілітації, протезування/ортезування та забезпечення іншими  допоміжними засобами реабілітації військовослужбовців, які отримали поранення \nДля оперативного отримання інформації та консультування можна телефонувати за номером 1545 (в голосовому меню обрати кнопку 4).\nНомер є багатоканальним, телефонувати можна щодня з 8:00 до 20:00\nДзвінки на “гарячу лінію” з мережі  фіксованого  зв’язку Укртелекому та мобільних операторів Київстар, Vodafone Україна, Лайфселл безкоштовні.')
#    elif message.text=='2 крок':
#        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.krok2)
    elif message.text=='2 крок':
        await bot.send_message(message.from_user.id,'Звернись до ЦНАП, або ж УСЗН\n- заповни заяву;\n- ознайомся з переліком підприємств та каталогом засобів реабілітації.\nДо речі ти можеш подати документи онлайн:\n- Єдиний державний веб-портал електронних послуг (https://diia.gov.ua/)\n- Електронний кабінетособи з інвалідністю (https://ek-cbi.msp.gov.ua/)')
    elif message.text=='Попередній крок':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.pokrokova)
    elif message.text=='3 крок':
        await bot.send_message(message.from_user.id,'Дочекайся на повідомлення про надання тобі електронного направлення для отримання протезування')
    elif message.text=='4 крок':
        await bot.send_message(message.from_user.id,'Звернись до підприємства, яке ти обрав\nПодай заяву особисто або онлайн')
    elif message.text=='5 крок':
        await bot.send_message(message.from_user.id,'Отримай свій засіб реабілітації\nОбов`язково ретельно оглянь та приміряй засіб. Отримай настанову щодо експлуатації. Не забудь оформити талон на гарантійний ремонт.')
    elif message.text=='На що звернути увагу!':
        await bot.send_message(message.from_user.id,'Для того, щоб отримати протез за державні кошти, необхідно подати заяву онлайн на первинну реєстрацію в Електронному кабінеті Централізованого банку даних з проблем інвалідності (Далі- ЦБІ) (https://ek-cbi.msp.gov.ua/) та зібрати відповідні документи. Зібрані документи необхідно завантажити в електронному кабінеті ЦБІ.')


    elif message.text=='Superhumans':
        await bot.send_message(message.from_user.id,'https://superhumans.com/patients/')
    elif message.text=='Без обмежень':
        await bot.send_message(message.from_user.id,'https://www.bez-obmezhen.com.ua/')
    elif message.text=='Незламні':
        await bot.send_message(message.from_user.id,'https://unbroken.org.ua/ua')
    elif message.text=='СТЕЦЕНКО. ЦЕНТР ПРОТЕЗУВАННЯ':
        await bot.send_message(message.from_user.id,'https://www.stetsenko.center/')
    elif message.text=='ВЦРП ЗДОРОВ`Я':
        await bot.send_message(message.from_user.id,'https://health-ukraine.com.ua/uk/o-centre/')
    elif message.text=='БІОСКУЛЬПТОР':
        await bot.send_message(message.from_user.id,'http://biosculptor.com.ua/')
    elif message.text=='УКРАЇНСЬКИЙ НДІ ПРОТЕЗУВАННЯ, ПРОТЕЗОБУДУВАННЯ І ПОНОВЛЕННЯ ПРАЦЕЗДАТНОСТІ':
        await bot.send_message(message.from_user.id,'https://protez.eu/')
    elif message.text=='Протезувався в Україні':

        await bot.send_message(message.from_user.id,'Спілкувався з тими хто проходив протезування , але вибрав протезний центр не по відгуках, а по географічному розміщенню мене відносно найближчого представництва. (ветеран Р., 46 років)', reply_markup=mar.istor_ukr)
        await bot.send_message(message.from_user.id,'Особисто в моєму випадку, коли я ще знаходився у відділенні інтенсивної терапії гнійно-сепсисної хірургії в лікарні ім. Мечникова і був вже у більш-менш стабільному стані, до мене підійшов один зі співробітників цієї лікарні, та запитав про те, чи не хотів би я протезуватися за кордоном. Тоді я ще не знав, що в Україні для військовослужбовців передбачене фінансування протезування, тому одразу ж погодився, бо брали за кордон і на продовження лікування і протезування відразу. Чоловік, який цим займався дав свій контакт, взяв мій номер телефона та телефон найближчої людини, або людини, котра супроводжує. І сказав, що зробить все самостійно, мені тільки треба надати форму 100 («картка з надання домедичної допомоги в умовах бойових дій») попередні виписки з лікарень, документ, що підтверджує особу та довідку про обставини травмування. Про форму 100 дізналась моя наречена, коли я ще був у стані коми. Їй про те , що ця довідка має бути виписана військовими медиками сказав мій вітчим, який вже був військовим з 2015 року  і отримував раніше поранення. Усіма питаннями документів займалась наречена, бо я був невзмозі навіть розмовляти, тому цей чоловік з Мечникова далі комунікував з нею. Він їй сказав, що довідка про обставини травмування є найголовнішою у всьому процесі лікування, протезування та у подальшому оформленні інвалідної групи, компенсацій тощо.')
        await bot.send_message(message.from_user.id, 'І повідомив про, те що її треба запросити в медчастині або через свого командира. І командир з начальником медичної служби надіслали мені цю довідку поштою. Доречі, виявилося, що для протезування за кордоном навіть не обов’язковий був закордонний паспорт та звичайний (він у мене, на жаль, тимчасово був відсутній), бо я переживав через це. Ну от ми надали всі документи цьому чоловіку, а він надіслав все до МОЗ України. І сказав, що мені мають подзвонити з МОЗ тоді, коли мене обере якась із закордонних клінік. Коли це буде... він сказав просто чекати. Моєму сусіду по палаті передзвонили через два тижні і наступного дня він вже поїхав за кордон. А я так і не дочекався. Мене перевели в військовий шпиталь до Львова по вул. Личаківська. Там жахливе ставлення саме лікарів до пацієнтів. Мене запитали чи записувався я на протезування за кордоном, я розказав як було. У відповідь мовчання, ніякої інформації чи мене ще візьмуть, чи мені доведеться збирати гроші, чи взагалі про те що в Україні є можливість безкоштовного протезування, інформації нуль, навіть якщо запитувати — повне ігнорування або вони просто й самі не знають. Потім мене перевели до Трускавецького військового шпиталю. Там у мене також запитали, чи записувався я на протезування за кордоном. Згодом, до мого лікаря завітали представники одної з протезних фірм України та залишили свої рекламки, ')
        await bot.send_message(message.from_user.id,'а лікар передав їх мені. І в цей момент я дізнався, що є державна програма безкоштовного протезування, і що коштів виділяється вдвічі більше, ніж на цивільних, тому якщо натрапити на фірму з кваліфікованими спеціалістами, то можна зробити достатньо гарний протез. Мій лікар зовсім не мав подальшої інформації, що мені робити, тому дав телефон протезиста, який приходив. Не знаючи, що я маю право вибрати протезний центр з багатьох, які є в Україні, я одразу зібрався протезуватися у цього першого який трапив на шляху. Але він сказав, що як все заживе, щоб я йому подзвонив. Але я від нього очікував хоч якоїсь інформації про сам процес протезування, види протезів, як вони робляться, які бувають ступні, з яких матеріалів це все робиться, який час потрібен на протезування. Він сказав тільки те, що в Україні це безкоштовно і що я не маю знати як це робиться, а протезист сам все вирішить, бо я не компетентний. Потім мене перевели до філії Винницького шпиталю в Трускавецькій міській лікарні. Там усі пацієнти були з якимись видами ампутації і вже від них я дізнався всю інформацію про протезування, перелік документів і все, що стосувалося цього питання. І поступово почав дізнаватися інформацію, якої не вистачало, у медичного персоналу. Оформлення електронного направлення на протезування зайняло в мене приблизно три місяці замість кількох днів.')
        await bot.send_message(message.from_user.id,'  Тут проблема була в тому, що довідку військово-лікарської комісії довелося перероблювати тричі, бо у Винниках непраильно писали код хвороби. Після передачі довідки в соцзахист, якщо вона виявлялась неправильною, доводилось запрошувати нову і так декілька разів. Зараз така проблема — рідкість, вже вміють робити одразу правильно. Але зі мною було отак. Було б добре, якби був якийсь ресурс електронний, де були б зібрані всі-всі зразки необхідних документів. (ветеран К., 21 рік)')

    elif message.text=='Попереднє меню↩️':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.istor)

    elif message.text=='Протезувався за кордоном':
        await bot.send_message(message.from_user.id, 'Особисто я їздив протезуватися в Америку, бо поки що я не довіряю українським протезувальникам. Мають пройти роки, поки вони навчаться робити нормальні функціональні протези. Плюс, я ще й там був повністю безкоштовно на реабілітації. А тут, в Україні, мені б поставили протез і відправили додому самостійно вчитися на ньому ходити і пристосовуватися до нового життя. (ветеран Т., 32 роки)', reply_markup=mar.istor_kord)
        await bot.send_message(message.from_user.id, 'Я довірився відгукам хлопців, які вже отримували протез там, в США. Про українські протезувальні компанії я навіть не цікавився.  Я заповнив заявку і зі мною вже вийшли на зв’язок, попросили вислати всі документи і чекати, поки загоїться культя. (ветеран М., 27 років)')
        await bot.send_message(message.from_user.id, 'В мене ампутація руки і з цим взагалі дуже туго в Україні. Майже вся увага сконцентрована на протезування ніг: бо це простіше і таким ампутацій більше. За виготовлення протезу для мене поки що не взялась жодна протезувальна компанія в Україні. Поки що я розгублений, не знаю, може, їхати за кордон доведеться. (ветеран В., 28 років)')
    elif message.text=='Як можуть обманути?':
        await bot.send_message(message.from_user.id, 'Перша компанія, з якою  я стикнувся, зовсім не надала інформації. «Ваша справа обрати нас, а все інше ви не маєте знати, бо ви не протезист, я сам все зроблю, ви виконуйте мої вказівки», — сказав протезист цієї компаній коли я почав задавати «зайві» питання.\nДруга без погодження зі мною використовувала моє електронне направлення, писала від мого імені заяву на потребу протезування саме в їхній компанії, і це все було без мого відома. Таким чином, я ледь не лишився можливості протезування на два роки, бо коли через ці махінації я хотів обрати іншу компанію, вони говорили, що пустили електронне направлення в хід і воно вже використане, а наступне буде доступне тільки через два роки, але виявилось, що якщо в мене в момент між поданням заяви про намір протезування та безпосередньо отриманням протеза була операція, то від них можна відмовитися законним шляхом і не втратити можливість протезування в іншій компанії (з цим нам допомогли співробітники УСЗН)./nЗ третьою фірмою все добре. Дають на вибір ступню, скидають посилання на відеоогляди ступні, розказують, що і в якому випадку підходить саме мені ввічливі, навіть, кавою пригощають кожного разу. Тому уважно подумай і кілька разів все перевір перед тим, як підписувати будь-які документи. (ветеран К., 21 рік)')
        await bot.send_message(message.from_user.id, 'В нашому місцевому добропільському УСЗНі (це Донецька область) взагалі нічого не знали про процес протезування. Ми прийшли до них, а вони прям так прямим текстом і сказали, що нічого не знають, будуть розбиратись. Більше того, вони ще й дезінформували нас: сказали, що вони співпрацюють тільки з протезувальною компанією з Тернополя і замовити протез чоловік може тільки там і ніде більше. Ми сильно в тому питанні не розбирались. Раз сказали, що можна тільки там, то ми й замовили там, але це дуже незручно: їздити з Донецької області в Тернопіль, щоб щось підлаштувати в  протезі, а підлаштовувати треба постійно, бо культя то всихається, то набрякає. Коли проконсультувались з юристом, з`ясували, що ми маємо прави обрати будь-яку компанію з 58-ми, які є на сайті Мінсоцполітики, а не тільки ту, яку вказав УСЗН. (В., дружина пораненого ветерана)')
#        await bot.send_message(message.from_user.id, 'Для того, щоб не потрапити на гачок шахраїв, яких багато навіть у такий важкий час, необхідно бути дуже пильними і ретельно перевіряти всю інформацію – від оголошень про продаж товарів чи послуг до посилань на сайти. Звісно, в критичні моменти холодний розум може відмовляти, тому важливо не вестися на емоції і все ж витратити трохи часу на перевірку інформації. Отримувати її слід лише з офіційних джерел. Якщо, наприклад, пропонують отримати якісь виплати, то варто перевірити на офіційному сайті установи, яка відповідальна за такі виплати, усю можливу інформацію: яким чином кошти надходять і чи є взагалі такі види допомоги. Війна для всіх важкий та страшний період. Неуважність може зіграти комусь на руку, а вас наразити на небезпеку. Саме зараз треба бути максимально обачними, щоб не втратити кошти, які в майбутньому можуть вам знадобитись. Якщо хочете пожертвувати ЗСУ — обирайте вже перевірені вами фонди, які від 24 лютого працюють на благо України.')

    elif message.text =='Ще історії':
        await bot.send_message(message.from_user.id,'З точки зору оформлення документів у мене було все добре, проблеми є тільки з медичного боку. Поки я носив учбовий протез, в мене вилізли невроми і довелося робити додаткову операцію. Мене про це попереджали. Зараз я роблю операцію і вже тільки згодом я отримаю постійний протез. (ветеран М., 31 рік)', reply_markup=mar.istor_ukr3)
        await bot.send_message(message.from_user.id,'Я для себе обрав протезування в Україні, бо треба бути вдома. Знайшов фірму, яка має філіал недалеко від мене. Бо протез — то діло таке, його не вдягнеш один раз і назавжди. Потрібно постійно їздити до протезиста на обслуговування: щось підкрутити, щось підтягнути, бо культя з часом всихається і протез починає бовтатися. (ветеран Д., 22 роки)')
        await bot.send_message(message.from_user.id,'Я обирав таку протезувальну компанію, щоб вони були недалеко від мене. Ту, яку я вибрав, в 250 км від мене. Плюс, та компанія, яку я вибрав, має стаціонар. Вони кладуть і вони цілодобово поруч. Це ПП «Орсосервіс» у Вінниці. (ветеран А., 45 років)')
        await bot.send_message(message.from_user.id,'Я би не радив отримувати протез людині там, де вона лікується, вже краще отримати, коли повернеться додому. Я, наприклад, протезувався в Києві, хоча сам живу у Львові. Я отримував протез ще у 2014-му, тоді особливого вибору не було. Зараз я би хотів перевестись на обслуговування до львівських протезистів, щоб не їздити щоразу аж до Києва. (ветеран С. 32 роки)')
    elif message.text =='Ще  історії':
        await bot.send_message(message.from_user.id,'Далі буде...')



    elif message.text=='Найпоширеніші запитання':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zap)
    elif message.text =='➡️':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zapp)
    elif message.text =='⬅️':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zap)
    elif message.text =='ХТО МОЖЕ ОТРИМАТИ ПРОТЕЗ?':
        await bot.send_message(message.from_user.id,'"Отримати протез може будь-яка людина, яка цього потребує. За рахунок бюджетних коштів протези можуть отримати:\n\n- особи з інвалідністю (діти та дорослі) відповідно програми індивідуальної реабілітації;\nучасники АТО/ОС на підставі висновків військово-лікарських комісій;\n- ветерани військової служби, органів внутрішніх справ, державної пожежної охорони;\n- мирне населення, що проживало в районі проведення АТО/ОС, якщо вони не вчиняли кримінальних правопорушень на підставі висновків лікарсько-консультативних комісій лікувально-профілактичних закладів;\n- особи похилого віку."')
    elif message.text =='ПРО ВЗУТТЯ':
        await bot.send_message(message.from_user.id,'ЧИ МОЖУ Я ЗМІНЮВАТИ ВЗУТТЯ СЕЗОННО НА ПРОТЕЗІ?\nВи маєте одразу визначитися, яке взуття хочете носити. Від цього залежить як буде зроблена стопа й яку силу амортизації протез має витримувати. Якщо ви хочете сезонно змінювати взуття, про це варто одразу сказати протезисту й разом із ним його підібрати. Від цього залежить, яка модель стопи буде в вашому протезі.')
    elif message.text =='СКІЛЬКИ ПРОТЕЗІВ Я МОЖУ ОТРИМАТИ?':
        await bot.send_message(message.from_user.id,'Чи можеш ти отримати протез від держави, якщо вже отримав протез в волонтерській організації, або навпаки? Так, можеш отримати і там, і там, адже чинне законодавство України не містить подібних обмежень.')
    elif message.text =='ПРО СПОРТ':
        await bot.send_message(message.from_user.id,'Я МОЖУ ЗАЙМАТИСЯ СПОРТОМ НА ПРОТЕЗІ?\nДля того, щоб займатися спортом, треба мати спеціальний протез. Такі протези складаються зі спеціальних протишокових, протиударних вузлів й пристосовані до потреб того чи іншого виду спорту. Для занять фізкультурою можна використовувати протези 3-4 рівня функціональності.')
    elif message.text =='ЧАСТКОВА АМПУТАЦІЯ':
        await bot.send_message(message.from_user.id,'ЯКЩО В МЕНЕ ЧАСТКОВА АМПУТАЦІЯ, Я МОЖУ ОТРИМАТИ ПРОТЕЗ?\nЯкщо в людини часткова ампутація руки чи ноги, вона може отримати протези. Проте варто зважати на рівень ампутації та інші особливості. Протез не можна зробити, якщо залишкова частина занадто мала для кріплення чи має невиправні дефекти (наприклад, велика рубцьованість, уламки, які неможна вийняти).')
    elif message.text == 'ЩО ТАКЕ ГРАНИЧНІ ЦІНИ?':
        await bot.send_message(message.from_user.id, 'Протези оплачує держава в межах граничних цін. Вони встановлені наказами міністерства соціальної політики. Граничні суми складаються з вартості комплектуючих для протеза, оплати праці протезиста та послуг протезного підприємства. ')
    elif message.text == 'ЯКЩО ВИНИК ДИСКОМФОРТ':
        await bot.send_message(message.from_user.id, 'ЯКЩО Я ПОЧАВ ВІДЧУВАТИ ДИСКОМФОРТ ПІД ЧАС НОСІННЯ ПРОТЕЗА, ЩО РОБИТИ?\nНеобхідно звернутися до протезиста. Він повинен визначити причину дискомфорту. Якщо вона в протезі чи, наприклад, кукса зменшила свій об’єм, протезист повинен налагодити механізм чи запропонувати варіанти вирішення проблеми. Протезист може виконати корекцію протеза чи виконати ремонт.')
    elif message.text=='Для  проходження МСЕК':
        await bot.send_message(message.from_user.id,'- Направлення на МСЕК (форма ф. № 088/о);\n- паспорт або ID картка з витягом з Єдиного державного демографічного реєстру щодо реєстрації місця проживання;\n- копія ідентифікаційного коду;\n- військовий квиток або посвідчення офіцера (копія);\n- військово-облікові документи або їхні копії;\n- свідоцтво про хворобу або довідка ВЛК;\n- медична документація, оригінали (форми 025/о,027/о) та амбулаторна картка хворого;\n- у випадку, якщо ти є учасником ліквідації наслідків аварії на Чорнобильській АЕС (або особою, яка потерпіла від Чорнобильської катастрофи, чи постраждала від радіоактивного опромінення внаслідок будь-якої аварії) - відповідні підтверджуючі документи;\n- копія витягу з наказу командира військової частини про виключення зі списків особового складу частини / звільнення з військової служби (за наявності);\n- довідка про обставини травми (за потреби);\n- посвідчення УБД (за наявності);\n- копія трудової книжки (за наявності).\nПри проходженні МСЕК потрібно мати з собою оригінали зазначених документів.')
    elif message.text=='Для протезування':
        await bot.send_message(message.from_user.id,'- заява на забезпечення протезним виробом (Додаток 14);\n- копія паспорта громадянина України;\n- копія ідентифікаційного коду;\n- рішення ВЛК про необхідність забезпечення протезним виробом;\n- витяг з наказу командира в/ч або довідка про обставини травми;\n- копія довідки про безпосередню участь в бойових діях.')
    elif message.text=='Назад':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zraz)
    elif message.text=='Для отримання статусу УБД':
        await bot.send_message(message.from_user.id,'- довідка про безпосередню участь особи в заходах, необхідних для забезпечення оборони України, захисту безпеки населення та інтересів держави у зв’язку з військовою агресією російської федерації проти України;\n- не менш як один з таких документів:\n- витяги (копії) бойових донесень;\n- витяги (копії) з журналів бойових дій (оперативних завдань, ведення оперативної обстановки);\n- витяги (копії) з вахтових журналів;\n- копії польотних листів;\n- копії матеріалів спеціальних (службових) розслідувань за фактами отримання поранень, контузій, каліцтв.')
    elif message.text=='Для отримання статусу особи з інвалідністю':
        await bot.send_message(message.from_user.id,'- довідка командира військової частини про причини та обставини поранення;\n- довідка військово-лікарської комісії (ВЛК);\n- довідка медико-соціальної експертної комісії (МСЕК);\n- витяг із наказу командира військової частини про виключення зі списків особового складу частини.')
    elif message.text=='Перелік':
        await bot.send_message(message.from_user.id,'- заява на забезпечення протезним виробом (Додаток 14);\n- копія паспорта громадянина України;\n- копія ідентифікаційного коду;А\n- витяг з наказу командира в/ч або довідка про обставини травми;\n- копія довідки про безпосередню участь в бойових діях.')
    elif message.text=='Додаток 14':
        await bot.send_message(message.from_user.id,'https://turbota.mil.gov.ua/wp-content/uploads/2023/04/dodatok-14.-zayava-na-otrymannya-proteznogo-vyrobu.doc')
    elif message.text=='Історія створення':
        await bot.send_message(message.from_user.id,'Цей чатбот створений в рамках ініціативи «Як діяти, коли потрібен протез: створення дорожньої карти для ветеранів та колишніх військових», що впроваджується ГО «Ініціативний центр «Толока» за сприяння Програми розвитку ООН (ПРООН) в Україні за фінансової підтримки Європейського Союзу, наданої в межах проєкту «EU4Recovery – Розширення можливостей громад в Україні».\nЯкщо ти маєш ідеї для покращення цього чатботу, будь ласка, звертайся до нас або через сторінку організації на Фейсбуці https://www.facebook.com/ictoloka , або за телефоном +380668924833 (Viber, Telegram, Watsapp)')

    elif message.text=='Зразки документів':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.zrazz)


    elif message.text=='форма 027/0':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')
    elif message.text=='форма 025/о':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')
    elif message.text=='форма 088/о':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')
    elif message.text=='Заява на отримання протезного виробу':
        await bot.send_message(message.from_user.id,'https://docs.google.com/document/d/1B98YsUxu1vITI3VVZjowGLGcZogCWiur/edit')
    elif message.text=='Витяг з журналу ведення бойових дій':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')
    elif message.text=='Довідка про участь у бойових діях':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')
    elif message.text=='Довідка про обставини травми':
        await bot.send_message(message.from_user.id,'https://drive.google.com/drive/folders/1ghgSz1IRwPtZILVug-miEy9M9-THv86r')


    elif message.text=='Далі🔜':
        await bot.send_message(message.from_user.id,'Відкриваю', reply_markup=mar.centre2)

    elif message.text=='Інші центри протезування':
        await bot.send_message(message.from_user.id,'https://www.msp.gov.ua/content/zabezpechennya-tehnichnimi-ta-inshimi-zasobami-reabilitacii-specavtotransportom.html')
    elif message.text=='ТОВ Протолайф':
        await bot.send_message(message.from_user.id,'https://protolife.com.ua/')
    elif message.text=='Протезно-ортопедична майстерня':
        await bot.send_message(message.from_user.id,'https://protezmaster.com/#!/')
    elif message.text=='Форвард Орто':
        await bot.send_message(message.from_user.id,'https://forward-orto.com.ua/')
    elif message.text=='Орто-Трейд':
        await bot.send_message(message.from_user.id,'https://ortotrade.com.ua/')
    elif message.text=='ПП Ортосвіт':
        await bot.send_message(message.from_user.id,'"067 231 5147\nortosvit@i.ua"')












    elif message.text=='Контактні дані':
        await bot.send_message(message.from_user.id,'ГРОМАДСЬКА ОРГАНІЗАЦІЯ "ІНІЦІАТИВНИЙ ЦЕНТР  "ТОЛОКА" зареєстрована відповідно до  законодавства України з кодом ЄДРПОУ  40592337 з місцезнаходженням, що  розташоване за адресою 85310, Україна, \nДонецька область, м. Покровськ, вул.  Островського, буд.8\nТел: +38 066 892 48 33 \nЕлектронна пошта: \nt.moiseeva.shilenko@gmail.com')


    else: await  bot.send_message(message.from_user.id,'Нажаль я розумію тільки кнопки')









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)