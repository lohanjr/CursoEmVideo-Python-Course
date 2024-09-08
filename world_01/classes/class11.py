# COLORS IN THE TERMINAL
colors = {
    'stop':'\033[m',
    'yellow':'\033[33m',
    'green':'\033[32m',
    'red':'\033[31m'
}
print(f'{colors['yellow']}Hello World! In yellow...{colors['stop']}')
print(f'{colors['green']}Hello World! In green...{colors['stop']}')
print(f'{colors['red']}Hello World! In red...{colors['stop']}')