# Пример наследования реализации
# в данном случае два не связанных между собой в предметной области класса 
# MsgSecurityChallenge  - challenge для генерации кода проверки подлинности сообщения
# RandomGeneratorSeed   - seed для инициализации генератора случайных чисел. 
# техничеки обе сущности в нашей реализации просто представляют собой  массив байт, 
# однако в коде нам будет удобнее и нагляднее различать эти типы. Поэтому здесь применям
# наследование реализации  
class MsgSecurityChallenge(bytes):
    pass

class RandomGeneratorSeed(bytes):
    pass

challenge = MsgSecurityChallenge(b"\x00\x00")
seed = RandomGeneratorSeed(b"\x01\x01")

print(challenge)
print(seed)

# Пример льготного наследования
# В данном случае мы различаем типы строк 
# MultibyteStr и WideCharStr для того, чтобы эмулировать поведение 
# WinApi функции MultibyteToWideChar 
# в качестве дополнительной функциональности наследуемым классам можно 
# добавить валидацию строк, которые содержатся внутри них или передаются при создании

class MultibyteStr(str):
    pass

class WideCharStr(bytes):
    pass

class CodePage:
    pass

def emulate_MultibyteToWideChar(mbStr:MultibyteStr, codePage:CodePage) -> WideCharStr:
    pass
