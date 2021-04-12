import json
from conexao import mydb


def getSource(latitude, longitude, distance):
    # Gets all posts away from (latitude) and (longitude) by (distance) km, calculated on a Radius Perpective
    try:
        sql = \
            ' SELECT * FROM ' \
            ' ( ' \
            '    SELECT ' \
            '        a.*, ' \
            '        ROUND(111.111 * ' \
            '        DEGREES(ACOS(LEAST(1.0, COS(RADIANS(%s)) ' \
            '           * COS(RADIANS(a.latitude)) ' \
            '           * COS(RADIANS(%s - a.longitude)) ' \
            '           + SIN(RADIANS(%s)) ' \
            '           * SIN(RADIANS(a.latitude))))), 4) AS distance_in_km ' \
            '    FROM posts a ' \
            ' ) post_distance ' \
            ' WHERE distance_in_km < %s ' \
            % (latitude, longitude, latitude, distance)

        posts = mydb.cursor(dictionary=True)
        posts.execute(sql)

        posts = posts.fetchall()

        json_output = json.dumps(posts, indent=4, sort_keys=True, default=str)

        return json_output

    except Exception as E:
        print("Error: " + repr(E))


def postData(json_data):
    try:
        mydb.start_transaction()
        print('Starting process for user ' + str(json_data['nick']))

        query = mydb.cursor(dictionary=True)

        sql = "INSERT INTO posts(nick, post, latitude, longitude, post_date) " \
              "VALUES ('%s', '%s', %s, %s, NOW())" \
              % (json_data['nick'], json_data['post'], json_data['latitude'], json_data['longitude'])
        query.execute(sql)

        post_id = query.lastrowid

        mydb.commit()
        return '{"post_id": %s}' % post_id

    except KeyError as E:
        mydb.rollback()
        return '{"erro": "Field not found: %s"}' % str(E)

    except Exception as E:
        mydb.rollback()
        return '{"erro": "Non-mapped error: "%s"}' % str(E)