# jarvis/memory_provider.py
from pathlib import Path
from typing import List, Dict, Any, Optional

# Hermes MemoryProvider base class
try:
    from hermes.memory.provider import MemoryProvider
except ImportError:
    # Fallback if import path is slightly different
    from hermes.agent.memory.provider import MemoryProvider

# Import Genesis core
from genesis.agent_memory.core import AgentMemory


class GenesisMemoryProvider(MemoryProvider):
    """Genesis Cerberus OmniPalace as a full Hermes Memory Provider"""

    @property
    def name(self) -> str:
        return "genesis"

    @property
    def description(self) -> str:
        return "Genesis - Spatial Memory Palace, Living Obsidian Wiki, Cerberus Reasoning"

    def is_available(self) -> bool:
        return True

    def initialize(self, session_id: str, **kwargs) -> None:
        self.session_id = session_id
        home_dir = Path(kwargs.get("home_dir", "~/.jarvis")).expanduser()
        
        self.agent_memory = AgentMemory(
            home_dir=home_dir / "genesis_memory",
            session_id=session_id
        )
        self.agent_memory.initialize()
        print(f"✅ Genesis Memory Provider loaded successfully (OmniPalace + Wiki Active)")

    async def store(self, turn: Dict[str, Any]) -> None:
        """Store conversation turn"""
        await self.agent_memory.store_turn(turn)

    async def retrieve(self, query: str, limit: int = 15) -> List[Dict]:
        """Retrieve relevant memories using Genesis hybrid system"""
        return await self.agent_memory.retrieve(
            query=query,
            limit=limit,
            use_omnipalace=True,
            use_wiki=True
        )

    async def search(self, query: str, **kwargs) -> List[Dict]:
        """Full search (vector + full-text + spatial)"""
        return await self.agent_memory.search(query, **kwargs)

    def on_turn_start(self, **kwargs):
        """Preheat important context (Hall of Records, user model, etc.)"""
        if hasattr(self.agent_memory, 'preheat_context'):
            self.agent_memory.preheat_context()