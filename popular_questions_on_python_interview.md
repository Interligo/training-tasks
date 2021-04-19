## Вопросы по Python для подготовки к собеседованиям.

> Разумеется, на мой взгляд.

### 1. SOLID - это набор принципов проектирования для разработки программного обеспечения при помощи ООП.

* **Single Responsibility Principle** (принцип единственной обязанности):

Принцип единственной обязанности требует того, чтобы **один класс выполнял только одну работу**.

Класс User отвечает за свойства пользователя, в то время как класс UserDB отвечает за управление базой данных пользователя. 

```python
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass
```
* **Open-Closed Principle** (принцип открытости/закрытости):

Программные сущности (**классы, модули, функции**) должны быть **открыты для расширения, но не модификации**.

Класс Discount отвечает за предоставление скидки покупателям. Если необходимо удвоить скидку для VIP покупателей, то, исходя из принципа открытости/закрытости, необходимо написать класс VIPDiscount, который делает это расширяя, но не изменяя класс Discount. 

```python
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
      
    def get_discount(self):
      return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2
```

* **Liskov Substitution Principle** (принцип подстановки Лисков):

Данный принцип соответствует одному из базовых принципов ООП — **полиморфизму**.

Клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними, и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает, что **клиент полностью изолирован и не подозревает об изменениях в иерархии классов**.

Проще говоря, это значит, что подкласс должен соответствовать родительскому классу или супер классу.

```python
class User():
  def __init__(self, color, board):
    create_pieces()
    self.color = color
    self.board = board
    
  def move(self, piece:Piece, position:int):
      piece.move(position)
      chessmate_check()
      
      
  board = ChessBoard()
  user_white = User("white", board)
  user_black = User("black", board)
  pieces = user_white.pieces
  horse = helper.get_horse(user_white, 1)
  user.move(horse)
```

* **Interface Segregation Principle** (принцип разделения интерфейсов):

**Клиенты не должны зависеть от интерфейсов, которые они не используют**. Этот принцип устраняет недостатки реализации больших интерфейсов. 

Таким образом, единая реализация для всех общих методов между интерфейсами приведет к меньшей зависимости и более легкому тестированию.

```python
class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
```

* **Dependecy Inversion Principle** (принцип инверсии зависимостей):

**Зависимость должна быть от абстракций, а не от конкретики**. Модули верхних уровней не должны зависеть от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

```python
class AuthenticationForUser():
  def __init__(self, connector:Connector):
		self.connection = connector.connect()
	
	def authenticate(self, credentials):
		pass
    
	def is_authenticated(self):
		pass	
    
	def last_login(self):
		pass


class AnonymousAuth(AuthenticationForUser):
	pass


class GithubAuth(AuthenticationForUser):
	def last_login(self):
		pass


class FacebookAuth(AuthenticationForUser):
	pass


class Permissions()
	def __init__(self, auth: AuthenticationForUser)
		self.auth = auth
		
	def has_permissions():
		pass
		
    
class IsLoggedInPermissions (Permissions):
	def last_login():
		return auth.last_log
```

### 2. REST (Representational State Transfer).

REST устанавливает руководящие принципы проектирования API (всего их 5):

* Uniform interface (единый интерфейс):

API должен иметь **только один логичный URL** и все остальные API должны быть сформированы аналогичным образом. Представление API должно соответствовать соглашению об именах, формате ссылок и данных (XML, JSON).

* Client–server (клиент-сервер):

Клиентские и серверные API должны иметь возможность развиваться отдельно, **независимо друг от друга**. KISS :)

* Stateless (без сохранения состояния):

Сервер не должен ничего хранить о последнем запросе. Каждый запрос должен рассматриваться как новый. **Ни сеанса, ни истории**.

Каждый запрос от клиента должен содержать всю информацию, включая данные для аутентификации и авторизации.

* Cacheable (кэшируемость):

Кэширование - это **круто**. Всё, что только возможно, кэшируется. Кэширование может быть реализовано на сервере или на стороне клиента.

* Layered system (многоуровневая система):

REST позволяет использовать **многоуровневую системную архитектуру**, в которой API-интерфейсы развертываются на сервере A, а данные хранятся на сервере B, а запросы аутентифицируются, например, на сервере C.

> P.S. Тем не менее, время от времени, можно нарушить одно или два ограничения. Это всё ещё будет RESTful API, но не «по-настоящему RESTful».
