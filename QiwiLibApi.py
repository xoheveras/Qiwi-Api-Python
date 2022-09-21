from SimpleQIWI import *
import random
import requests

# Данные для работы с киви
token_qiwi = ""
p2ptoken = ""
phone = ""

# Связь с Api
api = QApi(token=token_qiwi, phone=phone)
api.start()

# Узнать баланс пользователя
def balans():
    return api.balance

# Перевести деньги на баланс
# @param int summ
# @param string phonepay
# @return True/False
def pay(summ=0,phonepay=phone):
    try:
        api.pay(account=phonepay, amount=summ, comment="Перевод через api")
        print("Перевод прошел успешно")
        return True
    except:
        print("Ошибка при переводе Qiwi")
        return False

# Генерация страницы оплаты с комментарием
# @param int summ
# @return url,comment
def generatePay(summ):

    # Генерация комментария из bits
    comment = str(random.getrandbits(10))+"-"+str(random.getrandbits(10))+"-"+str(random.getrandbits(10))+"-"+str(random.getrandbits(10))

    # Отправка данныех в консоль о успешном создании страницы
    print([f"https://oplata.qiwi.com/create?publicKey={p2ptoken}&amount={summ}&comment={comment}",comment])
    return [f"https://oplata.qiwi.com/create?publicKey={p2ptoken}&amount={summ}&comment={comment}",comment]

# Проверка оплаты через комментарий
# @return True/False
def checkPay(comment):
    state = False
    lastPayments = payment_history_last(phone,token_qiwi,'10','','')
    for i in range(0,len(lastPayments)):
        if lastPayments["data"][0]["status"] == "SUCCESS":
            if lastPayments["data"][0]["comment"] == comment:
                state = True
                break;

    if state:
        return True
    else:
        return False

# История переводов
# @param string my_login
# @param string api_access_token
# @param int rows_num
# @param string next_TxnID
# @param string next_TxnDate
def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate, 'operation': 'IN'}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params = parameters)
    return h.json()
