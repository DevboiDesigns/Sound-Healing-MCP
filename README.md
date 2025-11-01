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

## Quick Start

1. **Clone or download this repository**
2. **Install dependencies** (see Installation section below)
3. **Configure your MCP client** (see MCP Client Setup section)
4. **Start using the tools!**

## Installation

### Step 1: Install Python

Ensure you have Python 3.8 or higher installed:

```bash
# Check Python version
python3 --version  # macOS/Linux
python --version   # Windows
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

**Note:**

- On macOS/Linux, you may have both `python` (Python 2) and `python3` (Python 3). Always use `python3`.
- On Windows, `python` usually refers to Python 3 if you installed it correctly.

### Step 2: Clone or Download the Repository

**Option A: Clone with Git**

```bash
git clone https://github.com/yourusername/Sound-Healing-MCP.git
cd Sound-Healing-MCP
```

**Option B: Download ZIP**

1. Click "Download ZIP" on GitHub
2. Extract the ZIP file to your desired location
3. Open a terminal in the extracted folder

### Step 3: Install Dependencies

Navigate to the repository directory and install required packages:

**macOS/Linux:**

```bash
# Make sure you're in the Sound-Healing-MCP directory
cd Sound-Healing-MCP

# Install dependencies
pip3 install -r requirements.txt

# Or use python3 -m pip
python3 -m pip install -r requirements.txt
```

**Windows:**

```bash
# Make sure you're in the Sound-Healing-MCP directory
cd Sound-Healing-MCP

# Install dependencies
pip install -r requirements.txt

# Or use python -m pip
python -m pip install -r requirements.txt
```

**Verify installation:**

```bash
# Check if mcp package is installed
pip3 list | grep mcp  # macOS/Linux
pip list | findstr mcp  # Windows
```

### Step 4: Get the Server Path

You'll need the **absolute path** to `server.py` for configuration. Here's how to find it:

**macOS/Linux:**

```bash
# Get the absolute path
pwd
# Output example: /Users/yourusername/GitHub/Sound-Healing-MCP

# Full path to server.py
echo "$(pwd)/server.py"
# Output: /Users/yourusername/GitHub/Sound-Healing-MCP/server.py
```

**Windows:**

```cmd
REM Get the absolute path
cd
REM Output example: C:\Users\yourusername\GitHub\Sound-Healing-MCP

REM Full path to server.py
cd
echo %CD%\server.py
REM Output: C:\Users\yourusername\GitHub\Sound-Healing-MCP\server.py
```

**Important:**

- Use the **absolute path** (full path from root), not a relative path
- Copy this path - you'll need it in the next step

### Step 5: Test the Installation (Optional)

Test that the server can start:

```bash
# macOS/Linux
python3 server.py

# Windows
python server.py
```

The server will start and wait for connections (this is normal). Press `Ctrl+C` to stop it.

## MCP Client Setup

Now you need to configure the server in your MCP-compatible client. This tells your client how to start and communicate with the server.

**Choose your client:**

### Cursor

1. **Install the server:**

   ```bash
   git clone https://github.com/yourusername/Sound-Healing-MCP.git
   cd Sound-Healing-MCP
   pip3 install -r requirements.txt
   ```

2. **Find your Cursor MCP configuration:**

   - Open Cursor Settings
   - Navigate to Features → Model Context Protocol
   - Or manually edit: `~/.cursor/mcp.json` (macOS/Linux) or `%APPDATA%\Cursor\mcp.json` (Windows)

3. **Add the server configuration:**

   ```json
   {
     "mcpServers": {
       "sound-healing": {
         "command": "python3",
         "args": ["/absolute/path/to/Sound-Healing-MCP/server.py"]
       }
     }
   }
   ```

   **Important:** Replace `/absolute/path/to/Sound-Healing-MCP/server.py` with the actual path to your server.py file.

4. **Restart Cursor**

5. **Verify installation:** The sound healing tools should now be available in Cursor's MCP tools.

### Claude Desktop

1. **Install the server:**

   ```bash
   git clone https://github.com/yourusername/Sound-Healing-MCP.git
   cd Sound-Healing-MCP
   pip3 install -r requirements.txt
   ```

2. **Find your Claude Desktop configuration file:**

   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux:** `~/.config/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

3. **Edit or create the configuration file:**

   If the file doesn't exist, create it. If it exists, add to the existing `mcpServers` object:

   ```json
   {
     "mcpServers": {
       "sound-healing": {
         "command": "python3",
         "args": ["/absolute/path/to/Sound-Healing-MCP/server.py"]
       }
     }
   }
   ```

   **macOS/Linux example:**

   ```json
   {
     "mcpServers": {
       "sound-healing": {
         "command": "python3",
         "args": ["/Users/yourusername/GitHub/Sound-Healing-MCP/server.py"]
       }
     }
   }
   ```

   **Windows example:**

   ```json
   {
     "mcpServers": {
       "sound-healing": {
         "command": "python",
         "args": [
           "C:\\Users\\yourusername\\GitHub\\Sound-Healing-MCP\\server.py"
         ]
       }
     }
   }
   ```

