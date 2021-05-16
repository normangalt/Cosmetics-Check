import unittest

from vision_api import Knot, Cream

from unittest import TestCase

class TestVisionAPI(TestCase):
    def setUp(self):
        self.cream = Cream()
        with open('example.jpg', 'rb') as f:
            self.photo1 = f.read()
        with open('example2.jpg', 'rb') as f:
            self.photo2 = f.read()
        detected_text_1 = self.cream.detect_text(self.photo1)
        self.processed_text_1 = self.cream.process_text(detected_text_1)

        detected_text_2 = self.cream.detect_text(self.photo2)
        self.processed_text_2 = self.cream.process_text(detected_text_2)

    def test_process_text(self):
        result_1 = ['Drug Facts', 'Purpose', 'Active ingredient', 'Petrolatum 46.5%', '.Skin protectant (ointment)', \
                    'Uses', 'I temporarily protects and helps relieve chafed', 'chapped or cracked skin', 'I temporarily protects minor:', \
                    'I cuts scrapes burns', 'Ihelps protect from the drying effects of wind and cold weather.', 'Warnings', 'For external use only', \
                    'When using this product do not get into eyes', 'Stop use and ask a doctor if condition worsens symptoms last', \
                    'more than 7 days or clear up and occur again within a few days', 'Do not use on', 'deep or puncture wounds', \
                    'Keep out of reach of children. If swallowed', 'get medical help or contact', 'a Poison Control Center immediately', \
                    'animal bites serious burns', 'Directions', 'apply as needed', 'Inactive ingredients', 'mineral oil', 'paraffin', 'ozokerite', 'dimethicone', \
                    'hyaluronic acid', 'sodium', 'ydroxide', 'ceramide 1', 'ceramide 3', 'ceramide 6-11', 'tocopheryl acetate', 'phytosphingosine', 'cholesterol', \
                    'sodium lauroyl lactylate', 'carbomer', 'anthenol', 'water', 'L-proline', 'xanthan gum', 'Questions?', 'B6-free number 1-888-768-2915', \
                    'ww.cerave.com', 'ile LLC', 'New York', 'NY 10001', 'in USA', 'terave.com', 'ons or Comments? 1-888-768-2915', '02422']

        result_2 = ['ВАША КОЖА СклонНА К ПОЯВЛЕНИЮ НЕСОВЕРШЕНСТВ?', 'Мультифункциональная антибактериальная формула косметического средства', 'ОЧИЩЕНИЕ R1 ПРОТИВ НЕСОВЕРШЕНСТВ от NIVEA@ обогащена натуральным', \
                    '1. Средстве ывания: сокращает и предотвращает появлен в ного блеска', '12 Скраб: рас ет закупоренные поры', 'освобождает кож точек и', 'страктом лии и белой глиной:', 'надолго.', 'Помогает бо с бактериями', \
                    'вызывающими воспалет', 'Маска: испол я в начестве маски при нане н', 'еколько', 'минут. Улучшае пица', 'HACNAAMTECB 4NCTO M 3AOPOBBIM BMHONTNTEGƯONGE', 'а оубоко очишщена', 'лзаметно более здорсвая', \
                    'MМЕНЕНИЕ: МЯгкими масерующими ноурвъми никоиями нанесите средство', 'мажную кожу лица', 'шек вбдасти дена смате теплой водой. Используя в', 'вестве маски', 'оставьте на каже на 5- мину загам смойте. Избегайте области', \
                    'о паз. Ислользуйте ежедневно', 'с качестве маски - 2-3 раза в неделю.', 'к отимального результата используйте всю линию средств NIVEA для проблемной', 'ДЕРМАТОЛОГИЧЕСКИ ПРОТЕСТИРОВАНО.', \
                    'Fapююривает поры. Использование в пищевых целях опасно для жизни и здоровы.', 'акб для очищення 3 в 1 проти недоліків шкіри від NIVEA®', 'оведено во Франции', 'Космева С.А.С.', 'COSMEVA S.A.S.', \
                    '1 гuе des Sources F-77176', 'lemple', 'France. Bироблено у Франції', 'Космева С.А.С. Эксклюзивный импорея', 'ок 000 "Байерсдорф"', 'РФ', '105064', 'г. Москва', 'ул. Земляной Вал', 'дом 9. Телефм', \
                    'мни: 8-800-2000-753. Звонок по России бесплатный. Iмпортер в Укран:', 'кродорф Україна»', 'Україна', 'Київ-04119', 'вул. Дегтярівська 27Т. Годен дод', 'а: см', 'упаковку. Використати до: див. на упаковці. Умови зберiгання: п', \
                    'р 5-25°С', 'та відносній вологості <80%. Дата виробництва: за 30 міскцв да', 'аинористання.', 'Состав/Склад: Aqua', 'Kаolin', 'Glycerin', 'Alcohol Denat (3% od)', 'Glyceryl Stearate', 'Cetearyl Alcohol', 'Microcrystalline Ce', \
                    'Butyrospermum Parkii Butter', 'Caprylic/Capric Triglyceride', 'e', 'Magnolia Officinalis Bark Extract', 'Glyceryl Glucoside', 'Potassiom Ca', 'M Phosphate', 'Hydrogenated Palm Glycerides', 'Xanthan Gum', 'Dimethan', \
                    'Hydrogenated Castor Oil', 'Trisodium EDTA', 'Phenaxyethanol', 'Me', 'paraben', 'Alpha-Isomethyl lonone', 'Citronellol', 'Limonene', 'Par', 'CI 77891', 'CI 42090', 'Арт. 82305', '82305.986.BA.07', 'www.NIVEA.com', '150M', '動台', \
                    'Beiersdorf AG', 'D-20245 Наmburg', 'reg. tm. of Beiersdorf AG', 'Germany', 'LDPE', 'Beiersdorf', 'Hamburg', '• Wien']

        self.assertEqual(self.processed_text_1, result_1)
        self.assertEqual(self.processed_text_2, result_2)

    def test_find_ingredients(self):
        result_1 = ['Drug Facts', 'Purpose', 'Active ingredient', 'Petrolatum 46.5%', '.Skin protectant (ointment)', \
                    'Uses', 'I temporarily protects and helps relieve chafed', 'chapped or cracked skin', 'I temporarily protects minor:', \
                    'I cuts scrapes burns', 'Ihelps protect from the drying effects of wind and cold weather.', 'Warnings', 'For external use only', \
                    'When using this product do not get into eyes', 'Stop use and ask a doctor if condition worsens symptoms last', \
                    'more than 7 days or clear up and occur again within a few days', 'Do not use on', 'deep or puncture wounds', \
                    'Keep out of reach of children. If swallowed', 'get medical help or contact', 'a Poison Control Center immediately', \
                    'animal bites serious burns', 'Directions', 'apply as needed', 'Inactive ingredients', 'mineral oil', 'paraffin', 'ozokerite', 'dimethicone', \
                    'hyaluronic acid', 'sodium', 'ydroxide', 'ceramide 1', 'ceramide 3', 'ceramide 6-11', 'tocopheryl acetate', 'phytosphingosine', 'cholesterol', \
                    'sodium lauroyl lactylate', 'carbomer', 'anthenol', 'water', 'L-proline', 'xanthan gum', 'Questions?', 'B6-free number 1-888-768-2915', \
                    'ww.cerave.com', 'ile LLC', 'New York', 'NY 10001', 'in USA', 'terave.com', 'ons or Comments? 1-888-768-2915', '02422']

        result_2 = ['ВАША КОЖА СклонНА К ПОЯВЛЕНИЮ НЕСОВЕРШЕНСТВ?', 'Мультифункциональная антибактериальная формула косметического средства', 'ОЧИЩЕНИЕ R1 ПРОТИВ НЕСОВЕРШЕНСТВ от NIVEA@ обогащена натуральным', \
                    '1. Средстве ывания: сокращает и предотвращает появлен в ного блеска', '12 Скраб: рас ет закупоренные поры', 'освобождает кож точек и', 'страктом лии и белой глиной:', 'надолго.', 'Помогает бо с бактериями', \
                    'вызывающими воспалет', 'Маска: испол я в начестве маски при нане н', 'еколько', 'минут. Улучшае пица', 'HACNAAMTECB 4NCTO M 3AOPOBBIM BMHONTNTEGƯONGE', 'а оубоко очишщена', 'лзаметно более здорсвая', \
                    'MМЕНЕНИЕ: МЯгкими масерующими ноурвъми никоиями нанесите средство', 'мажную кожу лица', 'шек вбдасти дена смате теплой водой. Используя в', 'вестве маски', 'оставьте на каже на 5- мину загам смойте. Избегайте области', \
                    'о паз. Ислользуйте ежедневно', 'с качестве маски - 2-3 раза в неделю.', 'к отимального результата используйте всю линию средств NIVEA для проблемной', 'ДЕРМАТОЛОГИЧЕСКИ ПРОТЕСТИРОВАНО.', \
                    'Fapююривает поры. Использование в пищевых целях опасно для жизни и здоровы.', 'акб для очищення 3 в 1 проти недоліків шкіри від NIVEA®', 'оведено во Франции', 'Космева С.А.С.', 'COSMEVA S.A.S.', \
                    '1 гuе des Sources F-77176', 'lemple', 'France. Bироблено у Франції', 'Космева С.А.С. Эксклюзивный импорея', 'ок 000 "Байерсдорф"', 'РФ', '105064', 'г. Москва', 'ул. Земляной Вал', 'дом 9. Телефм', \
                    'мни: 8-800-2000-753. Звонок по России бесплатный. Iмпортер в Укран:', 'кродорф Україна»', 'Україна', 'Київ-04119', 'вул. Дегтярівська 27Т. Годен дод', 'а: см', 'упаковку. Використати до: див. на упаковці. Умови зберiгання: п', \
                    'р 5-25°С', 'та відносній вологості <80%. Дата виробництва: за 30 міскцв да', 'аинористання.', 'Состав/Склад: Aqua', 'Kаolin', 'Glycerin', 'Alcohol Denat (3% od)', 'Glyceryl Stearate', 'Cetearyl Alcohol', 'Microcrystalline Ce', \
                    'Butyrospermum Parkii Butter', 'Caprylic/Capric Triglyceride', 'e', 'Magnolia Officinalis Bark Extract', 'Glyceryl Glucoside', 'Potassiom Ca', 'M Phosphate', 'Hydrogenated Palm Glycerides', 'Xanthan Gum', 'Dimethan', \
                    'Hydrogenated Castor Oil', 'Trisodium EDTA', 'Phenaxyethanol', 'Me', 'paraben', 'Alpha-Isomethyl lonone', 'Citronellol', 'Limonene', 'Par', 'CI 77891', 'CI 42090', 'Арт. 82305', '82305.986.BA.07', 'www.NIVEA.com', '150M', '動台', \
                    'Beiersdorf AG', 'D-20245 Наmburg', 'reg. tm. of Beiersdorf AG', 'Germany', 'LDPE', 'Beiersdorf', 'Hamburg', '• Wien']

        ingredients_1 = self.cream.find_ingredients(self.photo1)
        ingredients_2 = self.cream.find_ingredients(self.photo2)

        self.assertEqual(ingredients_1, result_1)
        self.assertEqual(ingredients_2, result_2)
