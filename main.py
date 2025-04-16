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

def main():
    file_path = Path("time_log.txt")
    total_minutes = 0

    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                total_minutes += parse_time_entry(line)

    total_hours = total_minutes / 60
    total_cost = total_hours * RATE_PER_HOUR

    print('  ========================')
    print(f"    Общее время: {int(total_minutes // 60)}:{int(total_minutes % 60)}")
    # print(f"    Общее количество часов: {total_hours:.2f}")
    print(f"      Стоимость: ${total_cost:.2f}")
    print('  ========================')
    print(f'   Отложить 15%: ${(total_cost / 100) * 15:.2f}')
    print(f'        Остаток: ${(total_cost / 100) * 85:.2f}')
    print('  ========================')

if __name__ == "__main__":
    main()
