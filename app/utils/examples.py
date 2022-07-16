BASIC_EXAMPLES = {
    "combinations with conditions": {
        "value": {
            "parameters": {
                "OS": ["Windows 7", "Windows 10", "Mac OS X"],
                "Browser": ["Google Chrome", "Safari", "Firefox"],
                "Resolution": ["1920*1080", "1600*900", "1366*768"],
            },
            "conditions": {
                "can": [{"Browser": "Safari", "OS": "Mac OS X"}],
                "cannot": [{"Browser": "Firefox", "OS": "Mac OS X"}],
            },
        }
    },
    "combinations without conditions": {
        "value": {
            "parameters": {
                "OS": ["Windows 7", "Windows 10", "Mac OS X"],
                "Browser": ["Google Chrome", "Safari", "Firefox"],
                "Resolution": ["1920*1080", "1600*900", "1366*768"],
            }
        }
    },
    "combinations with only 'can' conditions": {
        "value": {
            "parameters": {
                "OS": ["Windows 7", "Windows 10", "Mac OS X"],
                "Browser": ["Google Chrome", "Safari", "Firefox"],
                "Resolution": ["1920*1080", "1600*900", "1366*768"],
            },
            "conditions": {
                "can": [{"Browser": "Safari", "OS": "Mac OS X"}],
            },
        }
    },
    "combinations with only 'can not' conditions": {
        "value": {
            "parameters": {
                "OS": ["Windows 7", "Windows 10", "Mac OS X"],
                "Browser": ["Google Chrome", "Safari", "Firefox"],
                "Resolution": ["1920*1080", "1600*900", "1366*768"],
            },
            "conditions": {
                "can": [{"Browser": "Safari", "OS": "Mac OS X"}],
                "cannot": [{"Browser": "Firefox", "OS": "Mac OS X"}],
            },
        }
    },
}
