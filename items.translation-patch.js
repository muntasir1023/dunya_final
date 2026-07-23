/*
  Patch for items.html product translations.
  Ensures every language has translations for all product ids: fresh-dairy + product-1..product-13.

  Loaded after items.html's inline script via <script src="items.translation-patch.js"></script>.
*/

(() => {
  try {
    const translations = window.productTranslations;
    if (!translations) return;

    const requiredProductIds = [
      'fresh-dairy',
      'product-1','product-2','product-3','product-4','product-5','product-6','product-7','product-8','product-9','product-10','product-11','product-12','product-13'
    ];

    const languages = ['en','nl','tr','ku','es','ar','fr','zz'];

    // Ensure english fallback is always present for required ids.
    // This prevents partial maps from breaking other languages.
    const en = translations.en || {};
    if (!translations.en) translations.en = {};

    // If a pid is missing in en, do nothing (cannot translate).
    for (const pid of requiredProductIds) {
      if (!translations.en[pid] && en[pid]) translations.en[pid] = { ...en[pid] };
    }

    // For every language, ensure required ids exist.
    for (const lang of languages) {
      if (!translations[lang]) translations[lang] = {};

      for (const pid of requiredProductIds) {
        if (!translations[lang][pid]) {
          const fallback = translations.en && translations.en[pid] ? translations.en[pid] : null;
          if (fallback) translations[lang][pid] = { ...fallback };
        }
      }
    }

    // IMPORTANT: after patching, re-render for the currently selected language.
    // Retry until items.html finished defining __itemsReRender and products grid.
    const currentLang = localStorage.getItem('dunya-language') || 'en';
    const tryRerender = (attempt) => {
      if (typeof window.__itemsReRender === 'function') {
        // Patch succeeded; force rebuild now.
        window.__itemsReRender(currentLang);
        // Re-apply once more to cover edge cases.
        setTimeout(() => {
          if (typeof window.__itemsReRender === 'function') window.__itemsReRender(currentLang);
        }, 50);
        return;
      }
      if (attempt < 40) setTimeout(() => tryRerender(attempt + 1), 25);
    };




    tryRerender(0);

  } catch (e) {
    // no-op
  }
})();



