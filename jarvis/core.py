# jarvis/core.py
import asyncio
from jarvis.config import JarvisConfig
from jarvis.memory_provider import GenesisMemoryProvider

class JarvisOrchestrator:
    def __init__(self, profile: str = "default", model: str = "llama3.2"):
        self.config = JarvisConfig(profile=profile, default_model=model)
        self.memory_provider = None

    async def run(self):
        print("🚀 Initializing Genesis-Jarvis...")

        # Initialize Genesis Memory Provider
        self.memory_provider = GenesisMemoryProvider()
        self.memory_provider.initialize(
            session_id=f"jarvis-{self.config.profile}",
            home_dir=self.config.home_dir
        )

        print("✅ Genesis-Jarvis is alive!")
        print("   • Spatial Memory Palace (OmniPalace) Active")
        print("   • Living Obsidian Wiki Active")
        print("   • Cerberus Multi-Agent Reasoning Ready")
        print("\nType 'exit' or press Ctrl+C to quit.\n")

        # Placeholder loop for now
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                print("Jarvis: Thinking... (Full conversation loop coming soon)")
            except KeyboardInterrupt:
                break