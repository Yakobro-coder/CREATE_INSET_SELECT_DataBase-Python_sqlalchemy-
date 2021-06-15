
def create_table(connection):
    connection.execute('create table if not exists list_performers('
                       'id_performer serial unique,'
                       'name_nickname varchar(70) not null,'
                       'constraint list_performers_pk primary key (id_performer, name_nickname)'
                       ');')

    connection.execute('create table if not exists list_genres('
                       'id_genre serial primary key,'
                       'genre_name varchar(40) not null unique'
                       ');')

    connection.execute('create table if not exists genre_performer('
                       'id_performer integer references list_performers(id_performer),'
                       'id_genre integer references list_genres(id_genre),'
                       'constraint genre_performer_pk primary key (id_performer, id_genre)'
                       ');')

    connection.execute('create table if not exists albums('
                       'id_album serial unique,'
                       'name_album text not null,'
                       'release_date integer not null,'
                       'constraint albums_pk primary key (id_album, name_album)'
                       ');')

    connection.execute('create table if not exists performers_in_album('
                       'id_album integer references albums(id_album),'
                       'id_performer integer references list_performers(id_performer),'
                       'constraint performers_in_album_pk primary key (id_album, id_performer)'
                       ');')

    connection.execute('create table if not exists collections('
                       'id_collection serial unique,'
                       'name_collection varchar(70) not null,'
                       'release_date integer not null,'
                       'constraint collections_pk primary key (id_collection,name_collection)'
                       ');')

    connection.execute('create table if not exists tracks('
                       'id_track serial unique,'
                       'name_track varchar(100) not null,'
                       'id_album integer references albums(id_album),'
                       'duration integer not null,'
                       'constraint tracks_pk primary key (id_track, name_track, id_album)'
                       ');')

    connection.execute('create table if not exists tracks_in_collection('
                       'id_collection integer references collections(id_collection),'
                       'id_track integer references tracks(id_track)'
                       ');')
