"""
Utilities for model fine-tuning and inference.
"""

class GeminiFinetuner:
    def __init__(self):
            self.model_configs = {
                        'epochs': 5,
                                    'batch_size': 4,
                                                'learning_rate': 0.001
                                                        }