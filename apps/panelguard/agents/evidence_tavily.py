"""
Evidence lookup using Tavily API.
Research and decision-support only - not for clinical use.
"""

import os
from typing import Optional, Dict, List, Any


def lookup_antibody_evidence(
    antibody_name: str,
    tavily_api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Look up clinical significance evidence for an antibody using Tavily.
    
    Only the antibody name is sent to Tavily - never patient data.
    
    Args:
        antibody_name: e.g., 'K', 'Fya', 'Jka'
        tavily_api_key: Optional API key, defaults to env TAVILY_API_KEY
    
    Returns:
        {
            'antibody': str,
            'sources': [...],
            'available': bool
        }
    """
    result = {
        'antibody': antibody_name,
        'sources': [],
        'available': False
    }
    
    api_key = tavily_api_key or os.getenv('TAVILY_API_KEY')
    
    if not api_key:
        result['sources'].append({
            'title': 'Tavily API key not configured',
            'url': '',
            'snippet': 'Evidence lookup unavailable'
        })
        return result
    
    try:
        from tavily import TavilyClient
        
        client = TavilyClient(api_key=api_key)
        
        # Search query: antibody clinical significance only
        query = f"anti-{antibody_name} blood group antibody clinical significance transfusion AABB BCSH"
        
        response = client.search(
            query=query,
            max_results=3,
            search_depth="basic"
        )
        
        result['available'] = True
        
        for item in response.get('results', []):
            result['sources'].append({
                'title': item.get('title', ''),
                'url': item.get('url', ''),
                'snippet': item.get('content', '')[:300]
            })
    
    except ImportError:
        result['sources'].append({
            'title': 'Tavily client not installed',
            'url': '',
            'snippet': 'Install tavily-python package'
        })
    except Exception as e:
        result['sources'].append({
            'title': f'Error: {str(e)}',
            'url': '',
            'snippet': 'Evidence lookup failed'
        })
    
    return result
