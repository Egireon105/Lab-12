# ==================== ЗАДАНИЕ 5 ====================
class Streamer:
    def __init__(self, nickname, subscribers, donates):
        self.nickname = nickname
        self.subscribers = subscribers
        self.donates = donates

    def to_line(self):
        """Превращаем объект в строку формата: ник;подписчики;донат1,донат2,..."""
        donates_str = ",".join(str(d) for d in self.donates)
        return f"{self.nickname};{self.subscribers};{donates_str}"

    def __str__(self):
        total = sum(self.donates) if self.donates else 0
        avg = total / len(self.donates) if self.donates else 0
        return (f"Стример: {self.nickname}\n"
                f"Подписчики: {self.subscribers}\n"
                f"Всего донатов: {total}\n"
                f"Средний донат: {avg}")


def streamer_from_line(line):
    """Создаём объект Streamer из строки."""
    nickname, subscribers, donates_str = line.strip().split(";")
    if donates_str == "":
        donates = []
    else:
        donates = [int(d) for d in donates_str.split(",")]
    return Streamer(nickname, int(subscribers), donates)


# ==================== ЗАДАНИЕ 1 ====================
def task1():
    print("=== Задание 1: деление ===")
    try:
        a = int(input("Введи первое число: "))
        b = int(input("Введи второе число: "))
        result = a / b
        print("Результат:", result)
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    print()


# ==================== ЗАДАНИЕ 2 ====================
def task2():
    print("=== Задание 2: 10 / x + finally ===")
    try:
        x = int(input("Введи число: "))
        print("Результат:", 10 / x)
    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    else:
        print("Всё прошло хорошо.")
    finally:
        print("Программа завершена.")
    print()


# ==================== ЗАДАНИЕ 3 ====================
def task3():
    print("=== Задание 3: запись и чтение hello.txt ===")
    with open("hello.txt", "w", encoding="utf-8") as f:
        f.write("Привет\n")
        f.write("Как дела?\n")
        f.write("Пока\n")

    with open("hello.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    print(lines)
    real_lines = [x for x in lines if x != ""]
    print("Строк в файле:", len(real_lines))
    print()


# ==================== ЗАДАНИЕ 4 ====================
def task4():
    print("=== Задание 4: дозапись в hello.txt ===")
    with open("hello.txt", "a", encoding="utf-8") as f:
        f.write("Ещё одна строка\n")

    with open("hello.txt", "r", encoding="utf-8") as f:
        print(f.read())


# ==================== ЗАДАНИЕ 6 ====================
def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")


def load_from_file(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                objects.append(streamer_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return objects


# ==================== ЗАДАНИЕ 7 ====================
def task7():
    print("=== Задание 7: полная программа ===")
    streamers = [
        Streamer("GolubKin", 1200, [200, 150, 300]),
        Streamer("FrostMiron", 800, [100, 250]),
        Streamer("Egireon105", 5000, [500, 1000, 750, 250])
    ]

    save_to_file(streamers, "data.txt")
    print("Стримеры сохранены в data.txt\n")

    streamers = []

    loaded = load_from_file("data.txt")
    for s in loaded:
        print(s)
        print("---")


# ==================== ЗАДАНИЕ 8 (бонус) ====================
class Player:
    def __init__(self, name, points=0, level=1):
        self.name = name
        self.points = points
        self.level = level

    def to_line(self):
        return f"{self.name};{self.points};{self.level}"


def player_from_line(line):
    name, points, level = line.strip().split(";")
    return Player(name, int(points), int(level))


def save_player(player):
    with open("player.txt", "w", encoding="utf-8") as f:
        f.write(player.to_line())


def load_player():
    try:
        with open("player.txt", "r", encoding="utf-8") as f:
            return player_from_line(f.read())
    except FileNotFoundError:
        name = input("Как тебя зовут, игрок? ")
        return Player(name)


def task8():
    print("=== Задание 8: мини-игра ===")
    player = load_player()
    print(f"С возвращением, {player.name}! Очки: {player.points}, уровень: {player.level}")

    while True:
        answer = input("Играем ещё раунд? (да/нет): ").strip().lower()
        if answer == "нет":
            print("Пока!")
            break
        player.points += 10
        if player.points % 50 == 0:
            player.level += 1
            print(f"🎉 Новый уровень: {player.level}!")
        save_player(player)
        print(f"Очки сохранены: {player.points}")
    print()


# ==================== ЗАДАНИЕ 9 (бонус) ====================
def task9():
    print("=== Задание 9: чтение файла с обработкой ошибок ===")
    filename = input("Введи имя файла: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("❌ Файл не найден.")
    except PermissionError:
        print("❌ Нет прав на чтение файла.")
    except UnicodeDecodeError:
        print("❌ Ошибка кодировки (файл не в UTF-8).")
    print()


# ==================== ЗАДАНИЕ 10 (бонус) ====================
def save_custom(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            # формат: ник|подписчики|донат1,донат2,...
            donates_str = ",".join(str(d) for d in obj.donates)
            f.write(f"{obj.nickname}|{obj.subscribers}|{donates_str}\n")


def load_custom(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                nickname = parts[0]
                subscribers = int(parts[1])
                donates = [int(d) for d in parts[2].split(",")] if parts[2] else []
                objects.append(Streamer(nickname, subscribers, donates))
    except FileNotFoundError:
        print("Файл не найден.")
    return objects


def task10():
    print("=== Задание 10: свой формат ===")
    streamers = [Streamer("TestUser", 100, [50, 75])]
    save_custom(streamers, "custom.txt")
    loaded = load_custom("custom.txt")
    for s in loaded:
        print(s)
    print()