import re

with open('d:/Dunya website/vacancy.html', 'r', encoding='utf-8') as f:
    content = f.read()

# FIX 1: Fix the Internship mobile logo URL - change github.com/blob/ to raw.githubusercontent.com
old_url = 'https://github.com/muntasir1023/dunya_final/blob/main/logo%205.jpeg'
new_url = 'https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true'

# Only fix URLs inside the internship section (second occurrence)
# Actually let's just replace all occurrences safely
content = content.replace(old_url, new_url)

# FIX 2: The Internship mobile section lost its md:hidden wrapper div
# Look for the pattern: </div>\n\n                    <div class="w-20
# which indicates the opening div is missing
broken_internship_mobile = '''                    </div>

                        <div class="w-20 h-20 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden">
                            <img
                                src="https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true"
                                alt="DÜNYA logo"
                                class="w-12 h-12 object-contain"
                                loading="lazy"
                                onerror="this.src='https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true'"
                            >
                        </div>'''

fixed_internship_mobile = '''                    </div>
                    <!-- Mobile logo for Internship -->
                    <div class="md:hidden flex items-center justify-start mt-6">
                        <div class="w-20 h-20 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden">
                            <img
                                src="https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true"
                                alt="DÜNYA logo"
                                class="w-12 h-12 object-contain"
                                loading="lazy"
                                onerror="this.src='https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true'"
                            >
                        </div>'''

if broken_internship_mobile in content:
    content = content.replace(broken_internship_mobile, fixed_internship_mobile, 1)
    print("FIX 2: Fixed Internship mobile logo wrapper")
else:
    print("FIX 2: Could not find broken Internship mobile section pattern")
    # Show context
    idx = content.find('intern_badge')
    if idx > 0:
        # Find the mobile logo section after internship
        section = content[idx:idx+2000]
        print("Context around intern_badge:")
        print(section)

with open('d:/Dunya website/vacancy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved successfully")
</｜｜DSML｜｜parameter>
</invoke>
</｜｜DSML｜｜tool_calls>
