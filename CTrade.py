class CTrade():
    pos = 0
    volume = 0
    inPos = []
    outPos = []
    inTime = []
    outTime = []
    inPrice = []
    outPrice = []
    Note = []

    def __init__(self, position, n, price, type = "start"):
        self.pos = position
        self.volume = n
        self.inPos.append(n)
        self.inPrice.append(price)
        self.Note.append(type)

    def add(self, time, n, price, type = "add contract"):
        self.inTime.append(time)
        self.inPrice.append(price)
        self.Note.append(type)
        self.inPos.append(n)
        self.volume += n

    def stop(self, time, price, type = "stop"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(type)
        self.outPos.append(self.volume)
        self.volume = 0

    def limit(self, time, price, type = "limit"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(type)
        self.outPos.append(self.volume)
        self.volume = 0

    def cut(self, time, n, price, type = "cut"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(type)
        self.outPos.append(n)
        self.volume -= n

    def end(self):
        # write trade information into a table
        pass

trade = CTrade(-1, 3, 10666)
print("Current Volume:", trade.volume, ", dir:", trade.pos)
trade.add('08:50', 2, 10633)
print("Current Volume:", trade.volume, ", dir:", trade.pos)
trade.cut('12:34', 1, 10600)
print("Current Volume:", trade.volume, ", dir:", trade.pos)
trade.stop('13:45', 10638)
print("Current Volume:", trade.volume, ", dir:", trade.pos)

print("inPrice list:")
for price in trade.inPrice:
    print("  ", price)

print("outPrice list:")
for price in trade.outPrice:
    print("  ", price)

print("note list:")
for note in trade.Note:
    print("  ", note)

print("inPos list:")
for n in trade.inPos:
    print("  ", n)

print("outPos list:")
for n in trade.outPos:
    print("  ", n)