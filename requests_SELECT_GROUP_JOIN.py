import sqlalchemy
from pprint import pprint


def select_requests():
    # 1.Количество исполнителей в каждом жанре;
    performers = connection.execute("""SELECT l.genre_name, COUNT(id_performer) from genre_performer g
JOIN list_genres l ON l.id_genre = g.id_genre
GROUP BY genre_name; """).fetchall()
    pprint(performers)
    print()

    # 2.Количество треков, вошедших в альбомы 2019 - 2020 годов;
    # Вывод  кол-во по годам
    count_track = connection.execute("""SELECT  a.release_date, COUNT(id_track) from tracks t
JOIN albums a ON a.id_album = t.id_album
WHERE a.release_date BETWEEN 2019 AND 2020
GROUP BY a.release_date;""").fetchall()
    pprint(count_track)
    print()

    # Вывод общего числа всех треков вошедших в альбомы 2019 - 2020 годов
    count_track_v2 = connection.execute("""SELECT COUNT(t.id_track) from tracks t
JOIN albums a ON a.id_album = t.id_album
WHERE a.release_date BETWEEN 2019 AND 2020
ORDER BY SUM(t.id_track);""").fetchall()
    pprint(count_track_v2)
    print()

    # 3.Cредняя продолжительность треков по каждому альбому;
    avg_duration = connection.execute("""SELECT a.name_album, AVG(duration) FROM tracks t
JOIN albums a ON a.id_album = t.id_album
GROUP BY a.name_album;""").fetchall()
    pprint(avg_duration)
    print()

    # 4.Все исполнители, которые не выпустили альбомы в 2020 году;
    # Добавил в конце GROUP BY id_performer так как у "Руки Вверх" два альбома
    # и он задваивает группу при выводе списка исполнителей
    all_performers_2020 = connection.execute("""SELECT DISTINCT l.id_performer, l.name_nickname FROM list_performers l
JOIN performers_in_album p ON p.id_performer = l.id_performer
JOIN albums a ON a.id_album = p.id_album
WHERE a.release_date != 2020
ORDER BY l.id_performer;""").fetchall()
    pprint(all_performers_2020)
    print()

    # 5.Названия сборников, в которых присутствует конкретный исполнитель (выберите сами)-'Триагрутрика';
    name_collection = connection.execute("""SELECT name_collection FROM collections c
JOIN tracks_in_collection tc ON c.id_collection = tc.id_collection
JOIN tracks t ON t.id_track = tc.id_track
JOIN albums a ON a.id_album = t.id_album
JOIN performers_in_album pa ON pa.id_album = a.id_album
JOIN list_performers lp ON lp.id_performer = pa.id_performer
WHERE lp.name_nickname LIKE 'Триагрутрика';""").fetchall()
    pprint(name_collection)
    print()

    # 6.Название альбомов, в которых присутствуют исполнители более 1 жанра;
    name_album = connection.execute("""SELECT name_album FROM albums a
JOIN performers_in_album pa ON pa.id_album = a.id_album
JOIN list_performers lp ON lp.id_performer = pa.id_performer
JOIN genre_performer gp ON gp.id_performer = lp.id_performer
GROUP BY a.name_album
HAVING COUNT(gp.id_genre) > 1;""").fetchall()
    pprint(name_album)
    print()

    # 7.Наименование треков, которые не входят в сборники;
    tracks_not_in_collection = connection.execute("""SELECT name_track FROM tracks t
LEFT JOIN tracks_in_collection tc ON t.id_track = tc.id_track
WHERE tc.id_collection IS NULL;""").fetchall()
    pprint(tracks_not_in_collection)
    print()

    # 8.Вывести исполнителя(-ей), написавшего самый короткий по продолжительности трек
    # (теоретически таких треков может быть несколько);
    performer_mini_track = connection.execute("""SELECT lp.name_nickname, t.duration FROM list_performers lp
JOIN performers_in_album pa ON lp.id_performer = pa.id_performer
JOIN albums a ON pa.id_album = a.id_album
JOIN tracks t ON a.id_album = t.id_album
WHERE t.duration = (SELECT MIN(t.duration) FROM tracks t);""").fetchall()
    pprint(performer_mini_track)
    print()

    # 9.Название альбомов, содержащих наименьшее количество треков.
    mini_album = connection.execute("""SELECT name_album, COUNT(t.id_album) FROM albums a
JOIN tracks t ON a.id_album = t.id_album
GROUP BY a.name_album, t.id_album
HAVING COUNT(t.id_album) = (
SELECT MIN(count)
FROM (SELECT COUNT(t.id_album) FROM albums a
JOIN tracks t ON a.id_album = t.id_album
GROUP BY t.id_album)AS count
);""").fetchall()
    pprint(mini_album)
    print()


if __name__ == '__main__':
    db = 'postgresql://tester:1234@localhost:5432/test_base'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()

    select_requests()
