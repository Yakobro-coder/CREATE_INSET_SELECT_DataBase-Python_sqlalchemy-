# SELECT REQUESTS

def select_db(connection):
    # Альбомы 2018 выпуска
    print('Альбомы 2018 года выпуска:')
    alubums_in_2018 = connection.execute("""SELECT name_album, release_date FROM albums
    WHERE release_date = 2018;""").fetchall()
    for album in alubums_in_2018:
        print(f'Альбом "{album[0]}" выпущен в {album[1]} году.')
    print()

    # Самый долгий трек
    long_track = connection.execute("""SELECT name_track, duration FROM tracks
    ORDER BY duration  DESC;""").fetchmany(1)[0]
    if long_track[1] // 60 != 0:
        duration = long_track[1] // 60
    else:
        duration = 0
    print(f'Самый длинный трек "{long_track[0]}" '
          f'продолжительностью в {duration}:{long_track[1] % 60}({long_track[1]} sec.)')
    print()

    # Треки >= 3.5мин(210сек)
    tracks_longer_210 = connection.execute("""SELECT name_track FROM tracks
    WHERE duration  >= 210;""").fetchall()
    print('Треки длинее 3.5мин(210сек):')
    for track in tracks_longer_210:
        print('-', track[0])
    print()

    # Альбомы выпуска включительно с 2018 по 2020
    print('Альбомы c 2018 по 2020 год выпуска включительно:')
    albums_2018_2020 = connection.execute("""SELECT name_album, release_date FROM albums
    WHERE release_date BETWEEN 2018 AND 2020;""").fetchall()
    for album in albums_2018_2020:
        print(f'Альбом "{album[0]}"')
    print()

    # Исполнители с именем в одно слово
    performers_one_word = connection.execute("""SELECT name_nickname FROM list_performers
    WHERE name_nickname NOT LIKE '%% %%';""").fetchall()
    print('Исполнители с именем в одно слово:')
    print(performers_one_word)
    print()

    # Треки с вхождением 'мой' или 'my' в название
    tracks_my = connection.execute("""SELECT name_track FROM tracks
    WHERE name_track iLIKE '%%my%%' OR name_track iLIKE '%%мой%%';""").fetchall()
    print('Треки в название которых входит "мой" или "my":')
    print(tracks_my)
