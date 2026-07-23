import re

with open('d:/Dunya website/vacancy.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the job_badge span and the grid that follows
job_badge_marker = '<span data-i18n="job_badge">Job Vacancy</span>'
grid_marker = '<div class="grid grid-cols-1 lg:grid-cols-2 gap-10">'

badge_pos = content.find(job_badge_marker)
grid_pos = content.find(grid_marker, badge_pos)

if badge_pos >= 0 and grid_pos >= 0:
    between = content[badge_pos:grid_pos]
    print("=== TEXT TO REPLACE ===")
    print(repr(between[:300]))
    print("=== END ===")
    
    # Build the replacement
    replacement = '''<span data-i18n="job_badge">Job Vacancy</span>
                        </div>
                        <h2 class="text-3xl md:text-5xl font-serif font-bold text-white mb-5" data-i18n="job_title">Are you looking for a fun part-time job?</h2>
                        <p class="text-gray-300 text-lg leading-relaxed" data-i18n="job_intro">Are you looking for a fun part-time job or holiday job in a friendly and international environment? Then we are looking for you!</p>
                    </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">'''
    
    # Replace from job_badge to the end of the grid marker div
    end_of_marker = grid_pos + len(grid_marker)
    old_section = content[badge_pos:end_of_marker]
    
    new_content = content[:badge_pos] + replacement + content[end_of_marker:]
    
    with open('d:/Dunya website/vacancy.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("SUCCESS: File updated")
else:
    print("FAIL: Could not locate markers")
    print(f"badge_pos={badge_pos}, grid_pos={grid_pos}")
</｜｜DSML｜｜parameter>
</invoke>
</｜｜DSML｜｜tool_calls>
