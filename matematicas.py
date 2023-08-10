class Message:(object)
    def __init__(self, message: str, sender: int, receiver: int) -> None:
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def __str__(self) -> str:
        return self.message

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Message):
            return self.message == other.message
        return False


def process_queries(queries, messages):
    for query in queries:
        instruction, *data = query.split()
        if instruction == 'print':
            index = int(data[0])
            print(messages[index])
        elif instruction == 'eq':
            i1, i2 = map(int, data)
            print(messages[i1] == messages[i2])


# Example usage:
n = int(input())
messages = []
for _ in range(n):
    msg, sender, receiver = input().split()
    messages.append(Message(msg, int(sender), int(receiver)))

q = int(input())
queries = [input() for _ in range(q)]

process_queries(queries, messages)