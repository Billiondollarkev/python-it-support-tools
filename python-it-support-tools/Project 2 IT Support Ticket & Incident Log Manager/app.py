import datetime

class TicketManager:
    def __init__(self):
        self.tickets = []
        self.ticket_counter = 101

    def create_ticket(self, user, issue, priority="Medium"):
        ticket = {
            "id": f"TICK-{self.ticket_counter}",
            "user": user,
            "issue": issue,
            "priority": priority,
            "status": "OPEN",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tickets.append(ticket)
        self.ticket_counter += 1
        print(f"\n[+] Ticket {ticket['id']} logged successfully for {user}.")

    def view_tickets(self):
        print("\n--- ACTIVE IT SUPPORT TICKETS ---")
        if not self.tickets:
            print("No active tickets found.")
            return
        for t in self.tickets:
            print(f"[{t['id']}] | Priority: {t['priority']} | Status: {t['status']} | User: {t['user']}\n    Issue: {t['issue']} (Logged: {t['timestamp']})\n")

    def resolve_ticket(self, ticket_id):
        for t in self.tickets:
            if t["id"] == ticket_id:
                t["status"] = "RESOLVED"
                print(f"\n[✓] Ticket {ticket_id} marked as RESOLVED.")
                return
        print(f"\n[!] Ticket ID {ticket_id} not found.")

# Running the Interactive Console
if __name__ == "__main__":
    manager = TicketManager()
    manager.create_ticket("Alice User", "VPN connection keeps dropping", "High")
    manager.create_ticket("Bob Smith", "Password reset required for Outlook", "Low")
    manager.view_tickets()
    manager.resolve_ticket("TICK-102")
    manager.view_tickets()