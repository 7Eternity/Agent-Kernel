from typing import Dict, Any, Optional, Callable
from agentkernel_distributed.mas.agent.base.plugin_base import ProfilePlugin
from agentkernel_distributed.toolkit.logger import get_logger
from agentkernel_distributed.toolkit.storages import RedisKVAdapter

logger = get_logger(__name__)

class EasyProfilePlugin(ProfilePlugin):
    def __init__(self, redis: RedisKVAdapter, profile_data: Optional[Dict[str, Any]] = None):
        self.redis = redis
        self._profile_data = profile_data if profile_data is not None else {}
    async def init(self):
        pass
    async def execute(self):
        pass
    
    async def set_profile(self, key: str, value: Any):
        await self.redis.set(key, value)


