import json
import uuid
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass, asdict

@dataclass
class Event:
    """Immutable financial event for Event Sourcing"""
    event_id: str
    event_type: str
    aggregate_id: str  # Account ID, Transaction ID, etc.
    timestamp: str
    payload: Dict[str, Any]
    version: int = 1

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)

class EventStore:
    """
    Event Sourcing Store - Kafka Simulation
    In production, this would publish to Kafka topics
    """
    def __init__(self):
        self.events: List[Event] = []
    
    def append(self, event: Event):
        """Append event to immutable log"""
        self.events.append(event)
        print(f"[EVENT STORED] {event.event_type} | ID: {event.event_id[:8]}...")
    
    def get_events_by_aggregate(self, aggregate_id: str) -> List[Event]:
        """Replay events for a specific aggregate"""
        return [e for e in self.events if e.aggregate_id == aggregate_id]

class AccountAggregate:
    """Account state rebuilt from events"""
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0.0
        self.version = 0
    
    def apply_event(self, event: Event):
        """Event handler - rebuilds state"""
        if event.event_type == "AccountCreated":
            self.balance = event.payload.get("initial_balance", 0.0)
        elif event.event_type == "MoneyDeposited":
            self.balance += event.payload["amount"]
        elif event.event_type == "MoneyWithdrawn":
            self.balance -= event.payload["amount"]
        
        self.version = event.version
    
    def rebuild_from_events(self, events: List[Event]):
        """Replay all events to rebuild current state"""
        for event in events:
            self.apply_event(event)

# Example Usage
if __name__ == "__main__":
    store = EventStore()
    
    # Create account
    account_id = str(uuid.uuid4())
    event1 = Event(
        event_id=str(uuid.uuid4()),
        event_type="AccountCreated",
        aggregate_id=account_id,
        timestamp=datetime.now().isoformat(),
        payload={"initial_balance": 1000.0, "currency": "TRY"}
    )
    store.append(event1)
    
    # Deposit
    event2 = Event(
        event_id=str(uuid.uuid4()),
        event_type="MoneyDeposited",
        aggregate_id=account_id,
        timestamp=datetime.now().isoformat(),
        payload={"amount": 500.0, "source": "WIRE_TRANSFER"},
        version=2
    )
    store.append(event2)
    
    # Rebuild account state from events
    account = AccountAggregate(account_id)
    events = store.get_events_by_aggregate(account_id)
    account.rebuild_from_events(events)
    
    print(f"\n[ACCOUNT STATE] Balance: {account.balance} TRY | Version: {account.version}")
    print(f"Total Events in Store: {len(store.events)}")
