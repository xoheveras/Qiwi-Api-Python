# Qiwi API LIB

<p style="color:red;">!!! Qiwi API LIB - является оберткой для SimpleQiwi (Мы не несем ответственности за изменения кода в используемых библиотеках)</p>
<h3>Работа с библиотекой</h3>

Установка SimpleQiwi
```curl
pip install SimpleQiwi

```

Данные для авторизации

```python 

token_qiwi = ""
p2ptoken = ""
phone = ""

```

<h1>Функции</h1>


Получить данные о балансе
```python

def balans() -> str

```

Перевести средства
```python

def pay(summ=0,phonepay=phone) -> none

```

Сгенерировать страницу оплаты с определенной суммой и комментарием
```python

def generatePay(summ) -> str,str

```

Используя комментарий отследить оплату
```python

def checkPay(comment) -> bool

```

Получить список последних платежей кошелька (Используется при проверке оплаты)
```python

def payment_history_last(phone, token_qiwi, rows_num, next_TxnId, next_TxnDate) -> json

```
