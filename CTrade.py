class CTrade():
    direction = 0
    pos = 0
    inPos = []
    outPos = []
    inTime = []
    outTime = []
    inPrice = []
    outPrice = []
    Note = []

    def __init__(self, dir, n, price, reason = "start"):
        self.direction = dir
        self.pos = n
        self.inPos.append(n)
        self.inPrice.append(price)
        self.Note.append(reason)

    def add(self, time, n, price, reason = "add contract"):
        self.inTime.append(time)
        self.inPrice.append(price)
        self.Note.append(reason)
        self.inPos.append(n)
        self.pos += n

    def stop(self, time, price, reason = "stop"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(reason)
        self.outPos.append(self.pos)
        self.pos = 0

    def limit(self, time, price, reason = "limit"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(reason)
        self.outPos.append(self.pos)
        self.pos = 0

    def cut(self, time, n, price, reason = "cut"):
        self.outTime.append(time)
        self.outPrice.append(price)
        self.Note.append(reason)
        self.outPos.append(n)
        self.pos -= n

    def end(self):
        # write trade information into a table
        pass
