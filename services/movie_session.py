from datetime import datetime

from db.models import MovieSession, CinemaHall
from services.movie import get_movie_by_id


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(movie_id=movie_id,
                                show_time=movie_show_time,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> list[MovieSession]:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_id)


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None) -> None:
    session = get_movie_session_by_id(session_id)
    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie = get_movie_by_id(movie_id)
    if cinema_hall_id:
        session.cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    session.save()


def delete_movie_session_by_id(id_: int) -> None:
    MovieSession.objects.get(id=id_).delete()