# jarvis/cerberus_hook.py
from typing import Dict, Any

async def should_use_cerberus(query: str) -> bool:
    """Simple heuristic - can be made smarter later"""
    complex_keywords = ["analyze", "compare", "reason", "decide", "plan", "why", "how", "should", "best"]
    return any(kw in query.lower() for kw in complex_keywords)

async def run_cerberus(query: str, memory_context: list) -> str:
    """Placeholder - will wire to your real CerberusOrchestrator"""
    from genesis.cerberus import CerberusOrchestrator
    
    orchestrator = CerberusOrchestrator()
    result = await orchestrator.run(query, context=memory_context)
    return result