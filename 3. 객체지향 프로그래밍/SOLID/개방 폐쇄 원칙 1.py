class AppleKeyboard:
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def set_keyboard_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_keyboard_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class SamsungKeyboard:
    """삼성 키보드 클래스"""

    def __init__(self):
        """키보드 인풋"""
        self.user_input = ""

    def save_user_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def give_user_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_keyboard_input()


keyboard_manager = KeyboardManager()
samsung_keyboard = SamsungKeyboard()
keyboard_manager.connect_to_keyboard(samsung_keyboard)
samsung_keyboard.save_user_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

# get_keyboard_input이 send_keyboard_input을 가지고 오기 때문에 삼성키보드의 경우 호환되지 않음.
# 키보드가 추가되면 코드를 바꿔줘야 하기 때문에 개방 폐쇄 원칙에 어긋난다고 볼 수 있음
