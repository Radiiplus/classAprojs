import uuid

acc = {}
session = {
    "accid": None,
    "sessid": None
}

def genid():
    return uuid.uuid4().hex[:16]

def valaccid(accid):
    return accid in acc

def create(username, password):
    if userexist(username):
        return True
    
    check = toughpass(password)
    if check != "Password is strong":
        return check
    
    accid = genid()
    acc[accid] = {
        "id": accid,
        "username": username,
        "password": password,
        "balance": 0,
        "history": []
    }
    return f"Your account has been created successfully @{username} with account ID: {accid}"

def toughpass(password):
    try:
        if len(password) < 4:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        return "Password is strong"
    except ValueError as e:
        return str(e)

def deposit(amount):
    account, error = actsess()
    if error:
        return error
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        account['balance'] += amount
        account['history'].append(f"Deposited {amount}")
        return f"Deposited {amount} successfully"
    except ValueError as e:
        return str(e)

def withdraw(amount):
    account, error = actsess()
    if error:
        return error
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if account['balance'] < amount:
            raise ValueError("Insufficient balance")
        account['balance'] -= amount
        account['history'].append(f"Withdrew {amount}")
        return f"Withdrew {amount} successfully"
    except ValueError as e:
        return str(e)
    
def transfer(receiver, amount):
    account, error = actsess()
    if error:
        return error

    recid = findacc(receiver)
    if not recid:
        return "Receiver does not exist"

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if account['balance'] < amount:
            raise ValueError("Insufficient balance")
        account['balance'] -= amount
        acc[recid]['balance'] += amount
        account['history'].append(f"Transferred {amount} to {receiver}")
        return f"Transfer sucessful"
    except ValueError as e:
        return str(e)

def balance():
    account, error = actsess()
    if error:
        return error
    return f"Your balance is {account['balance']}"

def history():
    account, error = actsess()
    if error:
        return error
    return account['history']

def auth(username, password):
    for accid, details in acc.items():
        if details['username'] == username and details['password'] == password:
            session['accid'] = accid
            session['sessid'] = genid()
            return f"Authentication successful for account ID: {accid} and session ID: {session['sessid']}"
    return "Authentication failed"


def logout():
    if not session.get('accid'):
        return "No active session"

    session['accid'] = None
    session['sessid'] = None
    return "Logged out successfully"


def findacc(receiver):
    if receiver in acc:
        return receiver

    for accid, details in acc.items():
        if details['username'] == receiver:
            return accid

    return None

def actsess():
    accid = session.get('accid')
    if not accid:
        return None, "No active session"
    if accid not in acc:
        return None, "Invalid account ID in session"
    return acc[accid], None


def userexist(username):
    for data in acc.values():
        if data['username'] == username:
            return True
    return False
