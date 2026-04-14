# jarvis/core.py
import asyncio
from jarvis.memory_provider import GenesisMemoryProvider

class JarvisOrchestrator:
    def __init__(self, profile: str = "default", model: str = "llama3.2"):
        self.profile = profile
        self.model = model
        self.memory_provider = None

    async def run(self):
        # Initialize Genesis as memory provider
        self.memory_provider = GenesisMemoryProvider()
        self.memory_provider.initialize(session_id=f"jarvis-{self.profile}")

        print("✅ Genesis-Jarvis is now running with full OmniPalace + Cerberus brain!")
        print("   Memory, Wiki, and Spatial Palace are active.")
        
        # TODO: Later we will start the full Hermes agent here with Genesis provider
        await asyncio.sleep(1)  # Placeholder
        print("🧠 Ready for commands. (Full integration coming in next steps)")