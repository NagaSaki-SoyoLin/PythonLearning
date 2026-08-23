from abc import ABC, abstractmethod  # 抽象类, 抽象方法
import json


# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 书籍编号
        self.title = title  # 书籍标题
        self.author = author  # 书籍作者
        self.total_num = total_num  # 书籍总数
        self.__available_num = total_num  # 书籍可借阅数量

    def borrow_book(self):  # 借阅书籍
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):  # 归还书籍
        self.__available_num += 1

    def get_available_num(self):  # 获取可借阅数量
        return self.__available_num


"""
抽象类: 是一种只能被继承, 不能被直接实例化的类, 作用就是规定子类必须要实现哪些方法, 强制子类必须遵守统一的代码规范
       Python 中的抽象类, 需要继承 abc 模块中的ABC类 -> ABC: Abstract Base Class
"""


# 会员类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员编号
        self.name = name  # 会员姓名
        self.__password = password  # 会员密码
        self.__borrowed_books = []  # 已借阅书籍列表

    def borrow_book(self, book: Book):  # 借阅书籍
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"{self.name} 已借阅数量已达最大限制, 无法继续借阅!")
            return False

        # 判断当前书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 借阅 {book.title} 成功!")
            return True
        else:
            print(f"{self.name} 借阅 {book.title} 失败, 该书籍已无可借阅数量!")
            return False

    def return_book(self, book: Book):  # 归还书籍
        # 判断当前书籍是否已借阅
        if book in self.__borrowed_books:
            # 归还书籍
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} 归还 {book.title} 成功!")
        else:
            print(f"{self.name} 未借阅 {book.title} 无法归还!")

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    @abstractmethod  # @abstractmethod 装饰器, 用于声明该方法为抽象方法
    def get_max_books(self) -> int:  # 获取最大借阅数量(需要在子类中实现)
        pass


# 普通会员类
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3


# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level  # VIP会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level


# 图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}  # 书籍列表 -> {'book_id': Book}
        self.members = {}  # 会员列表 -> {'member_id': Member}
        self.current_member: Member | None = None  # 当前登录的会员
        # 加载数据(书籍, 会员)
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):  # 加载书籍数据
        # 加载 data/books.json 文件中的书籍数据
        with open('data/books.json', 'r', encoding='utf-8') as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['数量'])
            print("加载书籍数据成功!")

    def load_members_data(self):  # 加载会员数据
        # 加载 data/members.json 文件中的会员数据
        with open('data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
                else:
                    self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'],
                                                             member['会员等级'])
            print("加载会员数据成功!")

    def login(self):  # 登录
        while True:
            print("\n【登录】")
            member_id = input("请输入会员卡号: ")
            password = input("请输入密码: ")

            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("会员卡号不存在, 请重新输入!")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() != password:
                print("密码不正确, 请重新输入!")
                continue
            else:
                self.current_member = member
                print(f"登录成功, 欢迎您, {member.name}!")
                return True

    def borrow_book(self):  # 借阅书籍
        # 1. 展示出当前图书馆的图书列表
        for book in self.books.values():
            print(
                f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}, 总数: {book.total_num}, 可用: {book.get_available_num()}")

        # 2. 输入要借阅的书籍编号
        book_id = input("请输入要借阅的书籍编号: ")
        if book_id not in self.books:
            print("书籍编号不存在, 请重新输入!")
            return
        self.current_member.borrow_book(self.books[book_id])

    def return_book(self):  # 归还书籍
        # 1. 展示出当前会员已借阅的书籍列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("【已借阅的书籍列表:】")
        for book in borrowed_books:
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}")

        # 2. 输入要归还的书籍编号, 并归还书籍
        book_id = input("请输入要归还的书籍编号: ")
        if book_id not in self.books:
            print("书籍编号不存在!")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):  # 查看已借阅的书籍
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已借阅的书籍列表:】")
            for book in borrowed_books:
                print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}")
        else:
            print("您暂未借阅任何书籍!")

    def run(self):
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请输入要执行的操作(1~4): ")
                match choice:
                    case '1':
                        self.borrow_book()
                    case '2':
                        self.return_book()
                    case '3':
                        self.show_borrowed_books()
                    case '4':
                        print("退出系统成功, Bye!")
                        break
                    case _:
                        print("输入错误, 请重新输入!")


if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()
