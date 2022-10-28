from typing import Dict, List, Union

Json = Union[Dict[str, "Json"], List["Json"], str, int, float, bool, None]
