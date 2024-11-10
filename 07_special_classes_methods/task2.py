class Lucas:
    u0:int = None
    u1:int = None
    p:int = None
    q:int = None
    n:int = None
    prev_val:int = None
    cur_val:int = None

    cur_idx:int = 0

    def __init__(self, u0:int, u1:int, p:int, q:int, n:int):
        self.u0 = u0
        self.u1 = u1
        self.p = p
        self.q = q
        self.n = n
    
    def __iter__(self):
        self.cur_idx = 0
        self.prev_val = self.u0
        self.cur_val = self.u1
        return self
    
    def __next__(self):
        if self.cur_idx >= self.n:
            raise StopIteration
        
        if self.cur_idx == 0:
            res = self.u0
        elif self.cur_idx == 1:
            res = self.u1
        else:
            res = self.p * self.cur_val - self.q * self.prev_val
            self.prev_val = self.cur_val
            self.cur_val = res
        
        self.cur_idx += 1
        return res
