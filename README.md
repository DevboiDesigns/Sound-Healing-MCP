# Sound Healing MCP Server

An MCP (Model Context Protocol) server that provides healing harmonic frequencies for therapeutic and wellness applications. This server offers access to well-known healing frequencies, experimental calculations, and innovative frequency generation methods.

## Features

### Well-Tone Frequencies
Access a comprehensive database of well-known healing frequencies including:
- **Chakra Frequencies**: Base (396 Hz), Sacral (417 Hz), Solar Plexus (528 Hz), Heart (639 Hz), Throat (741 Hz), Third Eye (852 Hz), Crown (963 Hz)
- **Solfeggio Frequencies**: Complete set of ancient Solfeggio tones (174, 285, 396, 417, 528, 639, 741, 852, 963 Hz)
- **Earth Resonance**: Schumann resonance frequencies (7.83 Hz, 8 Hz)
- **A-432 Hz Tuning**: Natural tuning frequency
- **Brainwave Frequencies**: Theta, Delta, Alpha, Beta, Gamma

### Experimental Calculations
- **Harmonic Series**: Calculate harmonic series from any base frequency
- **Pythagorean Ratios**: Generate frequencies using ancient Pythagorean ratios
- **Fibonacci Frequencies**: Create frequencies based on the Fibonacci sequence
- **Golden Ratio (Phi)**: Calculate frequencies using the golden ratio (1.618...)
- **Prime Harmonics**: Generate harmonics using prime numbers
- **Phi Spiral**: Create frequencies following golden ratio spirals

### Innovative Methods
- **Quantum Harmonics**: Calculate frequencies based on quantum energy levels
- **Fractal Frequencies**: Generate self-similar fractal-based frequencies
- **Resonance Cascade**: Create cascading resonance frequencies
- **Custom Frequency Matrix**: Combine multiple mathematical principles for unique frequency matrices

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
# On macOS/Linux, use pip3 or python3 -m pip
pip3 install -r requirements.txt

# Or alternatively:
python3 -m pip install -r requirements.txt

# On Windows, use:
pip install -r requirements.txt
```

## Usage

### Running the Server

```bash
# On macOS/Linux, use python3
python3 server.py

# On Windows, use:
python server.py
```

**Important:** This MCP server uses **stdio** (standard input/output) for communication, not HTTP/ports. It communicates via stdin/stdout streams, which is the standard way MCP servers work. The server waits for MCP protocol messages on stdin and responds on stdout.

When you run the server, it will wait for MCP client connections. You typically configure this server in an MCP-compatible client (like Claude Desktop, Cursor, or other MCP clients) where the client launches the server process and communicates with it via stdio.

### Available Tools

#### Well-Tone Tools
- `get_well_tone_frequency`: Get a specific well-tone frequency by name
- `list_all_well_tones`: List all available well-tone frequencies organized by category
- `get_chakra_frequencies`: Get all chakra healing frequencies

#### Calculation Tools
- `calculate_harmonic_series`: Calculate harmonic series from base frequency
- `calculate_pythagorean_frequency`: Calculate using Pythagorean ratios
- `calculate_fibonacci_frequency`: Calculate based on Fibonacci sequence
- `calculate_golden_ratio_frequency`: Calculate using golden ratio
- `calculate_prime_harmonics`: Calculate harmonics using prime numbers
- `generate_phi_spiral_frequencies`: Generate golden ratio spiral frequencies

#### Innovative Tools
- `calculate_quantum_harmonic`: Calculate quantum-level harmonics
- `generate_fractal_frequencies`: Generate fractal-based frequencies
- `calculate_resonance_cascade`: Calculate resonance cascade frequencies
- `generate_custom_frequency_matrix`: Generate custom frequency matrix combining multiple principles

## Example Usage

### Get a Chakra Frequency
```json
{
  "tool": "get_well_tone_frequency",
  "arguments": {
    "frequency_name": "chakra_heart"
  }
}
```

### Calculate Harmonic Series
```json
{
  "tool": "calculate_harmonic_series",
  "arguments": {
    "base_frequency": 440,
    "harmonics_count": 10
  }
}
```

### Generate Phi Spiral Frequencies
```json
{
  "tool": "generate_phi_spiral_frequencies",
  "arguments": {
    "base_frequency": 432,
    "count": 10
  }
}
```

### Calculate Quantum Harmonic
```json
{
  "tool": "calculate_quantum_harmonic",
  "arguments": {
    "base_frequency": 528,
    "quantum_level": 5
  }
}
```

## Frequency Categories

### Chakra Frequencies
- Base/Root: 396 Hz - Liberation from fear and guilt
- Sacral: 417 Hz - Undoing situations and facilitating change
- Solar Plexus: 528 Hz - Transformation and miracles (DNA repair)
- Heart: 639 Hz - Connection and relationships
- Throat: 741 Hz - Expression and solutions
- Third Eye: 852 Hz - Returning to spiritual order
- Crown: 963 Hz - Connection to higher consciousness

### Solfeggio Frequencies
Ancient six-tone scale used in sacred music:
- 174 Hz - Foundation of conscious development
- 285 Hz - Quantum cognition and quantum awareness
- 396 Hz - Liberation from fear and guilt
- 417 Hz - Facilitation of change
- 528 Hz - Transformation and miracles
- 639 Hz - Connection and relationships
- 741 Hz - Expression and solutions
- 852 Hz - Returning to spiritual order
- 963 Hz - Connection to higher consciousness

### Earth Resonance
- 7.83 Hz - Primary Schumann resonance (Earth's natural frequency)
- 8 Hz - Base Schumann resonance
- 432 Hz - Natural tuning frequency (A4)

### Brainwave States
- Delta: 0.5-4 Hz - Deep sleep, healing
- Theta: 4-8 Hz - Deep meditation, creativity
- Alpha: 8-13 Hz - Relaxed awareness, flow state
- Beta: 13-30 Hz - Active thinking, focus
- Gamma: 30-100 Hz - Peak concentration, insight

## Scientific Background

This server combines:
- **Traditional Knowledge**: Well-established healing frequencies used in sound therapy
- **Mathematical Principles**: Fibonacci sequence, golden ratio, prime numbers, fractals
- **Quantum Concepts**: Energy level calculations for quantum harmonics
- **Experimental Methods**: Novel approaches to frequency generation

## License

This project is provided as-is for public use. Please use responsibly and consult with healthcare professionals for medical applications.

## Contributing

Contributions are welcome! Feel free to add new frequency calculation methods, additional well-tone frequencies, or improve existing functionality.

## Disclaimer

This server provides frequencies for informational and research purposes. Sound healing frequencies are complementary practices and should not replace medical treatment. Always consult with qualified healthcare professionals for medical conditions.
