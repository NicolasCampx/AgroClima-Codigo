from dataclasses import dataclass
from math import isfinite
from statistics import pstdev


SENSOR_COLUMNS = {
    "soil_moisture": 1,
    "air_humidity": 3,
    "air_temp": 2,
    "light_pct": 4,
}


@dataclass(frozen=True)
class VariableStatistics:
    count: int
    standard_deviation: float | None


@dataclass(frozen=True)
class PeriodStatistics:
    reading_count: int
    variables: dict[str, VariableStatistics]


def valid_number(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        return None
    return number if isfinite(number) else None


def population_statistics(values):
    numbers = [
        number for value in values if (number := valid_number(value)) is not None
    ]

    return VariableStatistics(
        len(numbers), pstdev(numbers) if len(numbers) >= 2 else None
    )


def calculate_statistics(rows):
    values = {key: [] for key in SENSOR_COLUMNS}
    count = 0
    for row in rows:
        count += 1
        for key, column in SENSOR_COLUMNS.items():
            values[key].append(row[column])
    return PeriodStatistics(
        count, {key: population_statistics(data) for key, data in values.items()}
    )


def interpret_variability(deviation, temperature=False):
    if deviation is None:
        return "Dados insuficientes", "neutral"
    low, high = (1, 2.5) if temperature else (3, 7)
    if deviation < low:
        return ("Temperatura estável" if temperature else "Baixa variação"), "ok"
    if deviation <= high:
        return "Variação moderada", "warning"
    return ("Alta variação térmica" if temperature else "Alta variação"), "info"
