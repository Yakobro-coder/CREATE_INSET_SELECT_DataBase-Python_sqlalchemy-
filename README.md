
---
<details>
  <summary>Описание выполненного здесь задания.</summary>
  
## ДЗ(Практика) «Select-запросы, выборки из одной таблицы»

**КОД создания БД в модуле ["requests_CREATE.py"](https://github.com/Yakobro-coder/CREATE_INSET_SELECT_DataBase-Python_sqlalchemy-/blob/master/requests_CREATE.py)**
### Задание 1
 **КОД в модуле ["requests_INSERT.py"](https://github.com/Yakobro-coder/CREATE_INSET_SELECT_DataBase-Python_sqlalchemy-/blob/master/requests_INSERT.py)**

Заполнить базу(Схема БД файл **["scheme_database.png"](https://github.com/Yakobro-coder/CREATE_INSET_SELECT_DataBase-Python_sqlalchemy-/blob/master/scheme_database.png)**). В ней должно быть:

* не менее 8 исполнителей;
* не менее 5 жанров;
* не менее 8 альбомов;
* не менее 15 треков;
* не менее 8 сборников.
  
Должны быть заполнены все поля каждой таблицы, в т.ч. таблицы связей 
(исполнителей с жанрами, исполнителей с альбомами, сборников с треками).

### Задание 2
**КОД в модуле ["requests_SELECT.py"](https://github.com/Yakobro-coder/CREATE_INSET_SELECT_DataBase-Python_sqlalchemy-/blob/master/requests_SELECT.py)**

Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.  
Результаты запросов не должны быть пустыми (учесть при заполнении таблиц).

1. название и год выхода альбомов, вышедших в 2018 году;
2. название и продолжительность самого длительного трека;
3. название треков, продолжительность которых не менее 3,5 минуты;
4. названия сборников, вышедших в период с 2018 по 2020 год включительно;
5. исполнители, чье имя состоит из 1 слова;
6. название треков, которые содержат слово "мой"/"my".

### Задание 3
**КОД в модуле ["requests_SELECT_GROUP_JOIN.py"](https://github.com/Yakobro-coder/CREATE_INSET_SELECT_DataBase-Python_sqlalchemy-/blob/master/requests_SELECT_GROUP_JOIN.py)**

Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
Результаты запросов не должны быть пустыми (при необходимости добавьте данные в таблицы).

1. количество исполнителей в каждом жанре;
2. количество треков, вошедших в альбомы 2019-2020 годов;
3. средняя продолжительность треков по каждому альбому;
4. все исполнители, которые не выпустили альбомы в 2020 году;
5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
6. название альбомов, в которых присутствуют исполнители более 1 жанра;
7. наименование треков, которые не входят в сборники;
8. исполнителя(-ей), написавшего самый короткий по продолжительности трек 
   (теоретически таких треков может быть несколько);
9. название альбомов, содержащих наименьшее количество треков.

</details>

---