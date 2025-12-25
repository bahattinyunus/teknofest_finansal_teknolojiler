"""
Fin-Arch-TR Core Financial Modules
===================================
This package contains the core financial logic for the FinTech architecture.
"""

from .ledger import CoreLedger, Transaction, TransactionLine

__all__ = ['CoreLedger', 'Transaction', 'TransactionLine']
__version__ = '1.0.0'
