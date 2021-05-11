"""
    Domain service
    
    At the center of an onion layered model. 
    Depends on no one. 
    Is depended by everyone. 
    Receives arrows but does send any arrow. 

    Is stateless. 
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set


# ------------------------------------ Domain service ------------------------------------------
class OutOfStock(Exception):
    pass

def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")

# ------------------------------------ Models ------------------------------------------

# ------------------------------------ Order ------------------------------------------
@dataclass(unsafe_hash=True)
class Order:
    orderid: str
    sku: str
    qty: int
    eta: date


# ------------------------------------ OrderLine ------------------------------------------
@dataclass(unsafe_hash=True)
class OrderLine:
    orderid: str
    sku: str
    qty: int

# ------------------------------------ Batch ------------------------------------------
class Batch:
    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()  # type: Set[OrderLine]


    def to_json(self):
        return {
            "reference": self.reference,
            "sku": self.sku,
            "qty": self._purchased_quantity
            #"eta": self.eta
        }


    def __repr__(self):
        #return f"<Batch {self.reference}>"
        return f"'{self.sku}'"

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta

    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
