def parser(input):
    input = list(map(int, "\n".join(input)))
    disk, files, spaces = [], [], []

    for i, num in enumerate(input):
        disk.extend([i // 2 if i % 2 == 0 else -1] * num)
        (files if i % 2 == 0 else spaces).append((len(disk) - 1, num))

    return disk, files, spaces


def p1(input):
    disk, _, _ = input
    n = len(disk)
    i, j = 0, n - 1

    while i < j:
        while i < n and disk[i] != -1:
            i += 1

        while j >= 0 and disk[j] == -1:
            j -= 1

        if i < j:
            disk[i], disk[j] = disk[j], disk[i]
            i += 1
            j -= 1

    return sum([i * num for i, num in enumerate(disk) if num != -1])


def insert(disk, spaces, file_end, file_size):
    file_start = file_end - file_size + 1

    for i, (space_end, space_size) in enumerate(spaces):
        if file_start <= space_end:
            break

        if space_size < file_size:
            continue

        spaces[i] = (space_end, space_size - file_size)
        space_start = space_end - space_size + 1

        for j in range(file_size):
            disk[space_start + j], disk[file_start + j] = (
                disk[file_start + j],
                disk[space_start + j],
            )

        break


def p2(input):
    disk, files, spaces = input

    for file_id in range(len(files) - 1, -1, -1):
        file_end, file_size = files[file_id]
        insert(disk, spaces, file_end, file_size)

    return sum([i * num for i, num in enumerate(disk) if num != -1])
