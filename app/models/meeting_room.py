from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.core.db import Base
# from app.models.reservation import Reservation  # класс для связи


class MeetingRoom(Base):
    # Имя переговорки должно быть не больше 100 символов,
    # уникальным и непустым.
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # Установите связь между моделями через функцию relationship.
    reservations = relationship('Reservation', cascade='delete')
    # Можно установить связь, указав класс модели, чтобы не импортировать модели в __init__
    # reservations = relationship(Reservation, cascade='delete')
