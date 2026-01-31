import os, re, csv, collections, datetime

DUMP_DIR = r"C:\Users\yasha\CS4567\HW1\segment_dump"
OUT_CSV  = r"C:\Users\yasha\CS4567\HW1\keyword_stats.csv"

STOP = {
    "the","a","an","and","or","but","to","of","in","on","for","with","as","at","by",
    "from","is","are","was","were","be","been","it","this","that","these","those",
    "you","your","we","our","they","their","he","she","his","her","i","me","my",
    "not","can","will","would","should","could","may","might","about","into","over",
    "after","before","between","during","if","then","than","so","such"
}

word_re = re.compile(r"[a-z]{2,}")  # alphabetic tokens, len>=2

global_counts = collections.Counter()
docs = 0
tokens_total = 0

# readseg dumps can produce various filenames; we’ll just read all files that look text-like
TEXT_EXTS = (".txt", ".dump", ".out", ".log")

for root, _, files in os.walk(DUMP_DIR):
    for fn in files:
        lower = fn.lower()
        if lower.endswith(TEXT_EXTS) or "parse" in lower or "text" in lower or lower == "dump":
            path = os.path.join(root, fn)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read().lower()
            except Exception:
                continue

            toks = [t for t in word_re.findall(text) if t not in STOP]
            if toks:
                docs += 1
                tokens_total += len(toks)
                global_counts.update(toks)

top30 = global_counts.most_common(30)

print(f"Docs processed: {docs}")
print(f"Total tokens (non-stopwords): {tokens_total}")
print("Top 30 keywords:")
for w, c in top30:
    print(f"{w}\t{c}")

# Write a simple CSV for Excel
now = datetime.datetime.now().isoformat(timespec="seconds")
with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "docs_processed", "tokens_total"])
    writer.writerow([now, docs, tokens_total])
    writer.writerow([])
    writer.writerow(["keyword", "count"])
    writer.writerows(top30)

print(f"\nWrote CSV: {OUT_CSV}")
