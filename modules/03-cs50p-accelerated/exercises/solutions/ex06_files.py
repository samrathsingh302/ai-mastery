"""Reference solution — rung 6."""


def word_frequencies(path):
    counts = {}
    with open(path) as f:
        for line in f:
            for raw in line.split():
                word = raw.strip(".,!?;:").lower()
                if word:
                    counts[word] = counts.get(word, 0) + 1
    return counts


def write_then_read(path, lines):
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
    with open(path) as f:
        return [line.rstrip("\n") for line in f]
