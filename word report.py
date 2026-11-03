with open ("text.txt", encoding='utf-8') as f:
    text = f.read()
    for p in ".,!?;":
        text = text.replace(p, "")
        words = text.split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
            with open("word_report.txt", "w", encoding='utf-8') as out:
                out.write(f"Total words: {len(words)}\n")
                out.write(f"Unique words: {len(counts)}\n")
                for w in sorted(counts):
                    out.write(f"{w}: {counts[w]}\n")
                    print("Report saved")