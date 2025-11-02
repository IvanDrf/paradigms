type Version = int | str


class OS:
    __slots__ = ('id', 'name', 'version')

    def __init__(self, id: int, name: str, version: Version) -> None:
        self.id: int = id
        self.name: str = name
        self.version: Version = version


class Computer:
    __slots__ = ('id', 'name', 'processor_name', 'os_id')

    def __init__(self, id: int, name: str, processor_name: str, os_id: int) -> None:
        self.id: int = id
        self.name: str = name
        self.processor_name: str = processor_name
        self.os_id: int = os_id


class Server:
    __slots__ = ('os_id', 'computer_id')

    def __init__(self, os_id: int, computer_id: int) -> None:
        self.os_id: int = os_id
        self.computer_id: int = computer_id


operating_systems: list[OS] = [
    OS(1, 'Linux', 'Alpine'),
    OS(2, 'Linux', 'Arch'),
    OS(3, 'Linux', 'Fedora'),
    OS(4, 'Windows', 11),
    OS(5, 'Windows', 'XP'),
    OS(6, 'Windows', 10)
]

computers: list[Computer] = [
    Computer(1, 'compA', 'Intel Core i5-3770', 1),
    Computer(2, 'compB', 'Intel Core i7-3770 ', 3),
    Computer(3, 'compC', 'Intel Core i5-3470', 4),
    Computer(4, 'compD', 'Intel Core i7-3770', 6),
    Computer(5, 'compE', 'Intel Xeon Silver', 2)
]

# на одном компьютере может быть несколько ос
servers: list[Server] = [
    Server(1, 1),
    Server(1, 2),
    Server(2, 3),
    Server(3, 4),
    Server(3, 5),
    Server(4, 5),
    Server(4, 2),
    Server(6, 4),
    Server(5, 2),
    Server(6, 3),
]


def main() -> None:
    # cвязь один ко многим
    one_to_many: list[tuple[str, str, str]] = [
        (comp.name, comp.processor_name, os.name)
        for os in operating_systems
        for comp in computers
        if comp.os_id == os.id
    ]

    temp: list[tuple[str, int, int]] = [
        (os.name, s.os_id, s.computer_id)
        for os in operating_systems
        for s in servers
        if os.id == s.os_id
    ]

    # связь многие ко многим
    many_to_many: list[tuple[str, str, str]] = [
        (comp.name, comp.processor_name, os_name)
        for os_name, _, comp_id in temp
        for comp in computers if comp.id == comp_id
    ]

    print('Задание 1')
    first_res: list[tuple[str, str]] = find_comps_with_i7(one_to_many)
    print('Компьютеры с процессорами i7:')
    for comp_name, os_name in first_res:
        print(f'{comp_name} - {os_name}')
    print()

    print('Задание 2')
    second_res: list[tuple[str, str, str]
                     ] = find_min_linux_and_windows(one_to_many)
    print('Операционные системы с минимальным именем компьютера:')
    for os_name, comp_name, processor in second_res:
        print(f'{os_name}: {comp_name} - {processor}')
    print()

    print('Задание 3')
    third_res = sorted(many_to_many, key=lambda x: (x[2], x[0]))
    print('Все связанные компьютеры и операционные системы:')
    for comp_name, processor, os_name in third_res:
        print(f'{os_name}: {comp_name} - {processor}')


def find_comps_with_i7(one_to_many: list[tuple[str, str, str]]) -> list[tuple[str, str]]:
    res: list[tuple[str, str]] = [(comp_name, os_name) for comp_name, processor_name, os_name in one_to_many
                                  if comp_name.startswith('comp') and 'i7' in processor_name]

    return res


def find_min_linux_and_windows(one_to_many: list[tuple[str, str, str]]) -> list[tuple[str, str, str]]:
    os_computers_dict: dict['str', list[tuple[str, str]]] = {}

    for comp_name, processor_name, os_name in one_to_many:
        if os_name not in os_computers_dict:
            os_computers_dict[os_name] = []

        os_computers_dict[os_name].append((comp_name, processor_name))

    res: list[tuple[str, str, str]] = []
    for os_name, comp_list in os_computers_dict.items():
        min_comp = min(comp_list, key=lambda x: x[0])
        res.append((os_name, min_comp[0], min_comp[1]))

    return sorted(res, key=lambda x: x[0])


if __name__ == '__main__':
    main()
