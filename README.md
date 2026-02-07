# Q-SYS Log to Text Converter

A simple Python utility to convert Q-SYS `.qsyslog` files (gzip-compressed tar archives) into readable `.txt` format for easier analysis and troubleshooting.

## Features

- Extracts all file contents from `.qsyslog` archives
- Works with any Q-SYS device type
- Outputs a single text file with all extracted content
- Simple command-line interface
- No external dependencies (standard library only)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository or download `qsyslog_to_txt.py`
2. Make the script executable (optional):
   ```bash
   chmod +x qsyslog_to_txt.py
   ```

## Usage

Basic usage:
```bash
python qsyslog_to_txt.py <input.qsyslog>
```

Specify custom output file:
```bash
python qsyslog_to_txt.py <input.qsyslog> <output.txt>
```

If no output path is specified, the script creates a `.txt` file with the same name as the input file in the same directory.

### Example

```bash
python qsyslog_to_txt.py p_p_VENC-A4-2026-2-6T201426.qsyslog
# Output: p_p_VENC-A4-2026-2-6T201426.txt

python qsyslog_to_txt.py system.qsyslog logs/system_readable.txt
# Output: logs/system_readable.txt
```

## Disclaimer

**This tool is provided "as-is" without warranty of any kind, either expressed or implied. Use at your own risk.**

This project is **not affiliated with, endorsed by, or associated with QSC, LLC** or Q-SYS in any way. Q-SYS and QSC are trademarks of QSC, LLC.

THE SOFTWARE IS PROVIDED WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## License

This project is released under the MIT License. See LICENSE file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Author

Created for troubleshooting and analysis of Q-SYS system logs.