4. **Restart Claude Desktop**

5. **Verify installation:** Open Claude Desktop, start a conversation, and check if the sound healing tools are available.

### Other MCP Clients

For other MCP-compatible clients, the configuration format is generally:

```json
{
  "mcpServers": {
    "sound-healing": {
      "command": "python3",
      "args": ["/path/to/server.py"]
    }
  }
}
```

**Tips:**

- Use absolute paths (not relative paths)
- On macOS/Linux, use `python3`. On Windows, use `python`
- Make sure Python and the `mcp` package are in your PATH
- Restart your client after making configuration changes
- See `mcp-config-examples/` directory for example configuration files

### Quick Setup Script

You can use the provided setup script to automatically install dependencies and get your server path:

**macOS/Linux:**

```bash
./setup-mcp.sh
```

**Windows:**

```batch
setup-mcp.bat
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

### Example Tool Calls

#### Get a Chakra Frequency

```json
{
  "tool": "get_well_tone_frequency",
  "arguments": {
    "frequency_name": "chakra_heart"
  }
}
```

**Expected result:** Returns the heart chakra frequency (639 Hz)

#### List All Well-Tone Frequencies

```json
{
  "tool": "list_all_well_tones",
  "arguments": {}
}
```

**Expected result:** Returns all well-tone frequencies organized by category

#### Calculate Harmonic Series

```json
{
  "tool": "calculate_harmonic_series",
  "arguments": {
    "base_frequency": 440,
    "harmonics_count": 10
  }
}
```

**Expected result:** Returns an array of 10 harmonic frequencies starting from 440 Hz

#### Generate Phi Spiral Frequencies

```json
{
  "tool": "generate_phi_spiral_frequencies",
  "arguments": {
    "base_frequency": 432,
    "count": 10
  }
}
```

**Expected result:** Returns frequencies following the golden ratio spiral pattern

#### Calculate Quantum Harmonic

```json
{
  "tool": "calculate_quantum_harmonic",
  "arguments": {
    "base_frequency": 528,
    "quantum_level": 5
  }
}
```

**Expected result:** Returns frequency calculated using quantum energy level formula (528 × 5² = 13,200 Hz)

### Using in Conversations

In Cursor or Claude Desktop, you can simply ask:

- "What are the chakra frequencies?"
- "Calculate harmonic series for 432 Hz"
- "Generate fractal frequencies starting from 528 Hz"
- "Show me all Solfeggio frequencies"
- "What is the quantum harmonic for level 3 at base frequency 440 Hz?"

The AI will automatically call the appropriate tools.

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

## Troubleshooting

### Server Won't Start

**Problem:** The server doesn't start or shows errors.

**Solutions:**

1. Check Python version: `python3 --version` (should be 3.8 or higher)
2. Verify dependencies are installed: `pip3 list | grep mcp`
3. Reinstall dependencies: `pip3 install --upgrade -r requirements.txt`
4. Check file path is correct and absolute (not relative)

### Tools Not Appearing in Client

**Problem:** Tools don't show up in Cursor/Claude Desktop.

**Solutions:**

1. Verify configuration file syntax (valid JSON)
2. Check the path is absolute and correct
3. Use correct Python command (`python3` on macOS/Linux, `python` on Windows)
4. Restart the client completely (quit and reopen)
5. Check client logs for errors
6. Verify Python and `mcp` package are in PATH

### "Command Not Found" Errors

**Problem:** Client can't find Python.

**Solutions:**

1. Find Python path: `which python3` (macOS/Linux) or `where python` (Windows)
2. Use full path in config: `"/usr/bin/python3"` instead of just `"python3"`
3. Verify Python is installed and in PATH

### Path Issues

**Problem:** Server file not found.

**Solutions:**

1. Use absolute paths (full path from root)
2. On Windows, use double backslashes: `C:\\Users\\...`
3. On macOS/Linux, use forward slashes: `/Users/...`
4. Verify the file exists at that path
5. Check for typos in the path

### Permission Errors

**Problem:** Permission denied when running server.

**Solutions:**

1. Make sure the Python script is readable: `chmod +r server.py`
2. Check directory permissions
3. On Linux/macOS, you might need to adjust file permissions

### Still Having Issues?

1. Check the client's MCP logs (usually in client settings or logs folder)
2. Test the server manually: `python3 server.py` (it should start and wait)
3. Verify MCP protocol compatibility with your client version
4. Try a simple test: Use the absolute path in a terminal to verify it works

## Contributing

Contributions are welcome! Feel free to add new frequency calculation methods, additional well-tone frequencies, or improve existing functionality.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Ideas for Contributions

- Additional well-tone frequencies
- New calculation methods
- Performance improvements
- Documentation enhancements
- Example configurations for other MCP clients
- Tests and test coverage

## Disclaimer

This server provides frequencies for informational and research purposes. Sound healing frequencies are complementary practices and should not replace medical treatment. Always consult with qualified healthcare professionals for medical conditions.
