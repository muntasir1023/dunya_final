
$content = [System.IO.File]::ReadAllText("d:\Dunya website\vacancy.html", [System.Text.Encoding]::UTF8)

$oldBlock = @'
<h2 class="text-3xl md:text-5xl font-serif font-bold text-white mb-5" data-i18n="job_title">Are you looking for a fun part-time job?</h2>

                        </p>

                    </div>


                        <div class="w-28 h-28 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden">
'@

$newBlock = @'
<h2 class="text-3xl md:text-5xl font-serif font-bold text-white mb-5" data-i18n="job_title">Are you looking for a fun part-time job?</h2>
                        <p class="text-gray-300 text-lg leading-relaxed" data-i18n="job_intro">
                            Are you looking for a fun part-time job or holiday job in a friendly and international environment? Then we are looking for you!
                        </p>

                    </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
'@

$idx = $content.IndexOf($oldBlock)
if ($idx -ge 0) {
    Write-Host "Found old block at index: $idx"
    $content = $content.Replace($oldBlock, $newBlock)
    [System.IO.File]::WriteAllText("d:\Dunya website\vacancy.html", $content, [System.Text.Encoding]::UTF8)
    Write-Host "SUCCESS: File repaired! New size: $($content.Length)"
} else {
    Write-Host "ERROR: Old block not found!"
    $jidx = $content.IndexOf("job_title")
    Write-Host "job_title found at: $jidx"
    if ($jidx -ge 0) {
        Write-Host $content.Substring($jidx, 400)
    }
}
