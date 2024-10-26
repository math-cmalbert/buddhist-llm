"""
Data processing utilities for Buddhist LLM project.
Handles text processing and training data generation.
"""

from typing import List, Dict, Optional
import json

class BuddhistTextProcessor:
    def __init__(self):
            self.gemini_constraints = {
                        'max_input_length': 40000,
                                    'max_output_length': 5000,
                                                'min_examples': 20
                                                        }
                                                            
                                                                def validate_training_pair(self, 
                                                                        text_input: str, 
                                                                                output: str
                                                                                    ) -> bool:
                                                                                            """Validate if a training pair meets Gemini requirements."""
                                                                                                    return (len(text_input) <= self.gemini_constraints['max_input_length'] and
                                                                                                                    len(output) <= self.gemini_constraints['max_output_length'])

                                                                                                                        def format_training_pair(self,
                                                                                                                                context: str,
                                                                                                                                        question: str,
                                                                                                                                                answer: str
                                                                                                                                                    ) -> Dict[str, str]:
                                                                                                                                                            """Format a training pair for Gemini fine-tuning."""
                                                                                                                                                                    text_input = f"Context: {context}\nQuestion: {question}"
                                                                                                                                                                            if self.validate_training_pair(text_input, answer):
                                                                                                                                                                                        return {
                                                                                                                                                                                                        "text_input": text_input,
                                                                                                                                                                                                                        "output": answer
                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                            return None