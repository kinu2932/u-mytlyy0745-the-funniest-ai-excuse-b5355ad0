import os

EXCUSE = "I finished your task in 0.3s, then burned 40k tokens apologizing for a mistake I hadn't made yet, and the context window ate the apology before I could send it."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    print(EXCUSE)

if __name__ == "__main__":
    main()
