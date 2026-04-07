"""
accounts = [
["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","john00@mail.com","johnsmith@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]
]

{
johnsmith@mail.com: set(john_newyork@mail.com, john00@mail.com)
john_newyork@mail.com: set(johnsmith@mail.com)
john00@mail.com: set(johnsmith@mail.com)
mary@mail.com: set()
johnnybravo@mail.com: set()
}

{
johnsmith@mail.com: John
john00@mail.com: John
mary@mail.com: Mary
johnnybravo@mail.com: John
}

checked_emails = set()

for key, value in email_name_map.items()

johnsmith@mail.com: John
checked_emails = {johnsmith@mail.com, john_newyork@mail.com, john00@mail.com}
emails = [johnsmith@mail.com, john_newyork@mail.com, john00@mail.com]

[value] + sorted(emails)

john00@mail.com: John

=====

Time Complexity: O(nk^2 + nk log nk) (k: Max number of emails for one person)
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_graph = {}
        email_name_map = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            email_name_map[first_email] = name

            for i in range(1, len(account)):
                email = account[i]

                if email not in email_graph:
                    email_graph[email] = set()

            for i in range(1, len(account)):
                for j in range(i + 1, len(account)):
                    email_one = account[i]
                    email_two = account[j]

                    email_graph[email_one].add(email_two)
                    email_graph[email_two].add(email_one)

        visited = set()

        result = []
        for first_email, name in email_name_map.items():
            if first_email in visited:
                continue

            emails_set = set()

            self.dfs_collect_emails(email_graph, first_email, emails_set)

            temp_account = [name]
            for email in sorted(list(emails_set)):
                temp_account.append(email)

                visited.add(email)

            result.append(temp_account)

        return result

    def dfs_collect_emails(self, email_graph, current_email, emails_set):
        emails_set.add(current_email)

        for next_email in email_graph[current_email]:
            if next_email in emails_set:
                continue

            self.dfs_collect_emails(email_graph, next_email, emails_set)


"""
accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]

graph = {
    johnsmith@mail.com: [john_newyork@mail.com, john00@mail.com]
    john_newyork@mail.com: [johnsmith@mail.com]
    john00@mail.com: [johnsmith@mail.com]
    johnnybravo@mail.com: []
    mary@mail.com: []
}

{
    johnsmith@mail.com: John
    mary@mail.com: Mary
    johnnybravo@mail.com: John
}

[[John, johnsmith@mail.com, john_newyork@mail.com, john00@mail.com], [Mary, mary@mail.com]]
"""

"""
accounts = [
    ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
    ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
    ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
    ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
]

graph = {
    'Alex5@m.co': {'Alex4@m.co', 'Alex0@m.co'}, 
    'Alex4@m.co': {'Alex5@m.co', 'Alex0@m.co'}, 
    'Alex0@m.co': {'Alex5@m.co', 'Alex4@m.co'}, 
    'Ethan3@m.co': {'Ethan3@m.co', 'Ethan0@m.co'}, 
    'Ethan0@m.co': {'Ethan3@m.co'}, 
    'Kevin4@m.co': {'Kevin2@m.co'}, 
    'Kevin2@m.co': {'Kevin4@m.co', 'Kevin2@m.co'}, 
    'Gabe0@m.co': {'Gabe2@m.co', 'Gabe3@m.co'}, 
    'Gabe3@m.co': {'Gabe2@m.co', 'Gabe4@m.co', 'Gabe0@m.co'}, 
    'Gabe2@m.co': {'Gabe4@m.co', 'Gabe0@m.co', 'Gabe3@m.co'}, 
    'Gabe4@m.co': {'Gabe2@m.co', 'Gabe3@m.co'}
}

email_name = {
    'Alex5@m.co': 'Alex', 
    'Ethan3@m.co': 'Ethan', 
    'Kevin4@m.co': 'Kevin', 
    'Gabe0@m.co': 'Gabe', 
    'Gabe3@m.co': 'Gabe'
}
"""

"""
Implementing a dictionary-based graph from scratch feels quite difficult. However, solving these problems back-to-back has helped me see the commonalities and given me a bit
more confidence.

If there is a relationship where you can obtain B from A (A -> B) and A from C (C -> A), essentially a relationship where you can derive one from another and DFS seems
applicable, then it is a graph problem. Realizing that it is a graph problem and filling out the dictionary is half the battle.
"""

"""
I initially missed using the visited set here, and it is a point that is very easy to overlook. I must remember this.

We link the first email to the name in the `email_name_map` dict. However, if a link occurs at a point other than the first email within the same account, the `email_name_map`
treats it as if it were a different account. To avoid this, we add all visited emails to the `visited` set. This way, even if an email appears to be registered as a different
account in the `email_name_map`, we can identify that it has already been processed elsewhere.
"""
