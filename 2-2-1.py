import sys


def encode_states(seqs, seq_length):
    """
    Encode possible states of a set of sequences

    :param seqs: Iterable of binary strings representing genomic tracks with possible states
    :param seq_length: Length of all sequences
    """
    state_marker = 1
    states = {}  # Define possible states and representation
    state_tracker = []  # Indicator for state of position
    for i in range(0, seq_length):
        state = "".join([x[i] for x in seqs])
        if state not in states.keys():
            states[state] = state_marker
            state_marker += 1
        state_tracker.append(states[state])
    return state_tracker


with open(sys.argv[1], "r") as fh:
    next(fh)
    while True:
        try:
            n, l = [int(x) for x in next(fh).strip().split()]
        except StopIteration as e:
            break
        seqs = [next(fh) for _ in range(0, n)]
        states = encode_states(seqs, l)
        print(max(states))
        print(" ".join([str(x) for x in states]))
