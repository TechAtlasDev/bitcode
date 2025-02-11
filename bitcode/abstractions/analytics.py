from dataclasses import dataclass, field

@dataclass
class SimpleTicker:
    price: float = field(init=False, default=0.0)
    symbol: str = field(init=False, default="")

    def __init__(self, data: dict):
        self.price = float(data.get("price", 0.0))
        self.symbol = data.get("symbol", "")

@dataclass
class Ticker:
    id:int = field(init=False, default=0)
    price:float = field(init=False, default=0.0)
    symbol: str = field(init=False, default="")
    qty:float = field(init=False, default=0.0)
    quoteQty:float = field(init=False, default=0.0)
    time:int = field(init=False, default=0)
    isBuyerMaker:bool = field(init=False, default=False)
    isBestMatch:bool = field(init=False, default=False)

    def __init__(self, data: dict):
        self.id = int(data.get("id", 0))
        self.price = float(data.get("price", 0.0))
        self.symbol = data.get("symbol", "")
        self.qty = float(data.get("qty", 0.0))
        self.quoteQty = float(data.get("quoteQty", 0.0))
        self.time = int(data.get("time", 0))
        self.isBuyerMaker = bool(data.get("isBuyerMaker", False))
        self.isBestMatch = bool(data.get("isBestMatch", False))