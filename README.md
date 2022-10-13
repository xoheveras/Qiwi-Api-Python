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

Функции

```python

def balans()

def pay(summ=0,phonepay=phone)

def generatePay(summ)

def checkPay(comment)

def payment_history_last(phone, token_qiwi, rows_num, next_TxnId, next_TxnDate)

```
