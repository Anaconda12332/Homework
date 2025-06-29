def print_summary(messages):
    print(f"Total messages: {len(messages)}")
    print(f"Empty messages: {sum(1 for m in messages if not m.strip())}")
    print(f"Longest message: {max(messages, key=len)}")


def sum_empty_messages(messages):
    return sum(1 for m in messages if not m.strip())


def contains_urgent(messages):
    return any('urgent' in m.lower() for m in messages)


def get_average_length(messages):
    if not messages:
        return 0
    return sum(len(m) for m in messages) / len(messages)


def count_keywords(messages, keyword):
    if not messages:
        return 0
    return sum(1 for m in messages if keyword.lower() in m.lower())
