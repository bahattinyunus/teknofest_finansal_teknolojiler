import uuid
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class TransactionLine:
    account_id: str
    amount: float  # Positive for Debit, Negative for Credit
    description: str

@dataclass
class Transaction:
    transaction_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.now)
    lines: List[TransactionLine] = field(default_factory=list)

    def is_balanced(self) -> bool:
        """Double-entry bookkeeping must sum to zero."""
        return sum(line.amount for line in self.lines) == 0

class CoreLedger:
    """
    Elite FinTech Core Ledger Simulator
    Implements ACID principles and Double-Entry integrity.
    """
    def __init__(self):
        self.accounts: Dict[str, float] = {}
        self.history: List[Transaction] = []

    def create_account(self, account_id: str, initial_balance: float = 0.0):
        self.accounts[account_id] = initial_balance

    def post_transaction(self, transaction: Transaction):
        if not transaction.is_balanced():
            raise ValueError("Transaction Unbalanced! FinTech integrity violation.")
        
        # Atomic consistency simulation
        for line in transaction.lines:
            if line.account_id not in self.accounts:
                self.accounts[line.account_id] = 0.0
            self.accounts[line.account_id] += line.amount
        
        self.history.append(transaction)
        print(f"Transaction {transaction.transaction_id} posted successfully.")

# Example Usage
if __name__ == "__main__":
    ledger = CoreLedger()
    
    # Create Accounts
    ledger.create_account("CASH_RESERVE", 1000.0)
    ledger.create_account("USER_123_WALLET", 0.0)

    # Transfer 200 from Reserve to User
    tx = Transaction(lines=[
        TransactionLine("CASH_RESERVE", -200.0, "Withdrawal from reserve"),
        TransactionLine("USER_123_WALLET", 200.0, "Deposit to user wallet")
    ])

    try:
        ledger.post_transaction(tx)
        print(f"Balances: {ledger.accounts}")
    except ValueError as e:
        print(f"Error: {e}")
