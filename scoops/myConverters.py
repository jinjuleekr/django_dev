class CodeConverter:
    regex = r'\d{5}'

    # 문자를 받아서, 숫자로 변환한다.
    def to_python(self, value):
        print("to_python 함수", type(value), value)
        return int(value)