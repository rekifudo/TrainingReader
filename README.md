# Meaning Reader / 意群阅读器

An ebook-style English–Chinese reading workbench with short aligned paragraphs, subtle meaning-group colors, adjustable paced scrolling, and English read-aloud.

英文在上，中文紧接下方。每组编号，点击任意语言即可定位；朗读时整组高亮并跟随。适合阅读自己有权使用的论文、文章与学习材料。

## Try it

Download this repository and open **index.html** in Chrome. No installation, server, API key, or account is required. The included demo is original bilingual text.

1. Click **朗读英文** to hear English from the selected paragraph onward.
2. Choose a voice. Available voices come from your browser / operating system. Daniel is preferred when available, then other commonly available English male voice names; otherwise an English voice is used. Gender is not exposed reliably by the Web Speech API.
3. Adjust **朗读语速** (default 0.9×) and **音调** (default 0.8). Lower pitch can sound deeper, but does not guarantee a particular timbre or a natural, charismatic voice. Some engines ignore pitch. Local voices are marked `local`; other voices may process text through the browser's speech provider.
4. Click a numbered English or Chinese paragraph to start there. **定位当前段** brings the active pair back into view.
5. **上一段 / 下一段** navigate without losing the translation. **隐藏中文** supports English-only rereading.
6. **自动滚动** uses English word count (default 250 WPM). It is a separate mode from speech: actual speech timing determines read-aloud progress.
7. Space / Escape pause; manual wheel / touch or backgrounding also stop playback. Opening the page never autoplays.

Voice, pitch, rate, colors, translation visibility, and per-document position are saved in browser local storage. Cross-browser, cross-device and moved-file persistence are not guaranteed. Imported documents are not retained after reload: reimport the same JSON to resume its saved position. The page makes no application network requests; the selected speech provider may use the network.

## Bring your own reading material

Use **导入 JSON** to open already aligned bilingual material. PDF extraction and translation are **not** built into this release. Prepare the text with your own tools, then review the alignment before importing.

```json
{
  "id": "unique-document-id",
  "title": "My paper",
  "subtitle": "Author · Year",
  "pairs": [
    {
      "page": 1,
      "en": "Keep each idea close to its translation.",
      "zh": "让每个意思紧挨着对应翻译。",
      "chunks": [
        {"text": "Keep each idea", "role": "main"},
        {"text": "close to its translation.", "role": "modifier"}
      ]
    }
  ]
}
```

Prefer **1–2 sentences per pair**. Do not cut a sentence solely to meet a word limit. Retain speaker labels, page references, qualifications and citations. Supported color roles: `main`, `condition`, `reason`, `contrast`, `modifier`. Colors are interpretive hints, not authoritative grammatical parsing. `chunks` is optional; its text should preserve the English in `en`. An optional `originalImage` accepts a local or data URL for source-page inspection. Do not use untrusted remote URLs for private materials.

**导出阅读材料** downloads the current JSON. Only publish texts and translations you have permission to distribute. The public repository contains no uploaded course paper or personal documents.

## Build a single portable HTML

Python 3, standard library only:

```sh
python3 build.py example.json -o index.html
python3 build.py my-reading.json -o my-reading.html
node --check app.js
```

`template.html`, `style.css`, and `app.js` are the editable source; `index.html` embeds everything for easy sharing. Files are rendered as text, not executable HTML. Imported JSON should come from sources you trust, and large files / images may slow the browser.

## Scope and limits

This is a reading aid, not a validated speed-reading intervention. 250 WPM is a convenient adjustable preset, not a universal native-student comprehension standard. This release follows whole short paragraphs during speech; it does not offer word-level audio alignment, neural voice cloning, automatic PDF layout recovery, or automatic translation. Browser speech behavior and voice availability vary.

Web speech implementation reference: [MDN SpeechSynthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis), [pitch](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisUtterance/pitch).

## License

MIT for the reader code and the original demo. Imported documents keep their own licenses.
