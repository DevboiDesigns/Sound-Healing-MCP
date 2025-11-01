"""
MCP Server for Healing Harmonic Frequencies
Provides tools and resources for accessing healing frequencies including
well-tone frequencies, experimental frequencies, and innovative calculations.
"""

import asyncio
import json
import math
from typing import Any, Sequence
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.models import InitializationOptions
from mcp.types import Tool, TextContent, ServerCapabilities

# Initialize the server
app = Server("sound-healing-mcp")

# Well-Tone Frequency Database
WELL_TONE_FREQUENCIES = {
    "chakra_base": 396,
    "chakra_sacral": 417,
    "chakra_solar_plexus": 528,
    "chakra_heart": 639,
    "chakra_throat": 741,
    "chakra_third_eye": 852,
    "chakra_crown": 963,
    "love_frequency": 528,
    "solfeggio_174": 174,
    "solfeggio_285": 285,
    "solfeggio_396": 396,
    "solfeggio_417": 417,
    "solfeggio_528": 528,
    "solfeggio_639": 639,
    "solfeggio_741": 741,
    "solfeggio_852": 852,
    "solfeggio_963": 963,
    "earth_432": 432,
    "earth_8": 8,  # Schumann resonance base
    "earth_7_83": 7.83,  # Schumann resonance primary
    "theta": 4,  # Theta brainwave
    "delta": 0.5,  # Delta brainwave
    "alpha": 8,  # Alpha brainwave
    "beta": 13,  # Beta brainwave
    "gamma": 40,  # Gamma brainwave
}


def calculate_harmonic_series(base_freq: float, harmonics: int = 10) -> list[float]:
    """Calculate harmonic series from a base frequency."""
    return [base_freq * (n + 1) for n in range(harmonics)]


def calculate_pythagorean_ratio(freq: float, ratio: tuple[int, int]) -> float:
    """Calculate frequency using Pythagorean ratios."""
    return freq * (ratio[0] / ratio[1])


def calculate_fibonacci_frequency(base: float, index: int) -> float:
    """Calculate frequency based on Fibonacci sequence."""
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    if index < len(fibonacci):
        return base * fibonacci[index]
    return base * fibonacci[-1]


def calculate_golden_ratio_frequency(base: float) -> float:
    """Calculate frequency using golden ratio (1.618...)."""
    phi = (1 + math.sqrt(5)) / 2
    return base * phi


def calculate_prime_harmonics(base: float, primes: list[int]) -> list[float]:
    """Calculate harmonics using prime numbers."""
    return [base * p for p in primes]


def generate_phi_based_frequencies(base: float, count: int = 10) -> list[float]:
    """Generate frequencies based on phi (golden ratio) spirals."""
    phi = (1 + math.sqrt(5)) / 2
    return [base * (phi ** n) for n in range(count)]


def calculate_quantum_harmonics(freq: float, quantum_level: int) -> float:
    """Calculate quantum-level harmonics (based on energy levels)."""
    return freq * (quantum_level ** 2)


def generate_fractal_frequencies(base: float, depth: int = 5) -> list[float]:
    """Generate fractal-based frequencies using self-similar patterns."""
    frequencies = [base]
    for i in range(depth):
        # Fractal pattern: each level multiplies by 2 and divides by golden ratio
        phi = (1 + math.sqrt(5)) / 2
        frequencies.append(frequencies[-1] * 2 / phi)
        frequencies.append(frequencies[-1] * phi)
    return sorted(set(frequencies))


