import re


def solution(new_id):
    """
    정규 표현식만 기억하면 풀 수 있다! 심지어 정규표현식 함수는 re.sub() 만 써도 충분하다. (문자열의 replace()와 비슷)
    그리고 [^(a|b|c)] 하면 (와 )도 문자로 인식되서 필터링되니, [^a|b|c] 해야 된다.
    """
    new_id = new_id.lower()
    new_id = re.sub("[^a-z|0-9|\-|\_|\.]", "", new_id)
    new_id = re.sub("\.+", ".", new_id)
    new_id = new_id.strip(".")
    new_id = new_id[:15] if new_id else "a"
    new_id = new_id.rstrip(".")
    new_id = (new_id+new_id[-1]*2)[:3] if len(new_id) < 3 else new_id
    return new_id


# 테스트 코드
print(solution("-_.~!@#$%^&*()=+[{]}:?,<>/._-"))
