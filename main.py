ENTRY = "You don't need to code — just tell the agent your idea in plain words, and it builds your first app while you watch; the only thing you risk is finding out your idea actually works."
OUTPUT_PATH = "/output/entry.txt"  # entry text is written here (no trailing newline); /output is created if missing


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
