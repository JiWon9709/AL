class Person: # 클래스
    def __init__(self, name_param):
        self.name = name_param
        print("hihi", self, self.name)
    def talk(self): # 메소드
        print("안녕하세요 저는 ", self.name, "입니다")

person_1 = Person("유재석")
print(person_1.name)
person_1.talk()
# print(person_1)

person_2 = Person("박명수")
person_2.talk()