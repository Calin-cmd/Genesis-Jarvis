# run_jarvis.py
#!/usr/bin/env python3
import asyncio
import argparse
from jarvis.core import JarvisOrchestrator

async def main():
    parser = argparse.ArgumentParser(description="Genesis-Jarvis - Your Iron Man Style AI Companion")
    parser.add_argument("--profile", default="default", help="Profile name")
    parser.add_argument("--model", default="llama3.2", help="Default model")
    args = parser.parse_args()

    print("🚀 Starting Genesis-Jarvis...")
    jarvis = JarvisOrchestrator(profile=args.profile, model=args.model)
    await jarvis.run()

if __name__ == "__main__":
    asyncio.run(main())