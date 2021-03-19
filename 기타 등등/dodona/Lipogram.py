# https://dodona.ugent.be/en/activities/1815535490/

def occurrences(file_name: str) -> dict:
    result = dict()
    with open(file_name, "r") as f:
        for ch in f.read():
            if ch.isalpha():
                ch = ch.lower()
                result[ch] = (result[ch]+1 if ch in result.keys() else 1)

    return result       # 함수의 반환값


def missing_letters(file_name: str) -> set:
    result = set(map(lambda x: chr(x), range(ord("a"), ord("z")+1)))
    with open(file_name, "r") as f:
        for ch in f.read():
            if ch.lower() in result:
                result.remove(ch.lower())

    return result


def make_lipogram(letters, source_file, output_file=""):
    result = ""
    letter_list = list(map(lambda x: x.lower(), letters))
    with open(source_file, "r") as f:
        for line in f.readlines():
            for ch in line:
                if ch.lower() not in letter_list:
                    result += ch

    if output_file:
        with open(output_file, "w") as f:
            f.write(result)
    else:
        for line in result.split("\n")[:-1]:
            print(line)
        print(result.split("\n")[-1], end="")


if __name__ == '__main__':
    print(occurrences("lipo.txt"))
    print(missing_letters("lipo.txt"))
    make_lipogram("aeiou", "lipo.txt")
    make_lipogram(["a", "e", "i", "o", "u"], "lipo.txt")
    make_lipogram("aeiou", "lipo.txt", "copy.txt")
