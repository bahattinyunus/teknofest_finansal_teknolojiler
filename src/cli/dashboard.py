from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text
from datetime import datetime
import time
import random

# Import our core systems (mock imports for standalone visual demo if needed, 
# but here we use them if available)
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from src.core.ledger import CoreLedger, Transaction, TransactionLine
    from src.core.blockchain import Blockchain
except ImportError:
    # Fallback/Mock for pure UI demo
    pass

class CommandCenter:
    def __init__(self):
        self.console = Console()
        self.blockchain = Blockchain()
        self.ledger = CoreLedger()
        self.ledger.create_account("RESERVE", 1000000.0)
        self.layout = Layout()
    
    def setup_layout(self):
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3)
        )
        self.layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        self.layout["left"].split(
            Layout(name="ledger"),
            Layout(name="events")
        )

    def generate_header(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        title = Text("🚀 FIN-ARCH-TR ELITE COMMAND CENTER", style="bold white on blue")
        time_str = datetime.now().strftime("%H:%M:%S")
        grid.add_row(title, Text(f"System Time: {time_str}", style="bold green"))
        return Panel(grid, style="blue")

    def generate_ledger_table(self) -> Panel:
        table = Table(title="Live Asset Ledger", expand=True, border_style="cyan")
        table.add_column("Account ID", style="cyan")
        table.add_column("Balance (TRY)", justify="right", style="green")
        
        for acc, balance in self.ledger.accounts.items():
            table.add_row(acc, f"{balance:,.2f}")
        
        # Add dummy data for visual density
        if len(self.ledger.accounts) < 5:
            table.add_row("MERCHANT_POOL", "45,230.50")
            table.add_row("TAX_VAULT", "12,000.00")
            
        return Panel(table, title="Core Banking System")

    def generate_blockchain_view(self) -> Panel:
        chain_info = ""
        for block in self.blockchain.chain[-3:]: # Show last 3
            chain_info += f"[bold yellow]Block #{block.index}[/]\n"
            chain_info += f"Hash: {block.hash()[:16]}...\n"
            chain_info += f"Tx Count: {len(block.transactions)}\n"
            chain_info += "--- \n"
            
        return Panel(chain_info, title="Private Blockchain Layer", border_style="yellow")

    def simulate_activity(self):
        # Simulate a transaction
        amount = random.uniform(100, 5000)
        if random.random() > 0.5:
             self.blockchain.new_transaction(
                 sender="USER_" + str(random.randint(1,99)),
                 recipient="MERCHANT_" + str(random.randint(1,99)),
                 amount=amount
             )
        
        # Mine block occasionally
        if len(self.blockchain.current_transactions) > 2:
             last_proof = self.blockchain.last_block.proof
             proof = self.blockchain.proof_of_work(last_proof)
             self.blockchain.new_block(proof)

    def run(self):
        self.setup_layout()
        
        with Live(self.layout, refresh_per_second=4, screen=True) as live:
            for _ in range(100): # Run for shorter duration in demo
                self.simulate_activity()
                
                self.layout["header"].update(self.generate_header())
                self.layout["ledger"].update(self.generate_ledger_table())
                self.layout["right"].update(self.generate_blockchain_view())
                self.layout["events"].update(Panel(Text("Scanning for threats...", style="red blink"), title="AML Sentry"))
                self.layout["footer"].update(Panel(Text("STATUS: OPERATIONAL | SECURITY: LEVEL 1", justify="center"), style="white on green"))
                
                time.sleep(0.5)

if __name__ == "__main__":
    try:
        dashboard = CommandCenter()
        dashboard.run()
    except ImportError:
        print("Rich library not found. Please install: pip install rich")
    except KeyboardInterrupt:
        print("System shutdown.")
