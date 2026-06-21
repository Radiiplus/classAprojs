from datetime import datetime

balance = 100000

market = {
    "GOLD": {
        "name": "GOLD",
        "price": 200,
        "quantity": 500
    },
    "OIL": {
        "name": "OIL",
        "price": 50,
        "quantity": 1000
    },
    "APPLE": {
        "name": "APPLE",
        "price": 180,
        "quantity": 300
    },
    "TESLA": {
        "name": "TESLA",
        "price": 300,
        "quantity": 250
    },
    "BITCOIN": {
        "name": "BITCOIN",
        "price": 65000,
        "quantity": 20
    }
}

portfolio = {}
history = []


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def findasset(asset):
    asset = asset.upper()

    if asset in market:
        return asset

    for code, details in market.items():
        if details['name'].upper() == asset:
            return code

    return None


def viewmarket():
    rows = []

    for code, details in market.items():
        rows.append(
            f"{code}: ${details['price']} | Available: {details['quantity']}"
        )

    return "\n".join(rows)


def changeprice(assetid, action, quantity):
    oldprice = market[assetid]['price']
    change = min(quantity * 0.001, 0.2)

    if action == "buy":
        newprice = oldprice * (1 + change)
    else:
        newprice = oldprice * (1 - change)

    market[assetid]['price'] = round(max(newprice, 1), 2)
    return oldprice, market[assetid]['price']


def buy(asset, quantity):
    global balance

    assetid = findasset(asset)
    if not assetid:
        return "Asset does not exist"

    try:
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        details = market[assetid]

        if details['quantity'] < quantity:
            raise ValueError("Not enough asset quantity available")

        price = details['price']
        cost = quantity * price

        if balance < cost:
            raise ValueError("Insufficient balance")

        old = portfolio.get(assetid, {
            "asset": assetid,
            "quantity": 0,
            "avgprice": 0
        })

        total_qty = old['quantity'] + quantity
        total_cost = (old['quantity'] * old['avgprice']) + cost

        portfolio[assetid] = {
            "asset": assetid,
            "quantity": total_qty,
            "avgprice": total_cost / total_qty
        }

        balance -= cost
        details['quantity'] -= quantity
        oldprice, newprice = changeprice(assetid, "buy", quantity)
        history.append(f"{now()} BUY {assetid} {quantity} @ {price}")

        return (
            f"Bought {quantity} {assetid} for ${cost}. "
            f"Price moved from ${oldprice} to ${newprice}"
        )

    except ValueError as e:
        return str(e)


def sell(asset, quantity):
    global balance

    assetid = findasset(asset)
    if not assetid:
        return "Asset does not exist"

    if assetid not in portfolio:
        return "You do not own this asset"

    try:
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        owned = portfolio[assetid]

        if owned['quantity'] < quantity:
            raise ValueError("You do not own enough quantity")

        price = market[assetid]['price']
        value = quantity * price

        owned['quantity'] -= quantity
        market[assetid]['quantity'] += quantity
        balance += value
        oldprice, newprice = changeprice(assetid, "sell", quantity)
        history.append(f"{now()} SELL {assetid} {quantity} @ {price}")

        if owned['quantity'] == 0:
            del portfolio[assetid]

        return (
            f"Sold {quantity} {assetid} for ${value}. "
            f"Price moved from ${oldprice} to ${newprice}"
        )

    except ValueError as e:
        return str(e)


def viewportfolio():
    if not portfolio:
        return f"Portfolio is empty\nBalance: ${balance}"

    rows = [f"Balance: ${balance}"]

    for assetid, details in portfolio.items():
        current = market[assetid]['price']
        profit = details['quantity'] * (current - details['avgprice'])
        rows.append(
            f"{assetid}: Owned: {details['quantity']} | "
            f"Bought At: ${details['avgprice']:.2f} | "
            f"Current: ${current} | Profit/Loss: ${profit:.2f}"
        )

    return "\n".join(rows)


def transhistory():
    if not history:
        return "No transactions yet"

    return "\n".join(history)
