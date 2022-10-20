from abc import ABC, abstractmethod


class IMessage(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass


class Email(IMessage):
    def __init__(self, content, owner_email):
        """이메일은 그 내용과 보낸 사람의 이메일 주소를 인스턴스 변수로 가짐"""
        self._content = content
        self.owner_email = owner_email

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """이메일 내용 수정 메소드"""
        self._content = self.owner_email + "님의 메일\n" + new_content

    def send(self, destination):
        """이메일 전송 메소드"""
        print("{}에서 {}로 이메일 전송!\n내용: {}").format(
            self.owner_email, destination, self._content
        )
        return True


class TextMessage(IMessage):
    def __init__(self, content):
        """문자 메시지는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """문자 메시지 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """문자 메시지 전송 메소드"""
        print("{}로 문자 메시지 전송!\n내용: {}").format(destination, self._content)


class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IMessage):
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)


class Memo(IMessage):
    def __init__(self, content):
        """메모는 그 내용은 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """메모 내용 수정 메소드"""
        self._content = new_content

    # 메모의 경우 누구에게 전송할 필요가 없으므로 send 메소드가 필요없음.
    # 하지만 Imessage 클래스를 상속받았기 때문에 반드시 send 메소드를 오버라이딩 해야하는 상황이 생김 -> 사용하질 않은 메소드에 의존할 것을 강요하는 상황

    def send(self, destination):
        """메모는 전송할 수 없음"""
        print("메모는 아무 데도 보낼 수 없습니다!")
        return False

    # 굳이 send를 만들어줬음
    # 이와 같이 너무 많은 메소드를 한번에 가지고 있는 인터페이스를 '뚱뚱한 인터페이스'라고 함
    # 더 작은 인터페이스, 즉 역할 인터페이스로 바꿔야함


email = Email("안녕 잘 지내니? 오랜만이다!", "young@codeit.kr")
text_message = TextMessage("내일 시간 가능? 한 1시쯤 만나자")
memo = Memo("장보기")

text_reader = TextReader()
text_reader.add_text(email)
text_reader.add_text(text_message)
text_reader.add_text(memo)
text_reader.read_all_texts()
