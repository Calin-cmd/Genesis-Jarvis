# jarvis/config.py
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class JarvisConfig:
    profile: str = "default"
    home_dir: Path = Path("~/.jarvis").expanduser()
    default_model: str = "llama3.2"
    temperature: float = 0.7
    use_cerberus_by_default: bool = True
    use_omnipalace: bool = True
    use_wiki: bool = True

    @property
    def genesis_memory_dir(self) -> Path:
        return self.home_dir / "genesis_memory"

    @property
    def obsidian_vault_dir(self) -> Path:
        return self.home_dir / "vault"