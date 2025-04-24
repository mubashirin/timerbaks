from pathlib import Path

RATE_PER_HOUR = 12  # ставка в долларах за час

def parse_time_entry(entry: str) -> int:
    """Преобразует строку ЧЧММ в общее количество минут."""
    entry = entry.strip()
    if len(entry) != 4 or not entry.isdigit():
        raise ValueError(f"Неверный формат: {entry}")
    hours = int(entry[:2])
    minutes = int(entry[2:])
    return hours * 60 + minutes

def format_time(total_minutes: int) -> str:
    """Форматирует минуты в строку с днями, часами и минутами."""
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    hours = remaining_minutes // 60
    minutes = remaining_minutes % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} дн")
    if hours > 0 or days > 0:
        parts.append(f"{hours} ч")
    parts.append(f"{minutes} мин")
    
    return " ".join(parts)

def main():
    file_path = Path("time_log.txt")
    total_minutes = 0
    daily_times = []

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                minutes = parse_time_entry(line)
                total_minutes += minutes
                daily_times.append(minutes)

    total_hours = total_minutes / 60
    total_cost = total_hours * RATE_PER_HOUR

    print('  ================================')
    for i, minutes in enumerate(daily_times, 1):
        print(f"         День {i}: {format_time(minutes)}")
    print('  ================================')
    print(f"    Общее время: {format_time(total_minutes)}")
    print(f"      Стоимость: ${total_cost:.2f}")
    print('  ================================')
    print(f'   Отложить 15%: ${(total_cost / 100) * 15:.2f}')
    print(f'        Остаток: ${(total_cost / 100) * 85:.2f}')
    print('  ================================')

if __name__ == "__main__":
    main()
