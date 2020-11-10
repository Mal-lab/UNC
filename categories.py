class Categories():
    def __init__(self):
        self.data = {'1. РУ 6-750 кВ': ['Таблица В1. УНЦ ячейки выключателя НУ 110 - 750 кВ (тыс. руб.)',
                                   'Таблица В2. УНЦ ячейки выключателя НУ 6 - 35 кВ (тыс. руб.)',
                                   'Таблица В3. УНЦ ячейки выключателя КРУ 6 - 35 кВ (тыс. руб.)',
                                   'Таблица В4. УНЦ ячейки выключателя ВУ 110 - 500 кВ с учетом здания ЗРУ (тыс. руб.)',
                                   'Таблица В5. УНЦ ячейки выключателя ВУ 110 - 500 кВ без учета здания ЗРУ (тыс. руб.)'],
                   '2. Объекты электросетевого хозяйства с использованием управляемых элементов сети  (автоматического пункта секционирования (реклоузера) 6 - 35 кВ, выключателя 6 - 750 кВ)':
                                    ['Таблица В6. УНЦ автоматического пункта секционирования (реклоузера) 6 - 35 кВ без ПКУ (тыс. руб.)',
                                     'Таблица В7. УНЦ автоматического пункта секционирования (реклоузера) 6 - 35 кВ с ПКУ и интеграцией в АСУТП (тыс. руб.)',
                                     'Таблица Д3. УНЦ ШПС (тыс. руб.)'],
                   '3. Ячейка трансформатора, регулировочного трансформатора, ячейка реактора ТОР (ДГР) 6 - 750 кВ':
                                    ['Таблица Т1. УНЦ ячейки трансформатора 110 - 500 кВ (тыс. руб.)',
                                     'Таблица Т2. УНЦ ячейки трансформатора 150 - 500 кВ (тыс. руб.)',
                                     'Таблица Т3. УНЦ ячейки трансформатора 330 - 750 кВ (тыс. руб.)',
                                     'Таблица Т4. УНЦ ячейки трансформатора 35 - 500 кВ (тыс. руб.)',
                                     'Таблица Т5. УНЦ ячейки трансформатора 6 - 35 кВ (тыс. руб.)',
                                     'Таблица Т6. УНЦ регулировочного трансформатора 6 - 35 кВ (тыс. руб.)',
                                     'Таблица Т7. УНЦ регулировочного трансформатора 6 - 220 кВ (тыс. руб.)',
                                     'Таблица Р1. УНЦ ячейки реактора ДГР 6 - 35 кВ (тыс. руб.)',
                                     'Таблица Р2. УНЦ ячейки реактора ТОР 6 - 35 кВ (тыс. руб.)',
                                     'Таблица Р3. УНЦ ячейки реактора ТОР 110 - 330 кВ (тыс. руб.)'],
                   '4. КРМ 6 - 750 кВ':
                                    ['Таблица Р4. УНЦ КРМ 110 - 750 кВ (тыс. руб.)',
                                     'Таблица Р5. УНЦ КРМ 6 - 35 кВ (тыс. руб.)'],
                   '5. КТП (РП, РТП, СП), ячейки выключателя РП (СП, ТП, РТП) 6 - 20 кВ':
                                    ['Таблица Э1. УНЦ КТП киоскового типа 6 - 20 кВ (тыс. руб.)',
                                     'Таблица Э2. УНЦ КТП мачтового (шкафного, столбового) типа с одним трансформатором 6 - 20 кВ(тыс. руб.)',
                                     'Таблица Э3. УНЦ КТП блочного типа (бетонные, сэндвич-панели) 6 - 20 кВ (тыс. руб.)',
                                     'Таблица Э4. УНЦ здания РП (СП, РТП, ТП) блочного типа 6 - 20 кВ (тыс. руб.)',
                                     'Таблица В8. УНЦ ячейки выключателя РП (СП, ТП, РТП) 6 - 20 кВ (тыс. руб.)'],
                   '6. Подготовка и устройство территории ПС (ЗПС) 35 - 750 кВ':
                                    ['Таблица Б1. УНЦ подготовки и устройства территории ПС (ЗПС) (тыс. руб.)',
                                     'Таблица С1. Площадь подготовки и устройства территории под элементы ПС (ЗПС) (м2)'],
                   '7. Система учета электрической энергии (мощности), АИИС КУЭ, ПКУ, технический учет электроэнергии':
                                    ['Таблица А1. УНЦ ИИК (тыс. руб.)',
                                     'Таблица А2. УНЦ ИВКЭ (тыс. руб.)'],
                   '8. АСУТП ПС и ТМ':
                                    ['Таблица А3. УНЦ АСУТП ПС и ТМ (тыс. руб.)',
                                     'Таблица А4. УНЦ АСУТП присоединения (тыс. руб.)',
                                     'Таблица А5. УНЦ систем АСУТП и ТМ (тыс. руб.)'],
                   '9. Системы связи, УПАСК, ПА':
                                    ['Таблица А6. УНЦ системы ВЧ связи 35 - 750 кВ (тыс. руб.)',
                                     'Таблица А7. УНЦ ВОСП (тыс. руб.)',
                                     'Таблица А8. УНЦ систем ПА, УПАСК (тыс. руб.)'],
                   '10. ПС 35 - 750 кВ':
                                    ['Таблица З1. УНЦ постоянной части ПС (тыс. руб.)',
                                     'Таблица З2. УНЦ постоянной части ЗПС (тыс. руб.)',
                                     'Таблица З3. УНЦ зданий ОПУ, РЩ (тыс. руб.)',
                                     'Таблица З4. УНЦ зданий ЗРУ, ЗПС, ОПУ, РЩ, РПБ (тыс. руб.)',
                                     'Таблица З5. УНЦ зданий ЗРУ, ЗПС (тыс. руб.)',
                                     'Таблица З6. УНЦ здания РПБ (тыс. руб.)'],
                   '11. Ячейка выключателя и элементы ПС':
                                    ['Таблица И1. УНЦ выключателя 110 - 750 кВ с устройством фундаментов (тыс. руб.)',
                                     'Таблица И2. УНЦ выключателя 35 кВ с устройством фундаментов (тыс. руб.)',
                                     'Таблица И3. УНЦ бакового выключателя 110 - 500 кВ с устройством фундаментов (тыс. руб.)',
                                     'Таблица И4. УНЦ бакового выключателя 35 кВ с устройством фундаментов (тыс. руб.)',
                                     'Таблица И5. УНЦ элементов ПС с устройством фундаментов (тыс. руб.)',
                                     'Таблица И6. УНЦ выключателя 110 - 750 кВ без устройства фундаментов (тыс. руб.)',
                                     'Таблица И7. УНЦ выключателя 35 кВ без устройства фундаментов (тыс. руб.)',
                                     'Таблица И8. УНЦ бакового выключателя 110 - 500 кВ без устройства фундаментов (тыс. руб.)',
                                     'Таблица И9. УНЦ бакового выключателя 35 кВ без устройства фундаментов (тыс. руб.)',
                                     'Таблица И10. УНЦ элементов ПС без устройства фундаментов (тыс. руб.)',
                                     'Таблица М3. УНЦ на внутриплощадочные дороги ПС и проезды (тыс. руб.)',
                                     'Таблица Д2. УНЦ системы диагностики и мониторинга оборудования ПС (тыс. руб.)'],
                   '12. РЗА, система оперативного постоянного тока и собственных нужд ПС, сети связи':
                                    ['Таблица И11. УНЦ РЗА (тыс. руб.)',
                                     'Таблица И12. УНЦ РЗА и прочие шкафы (панели) (тыс. руб.)',
                                     'Таблица И13. УНЦ системы оперативного постоянного тока и собственных нужд ПС (тыс. руб.)',
                                     'Таблица Н3. УНЦ контрольного (силового) кабеля (тыс. руб.)',
                                     'Таблица И14. УНЦ сети связи (тыс. руб.)'],
                   '13. Комплекс систем безопасности ПС':
                                    ['Таблица У3. УНЦ защитных конструкций ПС (тыс. руб.)',
                                     'Таблица У4. УНЦ защитных ограждений ПС (тыс. руб.)',
                                     'Таблица З7. УНЦ здания КПП (тыс. руб.)',
                                     'Таблица И15. УНЦ комплекса систем безопасности ПС (тыс. руб.)'],
                   '14. КЛ 0,4 - 500 кВ':
                                    ['Таблица К1. УНЦ КЛ 6 - 500 кВ (с алюминиевой жилой) (тыс. руб.)',
                                     'Таблица К2. УНЦ КЛ 6 - 500 кВ (с медной жилой) (тыс. руб.)',
                                     'Таблица К3. УНЦ КЛ 0,4 кВ (тыс. руб.)',
                                     'Таблица К4. УНЦ КЛ 110 - 500 кВ с системой термомониторинга (тыс. руб.)',
                                     'Таблица Д1. УНЦ системы диагностики и мониторинга КЛ (тыс. руб.)'],
                   '15. Подготовка и устройство территории при прокладке кабельной линии':
                                    ['Таблица Б2. УНЦ на устройство траншеи КЛ и восстановление благоустройства по трассе (тыс. руб.)',
                                     'Таблица Б3. УНЦ на устройство траншеи ВОК и восстановление благоустройства по трассе (для всех субъектов Российской Федерации) (тыс. руб.)',
                                     'Таблица Б4. УНЦ на восстановление дорожного покрытия при прокладке кабельной линии (для всех субъектов Российской Федерации) (тыс. руб.)'],
                   '16. Кабельные сооружения и устройство переходов при прокладке кабельной линии':
                                    ['Таблица Н1. УНЦ выполнения специального перехода кабельной линии методом ГНБ (тыс. руб.)',
                                     'Таблица Н2. УНЦ кабельных сооружений для прокладки кабельной линии (тыс. руб.)',
                                     'Таблица Н4. УНЦ кабельного сооружения с трубами (тыс. руб.)',
                                     'Таблица Н5. УНЦ кабельного колодца (тыс. руб.)',
                                     'Таблица К5. УНЦ на установку страховочных пакетов при прокладке КЛ 6 - 500 кВ (тыс. руб.)',
                                     'Таблица К6. УНЦ токопровода 6 - 35 кВ с литой изоляцией (тыс. руб.)'],
                   '17. Подводная прокладка КЛ 6 - 500 кВ':
                                    ['Таблица Ф1. УНЦ подводной прокладки КЛ 6 - 500 кВ (тыс. руб.)'],
                   '18. ВЛ 0,4 - 750 кВ':
                                    ['Таблица Л1. УНЦ ВЛ 0,4 - 750 кВ на строительно-монтажные работы без опор и провода (тыс. руб.)',
                                     'Таблица Л2. УНЦ ВЛ 0,4 - 750 кВ на строительно-монтажные работы без опор и провода (тыс. руб.)',
                                     'Таблица Л3. УНЦ опор ВЛ 0,4 - 750 кВ (тыс. руб.)',
                                     'Таблица Л4. УНЦ опор ВЛ 0,4 - 750 кВ (тыс. руб.)',
                                     'Таблица Л5. УНЦ провода ВЛ 0,4 - 750 кВ сталеалюминиевого типа (тыс. руб.)',
                                     'Таблица С2. Рекомендуемое количество проводов в фазе',
                                     'Таблица Л6. УНЦ грозотроса ВЛ (тыс. руб.)',
                                     'Таблица Л7. УНЦ провода СИП ВЛ 0,4 - 35 кВ (тыс. руб.)',
                                     'Таблица Л8. УНЦ провода ВЛ повышенной пропускной способности (тыс. руб.)',
                                     'Таблица Л9. УНЦ устройства лежневых дорог (тыс. руб.)',
                                     'Таблица Л10. УНЦ гирлянды изоляторов ВЛ (тыс. руб.)',
                                     'Таблица Л11. УНЦ арматуры, крепления, защиты от перенапряжений ВЛ 0,4 - 35 кВ (тыс. руб.)',
                                     'Таблица М1. УНЦ на устройство защиты опор ВЛ (тыс. руб.)',
                                     'Таблица М2. УНЦ на демонтаж ВЛ 0,4 - 750 кВ (тыс. руб.)',
                                     'Таблица Б7. УНЦ на вырубку (расширение, расчистку) просеки ВЛ (для всех субъектов Российской Федерации) (тыс. руб.)',
                                     'Таблица М4. УНЦ на трелевку хлыстов древесины при вырубке (расширении) просеки ВЛ (тыс. руб.)'],
                   '19. Переход ВЛ (переходной пункт ВЛ-КЛ)':
                                    ['Таблица Ж1. УНЦ переходных пунктов ВЛ-КЛ (тыс. руб.)',
                                     'Таблица Ж2. УНЦ больших переходов ВЛ (тыс. руб.)',
                                     'Таблица Ж3. УНЦ переустройства магистрального газопровода при переходе ВЛ (тыс. руб.)',
                                     'Таблица Ж4. УНЦ переустройства магистрального нефтепровода при переходе ВЛ (тыс. руб.)'],
                   '20. ВОЛС':
                                    ['Таблица О1. УНЦ ОКГТ (тыс. руб.)',
                                     'Таблица О2. УНЦ ОКСН (тыс. руб.)',
                                     'Таблица О3. УНЦ ВОК (тыс. руб.)',
                                     'Таблица О4. УНЦ ВОК в трубе в земле (тыс. руб.)'],
                   '21. УПГ':
                                    ['Таблица У1. УНЦ УПГ (тыс. руб.)',
                                     'Таблица Б5. Затраты на очистку участков местности от взрывоопасных предметов при строительстве ПС (ЗПС) (для всех субъектов Российской Федерации) (тыс. руб.)'],
                   '22. ДГУ':
                                    ['УНЦ ДГУ (тыс. руб.)'],
                   '23. Проектно-изыскательские работы (для всех субъектов Российской Федерации)':
                                    ['Таблица П1. Затраты на проектно-изыскательские работы для ПС (ЗПС) (тыс. руб.)',
                                     'Таблица П2. Затраты на проектно-изыскательские работы для элементов ПС (ЗПС) (тыс. руб.)',
                                     'Таблица П3. Затраты на проектно-изыскательские работы по ВЛ (тыс. руб.)',
                                     'Таблица П4. Затраты на проектно-изыскательские работы для больших переходов ВЛ (тыс. руб.)',
                                     'Таблица П5. Затраты на проектно-изыскательские работы по КЛ (тыс. руб.)',
                                     'Таблица П6. Затраты на проектно-изыскательские работы для отдельных элементов электрических сетей (тыс. руб.)',
                                     'Таблица П7. УНЦ на работы по инженерно-археологическим изысканиям (тыс. руб.)'],
                   '24. Разработка землеустроительной документации и оформление земельных отношений':
                                    ['Затраты на разработку и утверждение ДПТ при прохождении ВЛ по землям лесного фонда (землям, покрытым лесом) (тыс. руб.)',
                                     'Таблица П9. Затраты на разработку и утверждение ДПТ ВЛ (КЛ) по границам земельного участка (тыс. руб.)',
                                     'Таблица П10. Затраты на кадастровые работы ВЛ (КЛ) и работы по установлению земельных отношений (тыс. руб.)',
                                     'Таблица П11. Затраты на кадастровые работы ПС (ЗПС) и работы по установлению земельных отношений (тыс. руб.)']

                   }
        self.tables = {'1. РУ 6-750 кВ': [['1. РУ 6-750 кВ']],
        'Таблица В1. УНЦ ячейки выключателя НУ 110 - 750 кВ (тыс. руб.)': [
            ['Номер расценок', 'Напряжение, кВ', 'Номинальный ток, А', ' Нормативы цены', '-', '-'],
            ['-', '-', '-', '1', '2', '3'],
            ['-', '-', '-', 'Номинальный ток отключения, кА', '-', '-', ],
            ['-', '-', '-', '40', '50', '63'],
            ['В1-01 - 1..3 ', '110', '2500', '23135', '23135', '23135'],
            ['В1-02 - 1..3 ', '110', '3150', '23135', '24703', '25280'],
            ['В1-03 - 1..3 ', '220 (150) ', 'вне зависимости ', '63338', '70883', '74557'],
            ['В1-04 - 1..3 ', '330', '3150', '106581', '109163', '112837'],
            ['В1-05 - 1..3 ', '330', '4000', '106665', '110388', '114062'],
            ['В1-06 - 1..3 ', '500', '3150', '130589', '130589', '133381'],
            ['В1-07 - 1..3 ', '500', '4000', '131814', '131814', '134189'],
            ['В1-08 - 1..3 ', '750', '3150', '198157', '198157', '201831'],
            ['В1-09 - 1..3 ', '750', '4000', '200606', '200606', '204280']],
       'Таблица В2. УНЦ ячейки выключателя НУ 6 - 35 кВ (тыс. руб.)':
            [['Номер расценок', 'Напряжение, кВ', 'Номинальный ток, А', ' Нормативы цены', '-'],
             ['-', '-', '-', '1', '2'],
             ['-', '-', '-', 'Номинальный ток отключения, кА', '-'],
             ['-', '-', '-', '25', '31,5'],
             ['В2-01 - 1...2 ', '6-15', '630', '2486', '2486'],
             ['В2-02 - 1..2 ', '6-15', '800 (1000, 1250)', '2619', '2619'],
             ['В2-03 - 1..2 ', '6-15', '1600', '2768', '2768'],
             ['В2-04 - 1..2 ', '6-15', '2000', '3462', '3462'],
             ['В2-05 - 1..2 ', '35 (20) ', '2000', '9040', '10792'],
             ['В2-06 - 1..2 ', '35 (20) ', '2500', '10792', '10792']],
        'Таблица В3. УНЦ ячейки выключателя КРУ 6 - 35 кВ (тыс. руб.)':
            [['Номер расценок', 'Напряжение, кВ', 'Номинальный ток, А', ' Нормативы цены', '-', '-', '-', '-'],
             ['-', '-', '-', '1', '2', '3', '4', '5'],
             ['-', '-', '-', 'Номинальный ток отключения, кА', '-', '-', '-', '-'],
             ['-', '-', '-', '20', '25', '31,5', '40', '50'],
             ['В3-01 - 1..5 ', '6-15', '1000', '1188', '1188', '1188', '1528', '6108'],
             ['В3-02 - 1..5 ', '6-15', '1250', '1270', '1270', '1270', '1756', '6108'],
             ['В3-03 - 1..5 ', '6-15', '1600', '1301', '1301', '1301', '1756', '6307'],
             ['В3-04 - 1..5 ', '6-15', '2000', '1470', '1470', '1470', '1925', '6503'],
             ['В3-05 - 1..5 ', '6-15', '2500', '1760', '1760', '1760', '2179', '6624'],
             ['В3-06 - 1..5 ', '6-15', '3150', '1955', '1955', '1955', '2485', '7063'],
             ['В3-07 - 1..5 ', '6-15', '4000', '2160', '2160', '2160', '2179', '7129'],
             ['В3-08 - 1..5 ', '20', '1250', '4472', '6366', '6735', '6735', '6735'],
             ['В3-09 - 1..5 ', '20', '1600', '4874', '7267', '7476', '7476', '7476'],
             ['В3-10 - 1..5 ', '20', '2000', '4874', '7390', '7476', '7476', '7476'],
             ['В3-11 - 1..5 ', '20', '2500', '4874', '8533', '8533', '8533', '8533'],
             ['В3-12 - 1..5 ', '20', '3150', '5352', '8898', '8898', '8898', '8898'],
             ['В3-13 - 1..5 ', '35', '630', '5518', '5518', '10148', '10148', '10148'],
             ['В3-14 - 1..5 ', '35', '800(1000)', '5533', '5533', '10148', '10148', '10148'],
             ['В3-15 - 1..5 ', '35', '1250', '9928', '9928', '10148', '10148', '10148'],
             ['В3-16 - 1..5 ', '35', '1600', '10418', '10418', '11447', '11447', '11447'],
             ['В3-17 - 1..5 ', '35', '2000', '11038', '11038', '11447', '11447', '11447'],
             ['В3-18 - 1..5 ', '35', '2500', '11589', '11589', '12003', '12003', '12003'],
             ['В3-19 - 1..5 ', '35', '3150', '11860', '11860', '12003', '12003', '12003']],
        'Таблица В4. УНЦ ячейки выключателя ВУ 110 - 500 кВ с учетом здания ЗРУ (тыс. руб.)':
             [['Номер расценок', 'Напряжение, кВ', 'Номинальный ток, А', ' Нормативы цены', '-', '-'],
              ['-', '-', '-', '1', '2', '3'],
              ['-', '-', '-', 'Номинальный ток отключения, кА', '-', '-', ],
              ['-', '-', '-', '40', '50', '63'],
              ['В4-01 - 1..3 ', '110', 'вне зависимости ', '40670', '45507', '45507'],
              ['В4-02 - 1..3 ', '220 (150) ', '2000', '88743', '92417', '97315'],
              ['В4-03 - 1..3 ', '220 (150) ', '2500', '94866', '98540', '103438'],
              ['В4-04 - 1..3 ', '220 (150) ', '3150', '103438 ', '103438 ', '108337'],
              ['В4-05 - 1..3 ', '330', '2500', '176282', '176282', '178731'],
              ['В4-06 - 1..3 ', '330', '3150', '182405', '182405', '184854'],
              ['В4-07 - 1..3 ', '500', 'вне зависимости ', '298182', '298182', '298182']],
        'Таблица В5. УНЦ ячейки выключателя ВУ 110 - 500 кВ без учета здания ЗРУ (тыс. руб.)':
              [['Номер расценок', 'Напряжение, кВ', 'Номинальный ток, А', ' Нормативы цены', '-', '-'],
               ['-', '-', '-', '1', '2', '3'],
               ['-', '-', '-', 'Номинальный ток отключения, кА', '-', '-', ],
               ['-', '-', '-', '40', '50', '63'],
               ['В5-01 - 1..3 ', '110', 'вне зависимости ', '23533', '28530', '28530'],
               ['В5-02 - 1..3 ', '220 (150) ', '2000', '57058', '60854', '65914'],
               ['В5-03 - 1..3 ', '220 (150) ', '2500', '65843', '69638', '74699'],
               ['В5-04 - 1..3 ', '220 (150) ', '3150', '74699', '74699', '79759'],
               ['В5-05 - 1..3 ', '330', '2500', '137954', '137954', '140485'],
               ['В5-06 - 1..3 ', '330', '3150', '144334', '144334', '146864'],
               ['В5-07 - 1..3 ', '500', 'вне зависимости ', '262392', '262392', '262392']],
        '2. Объекты электросетевого хозяйства с использованием управляемых элементов сети  (автоматического пункта секционирования (реклоузера) 6 - 35 кВ, выключателя 6 - 750 кВ)':[['2. Объекты электросетевого хозяйства с использованием управляемых элементов сети']],
        'Таблица В6. УНЦ автоматического пункта секционирования (реклоузера) 6 - 35 кВ без ПКУ (тыс. руб.)':
               [['Номер расценок', 'Напряжение, кВ', 'Норматив цены'],
                ['В6-01', '6-15', '1358'],
                ['В6-02', '20', '1597'],
                ['В6-03', '35', '3474']],
        'Таблица В7. УНЦ автоматического пункта секционирования (реклоузера) 6 - 35 кВ с ПКУ и интеграцией в АСУТП (тыс. руб.)':
               [['Номер расценок', 'Напряжение, кВ', 'Норматив цены'],
                ['В7-01', '6-15', '1663'],
                ['В7-02', '20', '2037'],
                ['В7-03', '35', '4277']],
        'Таблица Д3. УНЦ ШПС (тыс. руб.)':
                [['Номер расценок', 'Напряжение, кВ', 'Норматив цены'],
                 ['Д3-01', '6 - 220', '447'],
                 ['Д3-02', '330 - 750', '1241']],
        '3. Ячейка трансформатора, регулировочного трансформатора, ячейка реактора ТОР (ДГР) 6 - 750 кВ':['3. Ячейка трансформатора, регулировочного трансформатора, ячейка реактора ТОР (ДГР) 6 - 750 кВ'],
        'Таблица Т1. УНЦ ячейки трансформатора 110 - 500 кВ (тыс. руб.)':
                [['Номер расценок ', 'Мощность, МВА ', 'Норматив цены для отдельных элементов в составе расценки ', '-', '-', '-'],
                 ['-', '-', '1', '2', '3', '4'],
                 ['-', '-', 'Обозначение трехобмоточного трансформатора, напряжение, кВ ', '-', '-'],
                 ['-', '-', 'Т 110/35/НН <*> ', 'Т 150/35/НН ', 'Т 220/35(20, 110)/НН ', 'Т 500/110/НН'],
                 ['Т1-01 - 1..4 ', '6,3 ', '32118 ', '- ', '-', '-'],
                 ['Т1-02 - 1..4 ', '10', '37578', '- ', '47558 ', '-'],
                 ['Т1-03 - 1..4 ', '16', '50105', '50105', '-', '-'],
                 ['Т1-04 - 1..4 ', '25', '51394', '70277', '80036', '-'],
                 ['Т1-05 - 1..4 ', '32', '54158', '77270', '96174', '-'],
                 ['Т1-06 - 1..4 ', '40', '54158', '95828', '109622', '-'],
                 ['Т1-07 - 1..4 ', '63', '69356', '115424', '119804', '-'],
                 ['Т1-08 - 1..4 ', '80', '143578 ', '-', '179726', '-'],
                 ['Т1-09 - 1..4 ', '100', '175859', '189788', '193654', '-'],
                 ['Т1-10 - 1..4 ', '125', '-', '-', '246837', '-'],
                 ['Т1-11 - 1..4 ', '160', '192654', '-', '-', '-'],
                 ['Т1-12 - 1..4 ', '200', '-', '-', '340540', '-'],
                 ['Т1-13 - 1..4 ', '300', '-', '-', '-', '396 411']],
        'Таблица Т2. УНЦ ячейки трансформатора 150 - 500 кВ (тыс. руб.)':
                 [['Номер расценок ', 'Мощность, МВА ', 'Норматив цены для отдельных элементов в составе расценки ', '-', '-', '-', '-'],
                  ['-', '-', '1', '2', '3', '4', '5'],
                  ['-', '-', 'Обозначение автотрансформатора, напряжение, кВ', '-', '-', '-', '-'],
                  ['-', '-', 'АТ 220(150)/110/НН ', 'АТ 330/110/НН ', 'АТ 330/150/НН ', 'АТ 330/220/НН ', 'АТ 500/220(110)/НН'],
                  ['Т2-01 - 1..5 ', '63', '131765', '-', '-', '-', '-'],
                  ['Т2-02 - 1..5 ', '80', '131765', '-', '-', '-', '-'],
                  ['Т2-03 - 1..5 ', '100', '165319', '-', '-', '-', '-'],
                  ['Т2-04 - 1..5 ', '125', '165319', '213506', '-', '-', '-'],
                  ['Т2-05 - 1..5 ', '150', '187689', '225524', '-', '-', '-'],
                  ['Т2-06 - 1..5 ', '200', '187689', '237541', '242973', '-', '-'],
                  ['Т2-07 - 1..5 ', '250', '187689', '263977', '263976', '267780', '301964'],
                  ['Т2-08 - 1..5 ', '500', '-', '-', '-', '-', '384105']],
        'Таблица Т3. УНЦ ячейки трансформатора 330 - 750 кВ (тыс. руб.)':
                 [['Номер расценок ', 'Мощность, МВА ', 'Норматив цены для отдельных элементов в составе расценки ', '-', '-', '-', '-'],
                  ['-', '-', '1', '2', '3', '4', '5'],
                  ['-', '-', 'Обозначение автотрансформатора, напряжение, кВ', '-', '-', '-', '-'],
                  ['-', '-', 'АТ 330/220/НН ', 'АТ 500/110(220)/НН ', 'АТ 500/330/НН ', 'АТ 750/330/НН ', 'АТ 750/500/НН '],
                  ['Т3-01 - 1..5 ', '3×133 ', '465145 ', '412236', '-', '-', '-'],
                  ['Т3-02 - 1..5 ', '3×135 (3×150) ', '- ', '463910', '- ', '- ', '- '],
                  ['Т3-03 - 1..5 ', '3×167 ', '- ', '517311', '541302 ', '- ', '- '],
                  ['Т3-04 - 1..5 ', '3×267 (3×250) ', '- ', '603042', '- ', '- ', '- '],
                  ['Т3-05 - 1..5 ', '3×333 ', '- ', '- ', '- ', '1090981', '-'],
                  ['Т3-06 - 1..5 ', '3×417 ', '- ', '- ', '- ', '- ', '1283452 ']],
       'Таблица Т4. УНЦ ячейки трансформатора 35 - 500 кВ (тыс. руб.)':
                  [['Номер расценок ', 'Мощность, кВА ', '- ', '- ', '- ', '- ', '- '],
                   ['', '', '1', '2', '3', '4', '5', '6'],
                   ['', '', 'Обозначение двухобмоточного трансформатора, напряжение, кВ ', '-', '-', '-', '-', '-'],
                   ['', '', 'Т 35/НН ', 'Т 110/НН ', 'Т 150/НН ', 'Т 220/НН ', 'Т 330/НН ', 'Т 500/НН '],
                   ['Т4-01 - 1..6 ', '2', '12774', '19078', '- ', '- ', '- ', '- '],
                   ['Т4-02 - 1..6 ', '2,5 ', '12774', '23088', '- ', '- ', '- ', '- '],
                   ['Т4-03 - 1..6 ', '4', '12906', '24338', '- ', '- ', '- ', '- '],
                   ['Т4-04 - 1..6 ', '5', '13695', '27426', '- ', '34 096 ', '- ', '- '],
                   ['Т4-05 - 1..6 ', '6,3 ', '13695', '27426', '- ', '41 033 ', '- ', '- '],
                   ['Т4-06 - 1..6 ', '10', '20978', '28252', '- ', '47 558 ', '- ', '- '],
                   ['Т4-07 - 1..6 ', '16', '23169', '36657', '41854', '49 943 ', '- ', '- '],
                   ['Т4-08 - 1..6 ', '20', '42524', '48424', '- ', '- ', '- ', '- '],
                   ['Т4-09 - 1..6 ', '25', '48392', '48424', '- ', '67933', '97 016 ', '- '],
                   ['Т4-10 - 1..6 ', '32', '56291', '56291', '71622', '81 381 ', '- ', '- '],
                   ['Т4-11 - 1..6 ', '40', '58303', '58303', '86193', '90 572 ', '- ', '- '],
                   ['Т4-12 - 1..6 ', '50', '58303', '58303', '- ', '- ', '- ', '- '],
                   ['Т4-13 - 1..6 ', '63', '58303', '58303', '93786 ', '98165 ', '139086', '- '],
                   ['Т4-14 - 1..6 ', '70', '- ', '68830', '114863 ', '- ', '-', '- '],
                   ['Т4-15 - 1..6 ', '80', '- ', '68830', '- ', '132423 ', '148963', '- '],
                   ['Т4-16 - 1..6 ', '100', '- ', '130468', '141337 ', '145334 ', '148963', '- '],
                   ['Т4-17 - 1..6 ', '125', '- ', '147770', '- ', '158039', '164006', '- '],
                   ['Т4-18 - 1..6 ', '150', '- ', '160559', '- ', '- ', '- ', '195299'],
                   ['Т4-19 - 1..6 ', '160', '- ', '160559', '- ', '164426', '- ', '- '],
                   ['Т4-20 - 1..6 ', '200', '- ', '187572', '- ', '191439', '- ', '- '],
                   ['Т4-21 - 1..6 ', '250', '- ', '- ', '- ', '235520', '- ', '313003'],
                   ['Т4-22 - 1..6 ', '400', '- ', '- ', '- ', '367764', '- ', '489560']]
           'Таблица Т5. УНЦ ячейки трансформатора 6 - 35 кВ (тыс. руб.)':
                   ['Номер расценок ', 'Мощность, кВА ', 'Норматив цены для отдельных элементов в составе расценки ', '-', '-', '-', '-'],
                   ['-', '-', '1', '2', '3', '4', '5'],
                   ['-', '-', 'Обозначение двухобмоточного трансформатора, напряжение, кВ ', '-', '-', '-', '-'],
                   ['-', '-', 'масляный Т 6 (10, 15)/НН ', 'масляный Т 20/НН ', 'Т 35/НН ', 'сухой Т 6 (10, 15)/НН ', 'сухой Т 20/НН'],
                   ['Т5-01 - 1..5 ', '1,25 ', '52', '88', '- ', '68', '115'],
                   ['Т5-02 - 1..5 ', '2,5 ', '65', '111', '- ', '75', '115'],
                   ['Т5-03 - 1..5 ', '4', '63', '107', '- ', '74', '115'],
                   ['Т5-04 - 1..5 ', '10', '70', '119', '- ', '114', '187'],
                   ['Т5-05 - 1..5 ', '16', '122', '207', '- ', '143', '232'],
                   ['Т5-06 - 1..5 ', '25', '122', '207', '- ', '152', '247'],
                   ['Т5-07 - 1..5 ', '40', '131', '215', '- ', '166', '258'],
                   ['Т5-08 - 1..5 ', '63', '151', '257', '- ', '204', '334'],
                   ['Т5-09 - 1..5 ', '80', '151', '257', '- ', '222', '364'],
                   ['Т5-10 - 1..5 ', '100', '189', '322', '1 031 ', '264', '432'],
                   ['Т5-11 - 1..5 ', '160', '239', '406', '1 649 ', '359', '589'],
                   ['Т5-12 - 1..5 ', '250', '309', '525', '2 182 ', '1 433 ', '2 410 '],
                   ['Т5-13 - 1..5 ', '300', '395', '671', '3 070 ', '1 494 ', '2 506 '],
                   ['Т5-14 - 1..5 ', '400', '395', '671', '3 070 ', '1 522 ', '2 553 '],
                   ['Т5-15 - 1..5 ', '500', '532', '905', '4 063 ', '1 688 ', '2 823 '],
                   ['Т5-16 - 1..5 ', '600', '532', '905', '4 063 ', '1 777 ', '2 975 '],
                   ['Т5-17 - 1..5 ', '630', '532', '905', '4 430 ', '1 777 ', '2 975 '],
                   ['Т5-18 - 1..5 ', '875', '886', '1 507 ', '6 807 ', '1 973 ', '3 277 '],
                   ['Т5-19 - 1..5 ', '1000', '886', '1 507 ', '6 619 ', '1 973 ', '3 277 '],
                   ['Т5-20 - 1..5 ', '1125', '1 053 ', '1 790 ', '7 957 ', '2 065 ', '3 420 '],
                   ['Т5-21 - 1..5 ', '1250', '1 220 ', '2 074 ', '8 329 ', '2 158 ', '3 562 '],
                   ['Т5-22 - 1..5 ', '1600', '1 761 ', '2 629 ', '10 400 ', '4 376 ', '6 881 '],
                   ['Т5-23 - 1..5 ', '2000', '2 311 ', '3 219 ', '12 774 ', '4 836 ', '7 262 '],
                   ['Т5-24 - 1..5 ', '2500', '2 477 ', '3 492 ', '12 774 ', '5 095 ', '7 702 '],
                   ['Т5-25 - 1..5 ', '3150', '3 732 ', '5 622 ', '- ', '5 289 ', '8 032 '],
                   ['Т5-26 - 1..5 ', '4000', '8 028 ', '11 061 ', '12 906 ', '8 463 ', '11 481 '],
                   ['Т5-27 - 1..5 ', '6300', '13 692 ', '13 695 ', '13 695 ', '- ', '- '],
                   ['Т5-28 - 1..5 ', '10000', '19 464 ', '20 978 ', '20 978 ', '- ', '- '],
                   ['Т5-29 - 1..5 ', '16000', '23 169 ', '23 169 ', '23 169 ', '- ', '- '],
                 'Таблица Т6. УНЦ регулировочного трансформатора 6 - 35 кВ (тыс. руб.)',      
                    ['Номер расценок ', 'Мощность, МВА ', 'Норматив цены для отдельных элементов в составе расценки ', '-'],
                    ['-', '-', '1', '2'],
                    ['-', '-', 'Напряжение, кВ ', '-'],
                    ['-', '-', '6-15', '35(20) '],
                    ['Т6-01 - 1..2 ', '16', '17 364 ', '- '],
                    ['Т6-02 - 1..2 ', '40', '31 297 ', '33 766 '],
                    ['Т6-03 - 1..2 ', '63', '39 313 ', '39 313 '],



        }
