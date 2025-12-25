"""
AML/KYC Validation Engine
Anti-Money Laundering & Know Your Customer
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

@dataclass
class Transaction:
    amount: float
    currency: str
    sender_id: str
    receiver_id: str
    country_code: str

@dataclass
class ValidationResult:
    is_valid: bool
    risk_level: RiskLevel
    flags: List[str]
    requires_manual_review: bool

class AMLEngine:
    """Anti-Money Laundering Detection Engine"""
    
    # Suspicious thresholds
    HIGH_VALUE_THRESHOLD = 50000.0  # TRY
    DAILY_LIMIT = 100000.0
    
    # High-risk countries (FATF blacklist simulation)
    HIGH_RISK_COUNTRIES = ["XX", "YY", "ZZ"]
    
    def validate_transaction(self, tx: Transaction) -> ValidationResult:
        flags = []
        risk_level = RiskLevel.LOW
        
        # Rule 1: High-value transaction
        if tx.amount > self.HIGH_VALUE_THRESHOLD:
            flags.append("HIGH_VALUE_TRANSACTION")
            risk_level = RiskLevel.MEDIUM
        
        # Rule 2: High-risk country
        if tx.country_code in self.HIGH_RISK_COUNTRIES:
            flags.append("HIGH_RISK_JURISDICTION")
            risk_level = RiskLevel.HIGH
        
        # Rule 3: Structured transactions (smurfing detection)
        if 9000 < tx.amount < 10000:
            flags.append("POTENTIAL_STRUCTURING")
            risk_level = RiskLevel.HIGH
        
        # Rule 4: Critical threshold
        if tx.amount > self.DAILY_LIMIT:
            flags.append("EXCEEDS_DAILY_LIMIT")
            risk_level = RiskLevel.CRITICAL
        
        requires_review = risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL]
        is_valid = risk_level != RiskLevel.CRITICAL
        
        return ValidationResult(
            is_valid=is_valid,
            risk_level=risk_level,
            flags=flags,
            requires_manual_review=requires_review
        )

# Example Usage
if __name__ == "__main__":
    engine = AMLEngine()
    
    # Test transactions
    test_cases = [
        Transaction(5000, "TRY", "USER_A", "USER_B", "TR"),
        Transaction(75000, "TRY", "USER_C", "USER_D", "TR"),
        Transaction(9500, "TRY", "USER_E", "USER_F", "TR"),
        Transaction(150000, "TRY", "USER_G", "USER_H", "XX"),
    ]
    
    for i, tx in enumerate(test_cases, 1):
        result = engine.validate_transaction(tx)
        print(f"\n[TX {i}] Amount: {tx.amount} {tx.currency}")
        print(f"  Risk: {result.risk_level.value}")
        print(f"  Flags: {', '.join(result.flags) if result.flags else 'None'}")
        print(f"  Manual Review: {'YES' if result.requires_manual_review else 'NO'}")
        print(f"  Valid: {'✓' if result.is_valid else '✗'}")
