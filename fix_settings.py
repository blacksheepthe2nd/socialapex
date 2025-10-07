# fix_settings.py
with open('socialapex/settings.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a proper newline at the end if missing
if not content.endswith('\n'):
    content += '\n'

with open('socialapex/settings.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed settings.py - added missing newline")