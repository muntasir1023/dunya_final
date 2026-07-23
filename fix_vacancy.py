#!/usr/bin/env python3
# Fix vacancy.html: Remove logo images from Job & Internship sections, fix broken HTML

import sys

FILEPATH = 'd:/Dunya website/vacancy.html'

with open(FILEPATH, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# ── Fix 1: Job section (missing <h2>/<p>, stray </div>, unwanted mobile logo) ──
job_fix_marker = 'data-i18n="job_title">Are you looking for a fun part-time job?</h2>'
if job_fix_marker not in content:
    old_job_block = '''                        </div>


<div class="md:hidden flex items-center justify-start mt-6">
                    <div class="w-20 h-20 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden">
                        <img
                            src="https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true"
                            alt="DÜNYA logo"
                            class="w-12 h-12 object-contain"
                            loading="lazy"
                            onerror="this.src='https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true'"
                        >
                    </div>

'''

    new_job_block = '''                        </div>

                        <h2 class="text-3xl md:text-5xl font-serif font-bold text-white mb-5" data-i18n="job_title">Are you looking for a fun part-time job?</h2>
                        <p class="text-gray-300 text-lg leading-relaxed" data-i18n="job_intro">
                            Are you looking for a fun part-time job or holiday job in a friendly and international environment? Then we are looking for you!
                        </p>

                    </div>

'''

    count = content.count(old_job_block)
    if count >= 1:
        content = content.replace(old_job_block, new_job_block, 1)
        print(f"Job section fixed (found {count} occurrence(s)).")
        changes += 1
    else:
        print("Job fix: old_block not found — may already be fixed or different.")
else:
    print("Job fix: already applied, skipping.")

# ── Fix 2: Internship section (stray broken logo images after intro <p>) ──
# Check if broken image block exists in the internship section
intern_marker_idx = content.find('Youve come to the right place.')
if intern_marker_idx == -1:
    # Try with smart quote
    intern_marker_idx = content.find("You've come to the right place.")
if intern_marker_idx == -1:
    intern_marker_idx = content.find("youve come to the right place")

if intern_marker_idx >= 0:
    # Check if the broken image markup still exists AFTER this marker (within next 600 chars)
    tail = content[intern_marker_idx:intern_marker_idx + 700]
    if 'logo%205' in tail:
        # Find the exact boundaries
        start = tail.find('</p>')
        if start >= 0:
            old_intern_tail = tail[start:]
            end = old_intern_tail.find('data-i18n="intern_learn_title"')
            if end >= 0:
                old_block = old_intern_tail[:end]
                # Only proceed if old_block contains broken image markup
                if 'logo' in old_block.lower() or 'image' in old_block.lower():
                    new_block = '</p>\n                    </div>\n                </div>\n\n                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">\n                    <div>\n                        <h3 class="text-xl md:text-2xl font-serif font-bold text-white mb-5 flex items-center gap-3">\n                            <i class="fa-solid fa-lightbulb text-dunya-light"></i>\n                            <span data-i18n="intern_learn_title"'
                    content = content.replace(old_block, new_block, 1)
                    print("Internship section fixed (removed broken logo images).")
                    changes += 1
                else:
                    print("Internship fix: no logo markup found in tail, already clean.")
            else:
                print("Internship fix: could not find intern_learn_title marker.")
        else:
            print("Internship fix: could not find </p> for boundary.")
    else:
        print("Internship fix: already applied, no logo markup remaining.")
else:
    print("Internship fix: could not find marker text.")

# ── Save if any changes were made ──
if changes > 0:
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nSUCCESS: {changes} fix(es) applied to {FILEPATH}")
else:
    print("\nNo changes needed — file is already clean.")
