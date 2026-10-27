"""
LLM client for Nebius Token Factory integration.
Research and decision-support only - not for clinical use.
"""

import os
from typing import Dict, Optional, List, Any
import json


class NebiusClient:
    """Client for Nebius Token Factory API (OpenAI-compatible)."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.tokenfactory.nebius.com/v1/",
        model_fast: Optional[str] = None,
        model_mid: Optional[str] = None,
        model_reason: Optional[str] = None
    ):
        self.api_key = api_key or os.getenv('NEBIUS_API_KEY')
        self.base_url = base_url
        
        # Model routing
        self.model_fast = model_fast or os.getenv('MODEL_FAST', 'nvidia/Nemotron-3_5-Lightning')
        self.model_mid = model_mid or os.getenv('MODEL_MID', 'nvidia/Nemotron-3.5-Super-VL')
        self.model_reason = model_reason or os.getenv('MODEL_REASON', 'nvidia/Nemotron-3-Ultra-550b-a55b')
        
        self.client = None
        self.offline_mode = False
        
        # Initialize OpenAI client if key available
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url
                )
            except ImportError:
                print("Warning: openai package not installed. Running in offline mode.")
                self.offline_mode = True
            except Exception as e:
                print(f"Warning: Failed to initialize OpenAI client: {e}. Running in offline mode.")
                self.offline_mode = True
        else:
            self.offline_mode = True
    
    def call(
        self,
        messages: List[Dict[str, str]],
        model_tier: str = 'fast',
        response_format: Optional[Dict] = None,
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        Call the LLM.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model_tier: 'fast', 'mid', or 'reason'
            response_format: Optional JSON schema for structured output
            temperature: float
            max_tokens: int
        
        Returns:
            {
                'content': str,
                'model': str,
                'usage': {...},
                'offline': bool
            }
        """
        if self.offline_mode or not self.client:
            return {
                'content': json.dumps({'error': 'offline_mode', 'message': 'LLM unavailable - rules-only mode'}),
                'model': 'offline',
                'usage': {},
                'offline': True
            }
        
        # Select model
        if model_tier == 'fast':
            model = self.model_fast
        elif model_tier == 'mid':
            model = self.model_mid
        elif model_tier == 'reason':
            model = self.model_reason
        else:
            model = self.model_mid
        
        try:
            # Build request params
            params = {
                'model': model,
                'messages': messages,
                'temperature': temperature,
                'max_tokens': max_tokens
            }
            
            # Add response_format if provided
            if response_format:
                params['response_format'] = response_format
            
            # Call API
            response = self.client.chat.completions.create(**params)
            
            return {
                'content': response.choices[0].message.content,
                'model': model,
                'usage': {
                    'prompt_tokens': response.usage.prompt_tokens,
                    'completion_tokens': response.usage.completion_tokens,
                    'total_tokens': response.usage.total_tokens
                },
                'offline': False
            }
        
        except Exception as e:
            print(f"LLM call failed: {e}")
            # Fallback to offline mode
            return {
                'content': json.dumps({'error': 'api_error', 'message': str(e)}),
                'model': model,
                'usage': {},
                'offline': True
            }
    
    def is_available(self) -> bool:
        """Check if LLM is available."""
        return not self.offline_mode and self.client is not None
