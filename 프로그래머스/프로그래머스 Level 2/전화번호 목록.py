def solution(phone_book):
    for i, phone in enumerate(phone_book):
        for j in range(len(phone_book)):
            if i != j and phone_book[j].startswith(phone):
                print(phone_book[j], phone)
                return False
    return True


# 아래는 테스트 출력문
print(solution(["119", "97674223", "1195524421"]))
