from enum import Enum, auto
from datetime import datetime
from typing import List, Optional, Tuple


class DayOfWeek(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Prayer(Enum):
    NICENE_CREED = auto()
    OUR_FATHER = auto()
    HAIL_MARY = auto()
    GLORY_BE = auto()
    FATIMA_PRAYER = auto()
    HAIL_HOLY_QUEEN = auto()
    ST_MICHAEL = auto()
    ANNOUNCE_MYSTERY = auto()


class JoyfulMysteries(Enum):
    ANNUNCIATION = "The Annunciation"
    VISITATION = "The Visitation"
    NATIVITY = "The Nativity"
    PRESENTATION = "The Presentation"
    FINDING_IN_TEMPLE = "The Finding in the Temple"


class SorrowfulMysteries(Enum):
    AGONY_IN_GARDEN = "The Agony in the Garden"
    SCOURGING_AT_PILLAR = "The Scourging at the Pillar"
    CROWNING_WITH_THORNS = "The Crowning with Thorns"
    CARRYING_OF_CROSS = "The Carrying of the Cross"
    CRUCIFIXION = "The Crucifixion"


class GloriousMysteries(Enum):
    RESURRECTION = "The Resurrection"
    ASCENSION = "The Ascension"
    DESCENT_OF_HOLY_SPIRIT = "The Descent of the Holy Spirit"
    ASSUMPTION = "The Assumption"
    CORONATION_OF_MARY = "The Coronation of Mary"


class LuminousMysteries(Enum):
    BAPTISM_OF_JESUS = "The Baptism of Jesus"
    WEDDING_AT_CANA = "The Wedding at Cana"
    PROCLAMATION_OF_KINGDOM = "The Proclamation of the Kingdom"
    TRANSFIGURATION = "The Transfiguration"
    INSTITUTION_OF_EUCHARIST = "The Institution of the Eucharist"


class Mysteries(Enum):
    JOYFUL = List[JoyfulMysteries]
    SORROWFUL = List[SorrowfulMysteries]
    GLORIOUS = List[GloriousMysteries]
    LUMINOUS = List[LuminousMysteries]


class Decade:
    def __init__(self, mysteries_count: int, rosary_mysteries: str) -> None:
        self.mystery_count: int = mysteries_count
        self.mystery: str = rosary_mysteries
        self.decade_prayers: List[Prayer] = (
            [Prayer.ANNOUNCE_MYSTERY, Prayer.OUR_FATHER]
            + [Prayer.HAIL_MARY] * 10
            + [
                Prayer.GLORY_BE,
                Prayer.FATIMA_PRAYER,
            ]
        )


class Rosary:
    def __init__(self) -> None:
        self.mysteries: Optional[Mysteries] = None
        self.day_of_week: Optional[DayOfWeek] = None
        self.rosary_start_prayers: List[Prayer] = [
            Prayer.NICENE_CREED,
            Prayer.OUR_FATHER,
            Prayer.HAIL_MARY,
            Prayer.HAIL_MARY,
            Prayer.HAIL_MARY,
            Prayer.GLORY_BE,
            Prayer.FATIMA_PRAYER,
        ]
        self.decades: Optional[List[Decade]] = None
        self.rosary_end_prayers: List[Prayer] = [
            Prayer.ST_MICHAEL,
            Prayer.HAIL_HOLY_QUEEN,
        ]
        self.decade_change: List[int] = [
            len(self.rosary_start_prayers),
            (len(self.rosary_start_prayers) + (1 * 14)),
            (len(self.rosary_start_prayers) + (2 * 14)),
            (len(self.rosary_start_prayers) + (3 * 14)),
            (len(self.rosary_start_prayers) + (4 * 14)),
            (len(self.rosary_start_prayers) + (5 * 14)),
        ]

    def set_day_of_week(self) -> None:
        current_day_index: int = datetime.now().weekday()  # Monday is 0, Sunday is 6
        self.day_of_week = DayOfWeek((current_day_index + 1) % 7)

    def set_decades(self) -> None:
        if self.day_of_week is None:
            raise ValueError("Day of week not set. Call set_day_of_week() first.")
        if (
            self.day_of_week == DayOfWeek.MONDAY
            or self.day_of_week == DayOfWeek.SATURDAY
        ):
            self.mysteries = Mysteries.JOYFUL
            self.decades = [
                Decade(mystery_count, mystery)
                for (mystery_count, mystery) in enumerate(Mysteries.JOYFUL.value)
            ]
        elif (
            self.day_of_week == DayOfWeek.TUESDAY
            or self.day_of_week == DayOfWeek.FRIDAY
        ):
            self.mysteries = Mysteries.SORROWFUL
            self.decades = [
                Decade(mystery_count, mystery)
                for (mystery_count, mystery) in enumerate(Mysteries.SORROWFUL.value)
            ]
        elif (
            self.day_of_week == DayOfWeek.WEDNESDAY
            or self.day_of_week == DayOfWeek.SUNDAY
        ):
            self.mysteries = Mysteries.GLORIOUS
            self.decades = [
                Decade(mystery_count, mystery)
                for (mystery_count, mystery) in enumerate(Mysteries.GLORIOUS.value)
            ]
        elif self.day_of_week == DayOfWeek.THURSDAY:
            self.mysteries = Mysteries.LUMINOUS
            self.decades = [
                Decade(mystery_count, mystery)
                for (mystery_count, mystery) in enumerate(Mysteries.LUMINOUS.value)
            ]

    def get_prayer_from_index(self, index: int) -> Tuple[Optional[str], Optional[str]]:
        prayer: Optional[Prayer] = None
        mysteries: Optional[str] = None
        if self.decades is None:
            raise ValueError("Decades not set. Call set_decades() first.")
        if index < self.decade_change[0]:
            prayer = self.rosary_start_prayers[index]
        elif self.decade_change[0] <= index < self.decade_change[1]:
            prayer = self.decades[0].decade_prayers[index - self.decade_change[0]]
            mysteries = self.decades[0].mystery
        elif self.decade_change[1] <= index < self.decade_change[2]:
            prayer = self.decades[1].decade_prayers[index - self.decade_change[1]]
            mysteries = self.decades[1].mystery
        elif self.decade_change[2] <= index < self.decade_change[3]:
            prayer = self.decades[2].decade_prayers[index - self.decade_change[2]]
            mysteries = self.decades[2].mystery
        elif self.decade_change[3] <= index < self.decade_change[4]:
            prayer = self.decades[3].decade_prayers[index - self.decade_change[3]]
            mysteries = self.decades[3].mystery
        elif self.decade_change[4] <= index < self.decade_change[5]:
            prayer = self.decades[4].decade_prayers[index - self.decade_change[4]]
            mysteries = self.decades[4].mystery
        elif (
            self.decade_change[5]
            <= index
            < (len(self.rosary_end_prayers) + self.decade_change[5])
        ):
            prayer = self.rosary_end_prayers[index - self.decade_change[5]]
        else:
            raise IndexError("Index out of range for rosary prayers.")

        return prayer_enum_to_string(prayer), mysteries


def setup_rosary() -> Rosary:
    rosary: Rosary = Rosary()
    rosary.set_day_of_week()
    rosary.set_decades()
    return rosary


def prayer_enum_to_string(prayer: Prayer) -> str:
    return prayer.name.replace("_", " ").title()