def calculate_resonance_cascade(base: float, steps: int = 7) -> list[float]:
    """Calculate resonance cascade frequencies."""
    cascade = [base]
    for i in range(1, steps):
        # Each step creates harmonics that resonate with previous
        next_freq = cascade[-1] * math.sqrt(2)
        cascade.append(next_freq)
    return cascade


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List all available tools."""
    return [
        Tool(
            name="get_well_tone_frequency",
            description="Get a specific well-tone healing frequency by name (e.g., chakra_base, solfeggio_528, earth_432)",
            inputSchema={
                "type": "object",
                "properties": {
                    "frequency_name": {
                        "type": "string",
                        "description": "Name of the well-tone frequency to retrieve"
                    }
                },
                "required": ["frequency_name"]
            }
        ),
        Tool(
            name="list_all_well_tones",
            description="List all available well-tone frequencies organized by category",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="get_chakra_frequencies",
            description="Get all chakra healing frequencies",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="calculate_harmonic_series",
            description="Calculate harmonic series from a base frequency",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "harmonics_count": {
                        "type": "integer",
                        "description": "Number of harmonics to calculate (default: 10)",
                        "default": 10
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="calculate_pythagorean_frequency",
            description="Calculate frequency using Pythagorean ratios",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "numerator": {
                        "type": "integer",
                        "description": "Numerator of the ratio"
                    },
                    "denominator": {
                        "type": "integer",
                        "description": "Denominator of the ratio"
                    }
                },
                "required": ["base_frequency", "numerator", "denominator"]
            }
        ),
        Tool(
            name="calculate_fibonacci_frequency",
            description="Calculate frequency based on Fibonacci sequence",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "fibonacci_index": {
                        "type": "integer",
                        "description": "Index in Fibonacci sequence (0-11)",
                        "minimum": 0,
                        "maximum": 11
                    }
                },
                "required": ["base_frequency", "fibonacci_index"]
            }
        ),
        Tool(
            name="calculate_golden_ratio_frequency",
            description="Calculate frequency using golden ratio (phi)",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="calculate_prime_harmonics",
            description="Calculate harmonics using prime numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "primes": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "List of prime numbers to use (default: first 10 primes)"
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="generate_phi_spiral_frequencies",
            description="Generate frequencies based on golden ratio spiral",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of frequencies to generate (default: 10)",
                        "default": 10
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="calculate_quantum_harmonic",
            description="Calculate quantum-level harmonics based on energy levels",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "quantum_level": {
                        "type": "integer",
                        "description": "Quantum energy level (1-10)",
                        "minimum": 1,
                        "maximum": 10
                    }
                },
                "required": ["base_frequency", "quantum_level"]
            }
        ),
        Tool(
            name="generate_fractal_frequencies",
            description="Generate fractal-based frequencies using self-similar patterns",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "depth": {
                        "type": "integer",
                        "description": "Fractal depth (default: 5)",
                        "default": 5
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="calculate_resonance_cascade",
            description="Calculate resonance cascade frequencies",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "steps": {
                        "type": "integer",
                        "description": "Number of cascade steps (default: 7)",
                        "default": 7
                    }
                },
                "required": ["base_frequency"]
            }
        ),
        Tool(
            name="generate_custom_frequency_matrix",
            description="Generate a matrix of frequencies combining multiple mathematical principles",
            inputSchema={
                "type": "object",
                "properties": {
                    "base_frequency": {
                        "type": "number",
                        "description": "Base frequency in Hz"
                    },
                    "include_fibonacci": {
                        "type": "boolean",
                        "description": "Include Fibonacci-based frequencies",
                        "default": True
                    },
                    "include_golden_ratio": {
                        "type": "boolean",
                        "description": "Include golden ratio frequencies",
                        "default": True
                    },
                    "include_primes": {
                        "type": "boolean",
                        "description": "Include prime-based harmonics",
                        "default": True
                    },
                    "matrix_size": {
                        "type": "integer",
                        "description": "Size of the frequency matrix (default: 8)",
                        "default": 8
                    }
                },
                "required": ["base_frequency"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    
    if name == "get_well_tone_frequency":
        freq_name = arguments.get("frequency_name", "")
        if freq_name in WELL_TONE_FREQUENCIES:
            freq = WELL_TONE_FREQUENCIES[freq_name]
            return [
                TextContent(
                    type="text",
                    text=json.dumps({
                        "frequency_name": freq_name,
                        "frequency_hz": freq,
                        "description": f"Retrieved {freq_name} frequency"
                    }, indent=2)
                )
            ]
        else:
            available = ", ".join(WELL_TONE_FREQUENCIES.keys())
            return [
                TextContent(
                    type="text",
                    text=json.dumps({
                        "error": f"Frequency '{freq_name}' not found",
                        "available_frequencies": available
                    }, indent=2)
                )
            ]
    
    elif name == "list_all_well_tones":
        categorized = {
            "chakras": {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k.startswith("chakra_")},
            "solfeggio": {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k.startswith("solfeggio_")},
            "earth_resonance": {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k.startswith("earth_")},
            "brainwaves": {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k in ["theta", "delta", "alpha", "beta", "gamma"]},
            "special": {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k == "love_frequency"}
        }
        return [
            TextContent(
                type="text",
                text=json.dumps(categorized, indent=2)
            )
        ]
    
    elif name == "get_chakra_frequencies":
        chakras = {k: v for k, v in WELL_TONE_FREQUENCIES.items() if k.startswith("chakra_")}
        return [
            TextContent(
                type="text",
                text=json.dumps(chakras, indent=2)
            )
        ]
    
    elif name == "calculate_harmonic_series":
        base = arguments["base_frequency"]
        count = arguments.get("harmonics_count", 10)
        harmonics = calculate_harmonic_series(base, count)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "harmonics": harmonics,
                    "count": len(harmonics)
                }, indent=2)
            )
        ]
    
    elif name == "calculate_pythagorean_frequency":
        base = arguments["base_frequency"]
        num = arguments["numerator"]
        den = arguments["denominator"]
        freq = calculate_pythagorean_ratio(base, (num, den))
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "ratio": f"{num}/{den}",
                    "calculated_frequency": freq
                }, indent=2)
            )
        ]
    
    elif name == "calculate_fibonacci_frequency":
        base = arguments["base_frequency"]
        index = arguments["fibonacci_index"]
        freq = calculate_fibonacci_frequency(base, index)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "fibonacci_index": index,
                    "calculated_frequency": freq
                }, indent=2)
            )
        ]
    
    elif name == "calculate_golden_ratio_frequency":
        base = arguments["base_frequency"]
        freq = calculate_golden_ratio_frequency(base)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "golden_ratio_frequency": freq,
                    "phi": (1 + math.sqrt(5)) / 2
                }, indent=2)
            )
        ]
    
    elif name == "calculate_prime_harmonics":
        base = arguments["base_frequency"]
        primes = arguments.get("primes", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        harmonics = calculate_prime_harmonics(base, primes)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "primes_used": primes,
                    "prime_harmonics": harmonics
                }, indent=2)
            )
        ]
    
    elif name == "generate_phi_spiral_frequencies":
        base = arguments["base_frequency"]
        count = arguments.get("count", 10)
        frequencies = generate_phi_based_frequencies(base, count)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "phi_spiral_frequencies": frequencies,
                    "count": len(frequencies)
                }, indent=2)
            )
        ]
    
    elif name == "calculate_quantum_harmonic":
        base = arguments["base_frequency"]
        level = arguments["quantum_level"]
        freq = calculate_quantum_harmonics(base, level)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "quantum_level": level,
                    "quantum_harmonic_frequency": freq
                }, indent=2)
            )
        ]
    
    elif name == "generate_fractal_frequencies":
        base = arguments["base_frequency"]
        depth = arguments.get("depth", 5)
        frequencies = generate_fractal_frequencies(base, depth)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "fractal_depth": depth,
                    "fractal_frequencies": frequencies,
                    "count": len(frequencies)
                }, indent=2)
            )
        ]
    
    elif name == "calculate_resonance_cascade":
        base = arguments["base_frequency"]
        steps = arguments.get("steps", 7)
        cascade = calculate_resonance_cascade(base, steps)
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "steps": steps,
                    "resonance_cascade": cascade
                }, indent=2)
            )
        ]
    
    elif name == "generate_custom_frequency_matrix":
        base = arguments["base_frequency"]
        include_fib = arguments.get("include_fibonacci", True)
        include_phi = arguments.get("include_golden_ratio", True)
        include_primes = arguments.get("include_primes", True)
        size = arguments.get("matrix_size", 8)
        
        matrix = []
        if include_fib:
            fib_freqs = [calculate_fibonacci_frequency(base, i) for i in range(min(size, 12))]
            matrix.extend(fib_freqs)
        if include_phi:
            phi_freqs = generate_phi_based_frequencies(base, size)
            matrix.extend(phi_freqs)
        if include_primes:
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29][:size]
            prime_freqs = calculate_prime_harmonics(base, primes)
            matrix.extend(prime_freqs)
        
        # Remove duplicates and sort
        matrix = sorted(set(matrix))
        
        return [
            TextContent(
                type="text",
                text=json.dumps({
                    "base_frequency": base,
                    "matrix_size": len(matrix),
                    "frequency_matrix": matrix,
                    "includes": {
                        "fibonacci": include_fib,
                        "golden_ratio": include_phi,
                        "primes": include_primes
                    }
                }, indent=2)
            )
        ]
    
    else:
        return [
            TextContent(
                type="text",
                text=json.dumps({"error": f"Unknown tool: {name}"})
            )
        ]


async def main():
    """Run the MCP server."""
    import sys
    # Write to stderr so it doesn't interfere with stdio communication
    print("Sound Healing MCP Server starting...", file=sys.stderr)
    print("Server name: sound-healing-mcp", file=sys.stderr)
    print("Version: 1.0.0", file=sys.stderr)
    print("Communication: stdio (standard input/output)", file=sys.stderr)
    print("Ready for MCP client connections...", file=sys.stderr)
    print("(Note: This server uses stdio, not HTTP/ports)", file=sys.stderr)
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="sound-healing-mcp",
                server_version="1.0.0",
                capabilities=ServerCapabilities()
            )
        )


if __name__ == "__main__":
    asyncio.run(main())
