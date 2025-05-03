from enum import Enum
from datetime import datetime
from typing import List, Optional


class DayOfWeek(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Rosary:
    def __init__(self) -> None:
        self.nicene_creed: bool = False
        self.our_father: bool = False
        self.hail_mary_track: List[bool] = [False] * 3
        self.glory_be: bool = False
        self.fatima_prayer: bool = False
        self.decade_track: List[bool] = [False] * 5
        self.hail_holy_queen: bool = False
        self.rosary_mysteries: List[List[str]] = [
            [
                "The Annunciation",
                "The Visitation",
                "The Nativity",
                "The Presentation",
                "The Finding in the Temple",
            ],  # Joyful Mysteries
            [
                "The Agony in the Garden",
                "The Scourging at the Pillar",
                "The Crowning with Thorns",
                "The Carrying of the Cross",
                "The Crucifixion",
            ],  # Sorrowful Mysteries
            [
                "The Resurrection",
                "The Ascension",
                "The Descent of the Holy Spirit",
                "The Assumption",
                "The Coronation of Mary",
            ],  # Glorious Mysteries
            [
                "The Baptism of Jesus",
                "The Wedding at Cana",
                "The Proclamation of the Kingdom",
                "The Transfiguration",
                "The Institution of the Eucharist",
            ],  # Luminous Mysteries
        ]
        self.hail_holy_queen: bool = False
        self.day_of_week: Optional[DayOfWeek] = None
        self.prayer_elements = [
            self.nicene_creed,
            self.our_father,
            *self.hail_mary_track,
            self.glory_be,
            self.fatima_prayer,
            *self.decade_track,
            self.hail_holy_queen,
        ]
        self.decades: Optional[List["Decade"]] = None

    def set_day_of_week(self) -> None:
        current_day_index: int = datetime.now().weekday()  # Monday is 0, Sunday is 6
        self.day_of_week = DayOfWeek((current_day_index + 1) % 7)

    def set_decades(self) -> None:
        if (
            self.day_of_week == DayOfWeek.MONDAY
            or self.day_of_week == DayOfWeek.SATURDAY
        ):
            self.decades = [Decade(mystery) for mystery in self.rosary_mysteries[0]]
        elif (
            self.day_of_week == DayOfWeek.TUESDAY
            or self.day_of_week == DayOfWeek.FRIDAY
        ):
            self.decades = [Decade(mystery) for mystery in self.rosary_mysteries[1]]
        elif (
            self.day_of_week == DayOfWeek.WEDNESDAY
            or self.day_of_week == DayOfWeek.SUNDAY
        ):
            self.decades = [Decade(mystery) for mystery in self.rosary_mysteries[2]]
        elif self.day_of_week == DayOfWeek.THURSDAY:
            self.decades = [Decade(mystery) for mystery in self.rosary_mysteries[3]]

    def get_prayer_start_finish(self) -> int:
        prayer_count: int = 0
        if self.nicene_creed:
            prayer_count += 1
        if self.our_father:
            prayer_count += 1
        for hail_mary in self.hail_mary_track:
            if hail_mary:
                prayer_count += 1
        if self.glory_be:
            prayer_count += 1
        if self.fatima_prayer:
            prayer_count += 1
        for decade in self.decade_track:
            if decade:
                prayer_count += 1
        if self.hail_holy_queen:
            prayer_count += 1
        return prayer_count


class Decade:
    def __init__(self, rosary_mysteries: str) -> None:
        self.mystery: str = rosary_mysteries
        self.announce_mystery: bool = False
        self.our_father: bool = False
        self.hail_mary_count: List[bool] = [False] * 10
        self.glory_be: bool = False
        self.fatima_prayer: bool = False


def setup_rosary() -> Rosary:
    rosary: Rosary = Rosary()
    rosary.set_day_of_week()
    rosary.set_decades()
    return rosary


def teardown_rosary() -> Rosary:
    rosary: Rosary = Rosary()
    return rosary
