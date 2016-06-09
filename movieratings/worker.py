import csv


def import_rater_data(apps, schema_editor):
    Rater = apps.get_model("movieratings", "Rater")
    with open("data/u.user") as infile:
        rater = csv.reader(infile, delimiter="|")
        for row in rater:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zip_code=row[4])
    # raise Exception("1 yay")


def import_movie_data(apps, schema_editor):
    Movie = apps.get_model("movieratings", "Movie")
    with open("data/u.item", encoding='latin1') as infile:
        movie = csv.reader(infile, delimiter="|")
        for row in movie:
            Movie.objects.create(id=row[0], movie_title=row[1], release_date=row[2], video_release_date=row[3],
                                 imdb_url=row[4], unknown=row[5], genre=row[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    # raise Exception("2 yay")


def import_rating_data(apps, schema_editor):
    Rating = apps.get_model("movieratings", "Rating")
    Movie = apps.get_model("movieratings", "Movie")
    Rater = apps.get_model("movieratings", "Rater")
    with open("data/u.data") as infile:
        rating = csv.reader(infile, delimiter="\t")
        for row in rating:
            rater_user_id = Rater.objects.get(id=row[0])
            movie_movie_id = Movie.objects.get(id=row[1])
            Rating.objects.create(user_id=rater_user_id, item_id=movie_movie_id, rating=row[2], timestamp=row[3])

    # raise Exception("3 yay")      # This is a great test
