from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):  # метод, который вызывается после создании объекта
        try:
            datetime.strptime(
                self.birthdate, "%Y/%m/%d"
            )  # преобразование строки в объект даты - время по заданному формату
        except ValueError:
            raise ValueError(
                f"birthdate format might be invalid: {self.birthdate}. Expected format: YYYY/MM/DD"
            )
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"gpa must be between 0 and 5, got {self.gpa}")

    def age(self) -> int:
        birth_day = datetime.strptime(
            self.birthdate, "%Y/%m/%d"
        ).date()  # отбрасываем время. ((для времени: (%H:%M:%S)))
        today = date.today()  # получение текущей даты
        if today.month > birth_day.month:
            return today.year - birth_day.year
        if today.month < birth_day.month:
            return today.year - birth_day.year - 1
        if today.day >= birth_day.day:
            return today.year - birth_day.year
        return today.year - birth_day.year - 1

    def to_dict(self) -> dict:  # преобразование объекта в словарь
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod  # используем, когда создаем новый объект
    def from_dict(cls, d: dict):  # создание объекта из словаря
        # TODO: реализовать десереализацию из словаря
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):  # строковое представление
        # TODO: f"{}, {}, {}"
        return f"{self.fio}, {self.birthdate}, {self.group}, {self.gpa}"


# strftime = "string format time" (дата → строка)
# strptime = "string parse time" (строка → дата)
