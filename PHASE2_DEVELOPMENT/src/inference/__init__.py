"""
Inference module for RYZEN-LLM Phase 2.

This module provides advanced inference capabilities including:
- Speculative decoding for accelerated text generation
- Multimodal processing
- Inference pipelines
"""

from .speculative_decoder import (
    SpeculativeConfig,
    SpeculativeStats,
    DraftModel,
    SimpleDraftModel,
    Verifier,
    TargetModelVerifier,
    SpeculativeDecoder,
    create_speculative_decoder,
    benchmark_speculative_decoding,
    performance_monitor,
)

__all__ = [
    "SpeculativeConfig",
    "SpeculativeStats",
    "DraftModel",
    "SimpleDraftModel",
    "Verifier",
    "TargetModelVerifier",
    "SpeculativeDecoder",
    "create_speculative_decoder",
    "benchmark_speculative_decoding",
    "performance_monitor",
]
