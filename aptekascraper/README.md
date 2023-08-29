# Задание выполнил Сергей Усынин (usynin.s00@mail.ru TG:@arts_context) для компании Brandquad

# Обзор проекта:

В данном проекте парсятся товары определенных каталогов по домену apteka-ot-sklada.ru.
Вот ссылки на категории товаров, с которых забирается информация:

1. Витамины для детей: [https://apteka-ot-sklada.ru/tomsk/catalog/medikamenty-i-bady/vitaminy-i-mikroelementy/vitaminy-dlya-detey]
2. Зубные пасты для взрослых: [https://apteka-ot-sklada.ru/tomsk/catalog/sredstva-gigieny/uhod-za-polostyu-rta/pasty-zubnye-vzroslym]
3. Косметические масла: [https://apteka-ot-sklada.ru/tomsk/catalog/kosmetika/masla-kosmeticheskie/kosmeticheskoe-maslo/]


# Как подготовить проект к запуску:

1. Создайте и активируйте виртуальное окружение:
```shell
python -m venv venv
source venv/bin/activate
```
2. Находясь в директории ~/scrapy_drug_store/aptekascraper/ скачиваем все библиотеки из файла requirements.txt:
```shell
pip install -r requirements.txt
```

# Как запустить проект:

- Чтобы паук смог забрать информацю с сайта и дать готовый json файл с информацией о товарах, необходимо использовать команду:
```shell
scrapy crawl имя_паука
```

- Вот команды для запуска всех трех пауков:
```shell
scrapy crawl cosmeticoilspider # для косметических масел

scrapy crawl adulttoothpastespider # для зубной пасты для взрослых

scrapy crawl childrenvitaminsspider # для детских витаминов
```

- После этого появится файлы с расширемние json, где будет представлена вся информация о товарах. 

# Обзор по информации, согласно шаблону задания:

[X] - Информация забирается из сайта либо генерируется;
[-] - Подобая информация не найдена мною на сайте, но передается в json как 0, 1 или [].

- "timestamp" [X]

- "RPC" [X]

- "url" [X]

- "title" [X]

- "marketing_tags" [-]

- "brand"  [X] 

- "section" [X]

- "price_data": {
    "current" [X]
    "original" [X]
    "sale_tag" [X] (случаи скидок не обнаружены, но есть формула подсчета скидок в pipelines.py)
  },

- "stock": {
    "in_stock" [X]
    "count"  [X]
  },

- "assets": {
        "main_image" [X]
        "set_images" [-]
        "view360" [-] 
        "video" [-]
    },

- "metadata": {
        "__description" [X]
    }

- "variants": 1, [-]

