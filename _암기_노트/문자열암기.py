# ============================================================
# 파이썬 문자열 필수 정리 - 코딩테스트 대비
# ============================================================


# ============================================================
# 1. 기본 조작
# ============================================================
s = "Hello World"

print(s.upper())          # "HELLO WORLD"
print(s.lower())          # "hello world"
print(s.swapcase())       # "hELLO wORLD"

print(s.strip())          # 양쪽 공백 제거
print(s.lstrip())         # 왼쪽 공백 제거
print(s.rstrip())         # 오른쪽 공백 제거

print(len(s))             # 11


# ============================================================
# 2. 탐색
# ============================================================
s = "hello"

print(s.find("l"))        # 2 (없으면 -1)
print(s.index("l"))       # 2 (없으면 오류)
print(s.count("l"))       # 2
print(s.startswith("he")) # True
print(s.endswith("lo"))   # True
print("l" in s)           # True


# ============================================================
# 3. 변환
# ============================================================
s = "hello world"

print(s.split())          # ["hello", "world"]
print(s.split("o"))       # ["hell", " w", "rld"]

words = ["hello", "world"]
print(" ".join(words))    # "hello world"
print("-".join(words))    # "hello-world"

print(s.replace("l", "r")) # "herro worrd"


# ============================================================
# 4. 슬라이싱
# ============================================================
s = "hello"

print(s[0])               # "h"
print(s[-1])              # "o"
print(s[1:3])             # "el"
print(s[:3])              # "hel"
print(s[2:])              # "llo"
print(s[::-1])            # "olleh" (뒤집기)
print(s[::2])             # "hlo"  (2칸씩)


# ============================================================
# 5. 문자 판별
# ============================================================
s = "Hello123"

print(s.isalpha())        # False (문자만 있으면 True)
print(s.isdigit())        # False (숫자만 있으면 True)
print(s.isalnum())        # True  (문자+숫자면 True)
print(s.isspace())        # False (공백만 있으면 True)
print(s.isupper())        # False (전부 대문자면 True)
print(s.islower())        # False (전부 소문자면 True)


# ============================================================
# 6. 아스키코드 변환
# ============================================================
print(ord("A"))           # 65
print(ord("a"))           # 97
print(ord("0"))           # 48

print(chr(65))            # "A"
print(chr(97))            # "a"

# 알파벳 순서 구할 때
print(ord("D") - ord("A")) # 3 (0부터 시작)


# ============================================================
# 7. 문자열 <-> 리스트
# ============================================================
s = "hello"

print(list(s))                        # ["h","e","l","l","o"]
print("".join(["h","e","l","l","o"])) # "hello"
print(sorted(s))                      # ["e","h","l","l","o"]
print("".join(sorted(s)))             # "ehllo"


# ============================================================
# 8. 포매팅
# ============================================================
n = 42
name = "윤서"

print(f"안녕 {name}, 숫자는 {n}")  # 안녕 윤서, 숫자는 42
print(f"{n:05d}")                   # "00042" (5자리, 빈칸 0으로)
print(f"{n:>5}")                    # "   42" (오른쪽 정렬)
print(f"{n:<5}")                    # "42   " (왼쪽 정렬)


# ============================================================
# 9. 자주 쓰는 패턴
# ============================================================
s = "hello"

# 팰린드롬 확인
print(s == s[::-1])                              # False

# 알파벳만 추출
result = "".join(c for c in s if c.isalpha())
print(result)                                    # "hello"

# 숫자만 추출
s2 = "h3ll0"
result = "".join(c for c in s2 if c.isdigit())
print(result)                                    # "30"

# 문자 빈도 세기
from collections import Counter
print(Counter("hello"))   # {'l': 2, 'h': 1, 'e': 1, 'o': 1}

# 알파벳 전체
import string
print(string.ascii_lowercase)  # "abcdefghijklmnopqrstuvwxyz"
print(string.ascii_uppercase)  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string.digits)           # "0123456789"


# ============================================================
# 10. 주의할 점 - 문자열은 불변
# ============================================================
s = "hello"

# s[0] = "H"  → 오류! 문자열은 직접 수정 불가

# 수정하려면 리스트로 변환 후 다시 합치기
s = list(s)
s[0] = "H"
s = "".join(s)
print(s)      # "Hello"


# ============================================================
# 우선순위 요약 (코테 출현 빈도 높은 순)
# ============================================================
# 1. split / join
# 2. 슬라이싱 (특히 [::-1] 뒤집기)
# 3. replace
# 4. Counter
# 5. ord / chr
# 6. isalpha / isdigit / isalnum
# 7. find / in
# 8. startswith / endswith
# 9. strip
# 10. 포매팅 (f-string)