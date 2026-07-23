$path = "d:/Dunya website/vacancy.html"
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

$old = "                    </div>

                        <div class=""w-20 h-20 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden"">
                            <img
                                src=""https://github.com/muntasir1023/dunya_final/blob/main/logo%205.jpeg""
                                alt=""DÜNYA logo""
                                class=""w-12 h-12 object-contain""
                                loading=""lazy""
                                onerror=""this.src='https://github.com/muntasir1023/dunya_final/blob/main/logo%205.jpeg'""
                            >
                        </div>
                </div>"

$new = "                    </div>
                    <!-- Mobile logo for Internship -->
                    <div class=""md:hidden flex items-center justify-start mt-6"">
                        <div class=""w-20 h-20 rounded-[2rem] glass-panel flex items-center justify-center overflow-hidden"">
                            <img
                                src=""https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true""
                                alt=""DÜNYA logo""
                                class=""w-12 h-12 object-contain""
                                loading=""lazy""
                                onerror=""this.src='https://raw.githubusercontent.com/muntasir1023/dunya_final/main/logo%205.jpeg?raw=true'""
                            >
                        </div>
                </div>"

if ($c.Contains($old)) {
    $c = $c.Replace($old, $new)
    [System.IO.File]::WriteAllText($path, $c, [System.Text.Encoding]::UTF8)
    Write-Host "SUCCESS: Fixed internship mobile logo section"
} else {
    Write-Host "FAILED: Could not find the exact pattern to replace"
    # Find nearby text
    $idx = $c.IndexOf("w-20 h-20 rounded-[2rem]")
    if ($idx -ge 0) {
        Write-Host "Found 'w-20 h-20' at index $idx"
        $start = [Math]::Max(0, $idx - 200)
        $len = [Math]::Min(600, $c.Length - $start)
        Write-Host "Context:"
        Write-Host $c.Substring($start, $len)
    }
}
