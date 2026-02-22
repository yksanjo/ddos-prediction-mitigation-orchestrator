from datetime import datetime, timezone


def main() -> None:
    print("ddos-prediction-mitigation-orchestrator initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
